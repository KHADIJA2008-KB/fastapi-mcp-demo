# FastAPI MCP Server

A FastAPI application that acts as a Model Context Protocol (MCP) Server, exposing tools that can be called by Gemini CLI.

## Features

- **Hello Tool**: Returns a personalized greeting message
- **Add Tool**: Performs addition of two numbers

## Setup

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the FastAPI server:
```bash
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

## API Endpoints

### Hello Tool
- **URL**: `/tools/hello`
- **Method**: GET
- **Parameters**: 
  - `name` (optional, default: "Student"): Name to greet
- **Example**: `http://localhost:8000/tools/hello?name=Khadija`

### Add Tool
- **URL**: `/tools/add`
- **Method**: GET
- **Parameters**:
  - `a` (required): First number
  - `b` (required): Second number
- **Example**: `http://localhost:8000/tools/add?a=5&b=3`

## Testing

You can test the endpoints using:
- Browser: Visit `http://localhost:8000/docs` for interactive API documentation
- cURL: `curl "http://localhost:8000/tools/hello?name=Khadija"`
- Gemini CLI: Configure using `mcp_config.json`

## MCP Configuration

The `mcp_config.json` file contains the configuration for connecting this server to Gemini CLI.

## Project Structure

```
fastapi-mcp-demo/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── mcp_config.json     # MCP configuration for Gemini CLI
├── README.md           # This file
└── venv/               # Virtual environment
```

