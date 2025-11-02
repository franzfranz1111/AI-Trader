# Railway Deployment Guide

## Schritt 1: Railway Account
1. Gehe zu https://railway.app
2. Registriere dich (GitHub-Login empfohlen)

## Schritt 2: Neues Projekt erstellen
1. Klicke "New Project"
2. Wähle "Deploy from GitHub repo"
3. Verbinde dein GitHub-Konto
4. Push dieses Repo zu GitHub
5. Wähle das Repo aus

## Schritt 3: Environment Variables setzen
Gehe zu "Variables" und füge hinzu:

```
OPENAI_API_KEY=dein_openai_key
OPENAI_API_BASE=https://api.openai.com/v1
ALPHAADVANTAGE_API_KEY=dein_alpha_vantage_key
JINA_API_KEY=dein_jina_key

DASHBOARD_USER=admin
DASHBOARD_PASSWORD=dein_sicheres_passwort

MATH_HTTP_PORT=8000
SEARCH_HTTP_PORT=8001
TRADE_HTTP_PORT=8002
GETPRICE_HTTP_PORT=8003

AGENT_MAX_STEP=30
RUNTIME_ENV_PATH=/app/.runtime_env.json
```

## Schritt 4: Deploy
- Railway deployt automatisch
- Warte ~2-3 Minuten
- Dashboard URL findest du unter "Settings" → "Networking"

## Schritt 5: Trading Bot starten (optional)
Wenn du Trading laufen lassen willst:
1. Erstelle zweites Service im gleichen Projekt
2. Start Command: `python main.py`
3. Nutzt gleiche Environment Variables

## Login
- URL: https://dein-projekt.railway.app
- Username: admin (oder was du in DASHBOARD_USER gesetzt hast)
- Password: dein_sicheres_passwort

## Kosten
- ~$5-10/Monat je nach Nutzung
- Erste $5 sind gratis
