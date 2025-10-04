# Quick Reference Guide 🚀

## Essential Commands

### Start the Server
```bash
cd /home/khadijab/fastapi-mcp-demo
source venv/bin/activate
uvicorn main:app --reload
```

### Stop the Server
Press `Ctrl+C` in the terminal running uvicorn

### Test Everything
```bash
./demo_script.sh
```

## API Endpoints

### Hello Tool
```bash
# Default greeting
curl "http://localhost:8000/tools/hello"

# Custom name
curl "http://localhost:8000/tools/hello?name=Khadija"
```

**Response**: `{"message":"Hello, [name]! This is your MCP Server speaking 👋"}`

### Add Tool
```bash
curl "http://localhost:8000/tools/add?a=10&b=20"
```

**Response**: `{"result":30}`

## Important URLs

| URL | Description |
|-----|-------------|
| `http://localhost:8000` | API root |
| `http://localhost:8000/docs` | Swagger UI (Interactive docs) |
| `http://localhost:8000/redoc` | ReDoc documentation |
| `http://localhost:8000/openapi.json` | OpenAPI schema |

## Git Commands

### Initial Commit
```bash
git commit -m "Initial commit: FastAPI MCP Server with Gemini CLI integration"
```

### Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/fastapi-mcp-demo.git
git branch -M main
git push -u origin main
```

### Check Status
```bash
git status
git log --oneline
```

## Troubleshooting

### Server won't start
```bash
# Check if port 8000 is in use
netstat -tuln | grep 8000

# Kill process using port 8000
kill $(lsof -t -i:8000)

# Restart server
uvicorn main:app --reload
```

### Virtual environment issues
```bash
# Recreate virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Dependencies missing
```bash
source venv/bin/activate
pip install -r requirements.txt
```

## File Locations

```
/home/khadijab/fastapi-mcp-demo/
├── main.py              ← FastAPI application
├── requirements.txt     ← Dependencies
├── mcp_config.json     ← MCP configuration
├── demo_script.sh      ← Demo script
└── README.md           ← Full documentation
```

## Testing Checklist

- [ ] Server starts without errors
- [ ] Hello tool responds correctly
- [ ] Add tool calculates correctly
- [ ] API docs accessible at /docs
- [ ] Demo script runs successfully
- [ ] All files committed to git

## Recording Demo

```bash
# 1. Start server
uvicorn main:app --reload

# 2. In another terminal, run demo
./demo_script.sh

# 3. Open browser
firefox http://localhost:8000/docs
```

## Gemini CLI Integration

### Configure MCP
```bash
# Option 1: Environment variable
export MCP_CONFIG_PATH="/home/khadijab/fastapi-mcp-demo/mcp_config.json"

# Option 2: Copy to config directory
mkdir -p ~/.config/gemini/mcp
cp mcp_config.json ~/.config/gemini/mcp/fastapi-mcp.json
```

### Use with Gemini
```bash
gemini mcp list
gemini mcp call fastapi-mcp hello --name="Khadija"
gemini mcp call fastapi-mcp add --a=10 --b=25
```

## Common Issues

**Problem**: Port 8000 already in use
**Solution**: `kill $(lsof -t -i:8000)` or use different port: `uvicorn main:app --port 8001`

**Problem**: Module not found
**Solution**: `source venv/bin/activate && pip install -r requirements.txt`

**Problem**: Git push rejected
**Solution**: Ensure you created the GitHub repo first, then `git push -u origin main`

## Support Files

| File | Purpose |
|------|---------|
| `README.md` | Complete documentation |
| `GEMINI_CLI_SETUP.md` | Gemini CLI integration |
| `GITHUB_UPLOAD.md` | GitHub instructions |
| `SCREEN_RECORDING_GUIDE.md` | Video demo guide |
| `PROJECT_SUMMARY.md` | Project overview |
| `QUICK_REFERENCE.md` | This file |

---

**Quick Help**: For detailed information, see the corresponding `.md` files in the project root.

