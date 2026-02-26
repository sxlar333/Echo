@echo off
echo Installing dependencies for this repo...
echo Please open a GitHub issue if you run into problems.
echo.

python -m pip install --upgrade pip
python -m pip install colorama colorist pystyle requests discord.py requests beautifulsoup4 rich

echo.
echo Setup complete. Press any key to run the tool.
pause

python multi-tool.py
