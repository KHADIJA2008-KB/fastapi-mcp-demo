from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from datetime import datetime
import math
import os

app = FastAPI(
    title="FastAPI MCP Server",
    description="MCP Server with multiple tools for Gemini CLI integration",
    version="1.0.0"
)

# Serve static files (for the web UI)
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Tool 1: Greeting Tool
@app.get("/tools/hello")
def hello_tool(name: str = "Student"):
    """
    MCP Tool: Returns a personalized greeting message.
    """
    return {
        "message": f"Hello, {name}! This is your MCP Server speaking 👋",
        "timestamp": datetime.now().isoformat()
    }

# Tool 2: Math Addition Tool
@app.get("/tools/add")
def add_tool(a: int, b: int):
    """
    MCP Tool: Adds two numbers and returns the result.
    """
    return {
        "operation": "addition",
        "a": a,
        "b": b,
        "result": a + b
    }

# Tool 3: Math Multiply Tool
@app.get("/tools/multiply")
def multiply_tool(a: float, b: float):
    """
    MCP Tool: Multiplies two numbers.
    """
    return {
        "operation": "multiplication",
        "a": a,
        "b": b,
        "result": a * b
    }

# Tool 4: Temperature Converter
@app.get("/tools/temp-convert")
def temp_convert_tool(celsius: float):
    """
    MCP Tool: Converts Celsius to Fahrenheit and Kelvin.
    """
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return {
        "celsius": celsius,
        "fahrenheit": round(fahrenheit, 2),
        "kelvin": round(kelvin, 2)
    }

# Tool 5: Text Analysis Tool
@app.get("/tools/analyze-text")
def analyze_text_tool(text: str):
    """
    MCP Tool: Analyzes text and returns statistics.
    """
    words = text.split()
    return {
        "text": text,
        "character_count": len(text),
        "word_count": len(words),
        "uppercase_count": sum(1 for c in text if c.isupper()),
        "lowercase_count": sum(1 for c in text if c.islower()),
        "digit_count": sum(1 for c in text if c.isdigit())
    }

# Tool 6: Square Root Calculator
@app.get("/tools/sqrt")
def sqrt_tool(number: float):
    """
    MCP Tool: Calculates the square root of a number.
    """
    if number < 0:
        return {"error": "Cannot calculate square root of negative number"}
    return {
        "number": number,
        "square_root": round(math.sqrt(number), 4)
    }

# Root endpoint - Serve the web UI
@app.get("/")
def root():
    """Serve the sample app web interface."""
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    index_file = os.path.join(static_dir, "index.html")
    
    if os.path.exists(index_file):
        return FileResponse(index_file)
    else:
        # Fallback to JSON if static files don't exist
        return {
            "name": "FastAPI MCP Server",
            "version": "1.0.0",
            "status": "running",
            "available_tools": [
                "/tools/hello",
                "/tools/add",
                "/tools/multiply",
                "/tools/temp-convert",
                "/tools/analyze-text",
                "/tools/sqrt"
            ],
            "documentation": "/docs",
            "web_ui": "Static files not found. Use /docs for API documentation."
        }

# API info endpoint
@app.get("/api/info")
def api_info():
    """Get server information via API."""
    return {
        "name": "FastAPI MCP Server",
        "version": "1.0.0",
        "status": "running",
        "available_tools": [
            "/tools/hello",
            "/tools/add",
            "/tools/multiply",
            "/tools/temp-convert",
            "/tools/analyze-text",
            "/tools/sqrt"
        ],
        "documentation": "/docs",
        "mcp_config": "/mcp-config"
    }

# MCP Configuration endpoint
@app.get("/mcp-config")
def get_mcp_config():
    """Get the MCP configuration for this server."""
    return {
        "mcpServers": {
            "fastapi-mcp": {
                "url": "http://localhost:8000",
                "description": "FastAPI MCP Server with multiple utility tools",
                "tools": [
                    {
                        "name": "hello",
                        "endpoint": "/tools/hello",
                        "method": "GET",
                        "description": "Returns a personalized greeting message with timestamp"
                    },
                    {
                        "name": "add",
                        "endpoint": "/tools/add",
                        "method": "GET",
                        "description": "Adds two numbers and returns the result"
                    },
                    {
                        "name": "multiply",
                        "endpoint": "/tools/multiply",
                        "method": "GET",
                        "description": "Multiplies two numbers"
                    },
                    {
                        "name": "temp-convert",
                        "endpoint": "/tools/temp-convert",
                        "method": "GET",
                        "description": "Converts temperature from Celsius to Fahrenheit and Kelvin"
                    },
                    {
                        "name": "analyze-text",
                        "endpoint": "/tools/analyze-text",
                        "method": "GET",
                        "description": "Analyzes text and returns character/word statistics"
                    },
                    {
                        "name": "sqrt",
                        "endpoint": "/tools/sqrt",
                        "method": "GET",
                        "description": "Calculates the square root of a number"
                    }
                ]
            }
        }
    }

