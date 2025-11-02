@echo off
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
python agent_tools/start_mcp_services.py
