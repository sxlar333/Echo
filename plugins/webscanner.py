import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import defaultdict
from rich.console import Console
from rich.tree import Tree

console = Console()

INTERESTING_EXTS = {
    "bak", "old", "zip", "rar", "7z",
    "sql", "db", "env", "log", "js",
    "php", "jsp", "asp", "aspx", "py"
}

INTERESTING_DIRS = {
    "admin", "administrator", "backend", "panel",
    "manage", "management", "database", "db",
    "internal", "private", "secure", "hidden"
}


def get_depth(path):
    return len([p for p in path.split("/") if p])


def get_last_dir(path):
    parts = [p for p in path.split("/") if p]
    return parts[-1].lower() if parts else ""


def crawl_site(base_url, max_depth=3, recurse_only_interesting=False):
    visited = set()
    found = {}
    domain = urlparse(base_url).netloc

    def crawl(url):
        if url in visited:
            return
        visited.add(url)

        try:
            r = requests.get(
                url,
                timeout=5,
                allow_redirects=False
            )
        except requests.RequestException:
            return

        status = r.status_code
        redirect = r.headers.get("Location")

        parsed_url = urlparse(url)
        path = parsed_url.path or "/"

        found[path] = {
            "url": url,
            "status": status,
            "redirect": redirect
        }

        # Stop if depth exceeded
        if get_depth(path) >= max_depth:
            return

        # Stop recursion if option enabled and dir is not interesting
        if recurse_only_interesting and get_depth(path) > 0:
            last_dir = get_last_dir(path)
            if last_dir not in INTERESTING_DIRS:
                return

        # Only parse HTML
        content_type = r.headers.get("Content-Type", "")
        if "text/html" not in content_type:
            return

        soup = BeautifulSoup(r.text, "html.parser")

        for link in soup.find_all("a", href=True):
            full = urljoin(url, link["href"])
            parsed = urlparse(full)

            if parsed.netloc != domain:
                continue

            clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
            crawl(clean_url)

    crawl(base_url)
    return found


def build_tree(paths):
    tree = lambda: defaultdict(tree)
    root = tree()

    for path, data in paths.items():
        parts = [p for p in path.split("/") if p]
        current = root

        for part in parts:
            current = current[part]

        current["_meta"] = data

    return root


def render_tree(tree_dict, base_url):
    tree = Tree(base_url)

    def add_nodes(node, subtree):
        for key, value in sorted(subtree.items()):
            if key == "_meta":
                continue

            meta = value.get("_meta", {})
            url = meta.get("url", "")
            status = meta.get("status", "")
            redirect = meta.get("redirect")

            is_file = "." in key
            ext = key.split(".")[-1] if is_file else ""

            interesting_file = ext in INTERESTING_EXTS
            interesting_dir = (not is_file) and key.lower() in INTERESTING_DIRS

            label = key

            if interesting_dir:
                label += " [DIR!]"
            if ext:
                label += f" [{ext}]"
            if interesting_file:
                label += " (!)"
            if status:
                label += f" [{status}]"
            if redirect:
                label += f" -> {redirect}"
            if url:
                label += f" → {url}"

            branch = node.add(label)
            add_nodes(branch, value)

    add_nodes(tree, tree_dict)
    return tree


def main():
    print("Simple Web Tree Scanner\n")

    url = input("Target URL: ").strip()

    depth_input = input("Max depth [3]: ").strip()
    max_depth = int(depth_input) if depth_input.isdigit() else 3

    recurse_input = input(
        "Only recurse into interesting directories? [y/N]: "
    ).strip().lower()
    recurse_only_interesting = recurse_input == "y"

    print("\nScanning...\n")

    paths = crawl_site(
        url,
        max_depth=max_depth,
        recurse_only_interesting=recurse_only_interesting
    )

    tree_data = build_tree(paths)
    tree = render_tree(tree_data, url)

    console.print(tree)
    print(f"\nFound {len(paths)} paths")


if __name__ == "__main__":
    main()
