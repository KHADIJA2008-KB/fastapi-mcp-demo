# Connecting FastAPI MCP Server to Gemini CLI

This guide explains how to connect your FastAPI MCP Server to Google's Gemini CLI.

## Prerequisites

1. FastAPI server running at `http://localhost:8000`
2. Gemini CLI installed (Google AI CLI)

## Step 1: Install Gemini CLI

If you haven't installed Gemini CLI yet:

```bash
# Using pip
pip install google-generativeai

# Or using npm (if using Node.js version)
npm install -g @google/generative-ai
```

## Step 2: Configure MCP Server

The `mcp_config.json` file in this project contains the MCP configuration. You need to register this with Gemini CLI.

### Option A: Using Environment Variable

```bash
export MCP_CONFIG_PATH="/home/khadijab/fastapi-mcp-demo/mcp_config.json"
```

### Option B: Copy to Gemini Config Directory

```bash
# Create Gemini config directory if it doesn't exist
mkdir -p ~/.config/gemini/mcp

# Copy the MCP config
cp mcp_config.json ~/.config/gemini/mcp/fastapi-mcp.json
```

## Step 3: Verify Server is Running

```bash
# Check if server is running
curl http://localhost:8000/docs

# Test the tools
curl "http://localhost:8000/tools/hello?name=YourName"
curl "http://localhost:8000/tools/add?a=5&b=10"
```

## Step 4: Use Gemini CLI with MCP Tools

### List Available MCP Servers
```bash
gemini mcp list
```

### Call MCP Tools via Gemini CLI

```bash
# Using the hello tool
gemini mcp call fastapi-mcp hello --name="Khadija"

# Using the add tool
gemini mcp call fastapi-mcp add --a=10 --b=25
```

## Step 5: Test with Gemini Chat

You can also use these tools within a Gemini chat session:

```bash
gemini chat --enable-mcp

# Then in the chat:
> Use the hello tool to greet me
> Use the add tool to calculate 42 + 58
```

## Alternative: Direct HTTP Testing

If Gemini CLI is not available, you can test the MCP server directly:

```bash
# Using curl
curl "http://localhost:8000/tools/hello?name=Student"
curl "http://localhost:8000/tools/add?a=10&b=20"

# Using the provided test script
./test_endpoints.sh

# Or open in browser
# http://localhost:8000/docs
```

## MCP Server Architecture

```
┌─────────────┐         HTTP          ┌──────────────────┐
│  Gemini CLI │ ◄──────────────────► │  FastAPI Server  │
│             │      GET /tools/*     │   (Port 8000)    │
└─────────────┘                       └──────────────────┘
       ▲                                       │
       │                                       │
       │                                       ▼
       │                              ┌──────────────────┐
       └─────── MCP Config ──────────│  mcp_config.json  │
                                      └──────────────────┘
```

## Troubleshooting

### Server not responding
```bash
# Check if server is running
ps aux | grep uvicorn

# Check the port
netstat -tuln | grep 8000

# Restart the server
cd /home/khadijab/fastapi-mcp-demo
source venv/bin/activate
uvicorn main:app --reload
```

### Gemini CLI can't find MCP server
- Verify `mcp_config.json` is in the correct location
- Check that the URL in the config matches your server address
- Ensure the server is running before calling MCP tools

## Recording Your Demo

For your screen recording, demonstrate:

1. **Terminal 1**: FastAPI server running
   ```bash
   uvicorn main:app --reload
   ```

2. **Terminal 2**: List MCP servers
   ```bash
   gemini mcp list
   ```

3. **Terminal 3**: Call MCP tools
   ```bash
   curl "http://localhost:8000/tools/hello?name=Khadija"
   curl "http://localhost:8000/tools/add?a=10&b=25"
   ```

4. **Browser**: Open `http://localhost:8000/docs` to show interactive API docs

