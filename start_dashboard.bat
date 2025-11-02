@echo off
chcp 65001 >nul
echo 📊 Starting AI-Trader Dashboard...
echo 🌐 Open your browser at: http://localhost:8888
echo.
cd docs
python -m http.server 8888
