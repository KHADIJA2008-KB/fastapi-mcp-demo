# 🚀 FastAPI MCP Server — Integrated with Gemini CLI

This project demonstrates how to **create and integrate a FastAPI-based MCP (Model Context Protocol) Server** with **Gemini CLI**.  
The server exposes multiple tool endpoints categorized into **Mathematical**, **Conversion**, **Text Processing**, and **Utility** operations.  

---

## 🧩 Overview

The FastAPI MCP Server runs locally and exposes tools that can be called using **Gemini CLI**.  
Each tool is a REST endpoint (e.g., `/tools/add`, `/tools/hello`, etc.), and Gemini CLI acts as a client to execute them.

---

## 🧠 Tools Summary

### 🧮 **Mathematical Tools**
| Tool | Endpoint | Description | Example |
|------|-----------|--------------|----------|
| **add** | `/tools/add?a=5&b=3` | Adds two numbers | `{"result": 8}` |
| **multiply** | `/tools/multiply?a=4&b=6` | Multiplies two numbers | `{"result": 24}` |
| **sqrt** | `/tools/sqrt?value=9` | Calculates square root | `{"result": 3.0}` |

---

### 🌡️ **Conversion Tools**
| Tool | Endpoint | Description | Example |
|------|-----------|--------------|----------|
| **temp-convert** | `/tools/temp-convert?celsius=25` | Converts Celsius to Fahrenheit & Kelvin | `{"fahrenheit": 77, "kelvin": 298.15}` |

---

### 📝 **Text Processing**
| Tool | Endpoint | Description | Example |
|------|-----------|--------------|----------|
| **analyze-text** | `/tools/analyze-text?text=Hello+World` | Analyzes character & word count | `{"characters": 11, "words": 2}` |

---

### ⚙️ **Utility Tools**
| Tool | Endpoint | Description | Example |
|------|-----------|--------------|----------|
| **hello** | `/tools/hello?name=Khadija` | Returns personalized greeting with timestamp | `{"message": "Hello, Khadija! 👋", "timestamp": "2025-10-04 17:30:00"}` |

---

## 🧰 Project Structure

2️⃣ Setup Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```

3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

🚀 Run MCP Server
```
uvicorn main:app --reload
```

--> Server will start at http://127.0.0.1:8000/docs
.

🔌 Configure Gemini CLI Integration
- Step 1: Create .mcp-config.json
```
{
  "servers": {
    "fastapi-mcp": {
      "command": "uvicorn",
      "args": ["main:app", "--host", "127.0.0.1", "--port", "8000"]
    }
  }
}
```

- Step 2: Move it to Gemini config folder
```
mkdir -p ~/.gemini
cp .mcp-config.json ~/.gemini/
```

🧠 Using Gemini CLI
1️⃣ Authenticate with Gemini

- Get your API key from Google AI Studio:
```
export GEMINI_API_KEY="your_api_key_here"
```

2️⃣ Verify Authentication
```
gemini models list
```

3️⃣ List MCP Servers
```
gemini mcp list
```

- Expected output:
```
fastapi-mcp    local    configured
```

4️⃣ Call MCP Tools via CLI
Example	Command
Greeting Tool	gemini mcp call fastapi-mcp /tools/hello name=Khadija
Add Numbers	gemini mcp call fastapi-mcp /tools/add a=5 b=8
Multiply Numbers	gemini mcp call fastapi-mcp /tools/multiply a=3 b=7
Square Root	gemini mcp call fastapi-mcp /tools/sqrt value=49
Convert Temp	gemini mcp call fastapi-mcp /tools/temp-convert celsius=30
Analyze Text	gemini mcp call fastapi-mcp /tools/analyze-text text="Hello FastAPI MCP"
📽️ Demo Video

- A screen recording of:

- MCP Server running

- gemini mcp list output

- CLI calls to tools

is included as demo.mp4 in this repository.

🧾 Requirements

- Python 3.8+

- FastAPI

- Uvicorn

- Node.js + npm

- Gemini CLI (npm install -g @google/gemini-cli)

✨ Author

- Khadija B.
- AI SkillBridge Bootcamp Project — FastAPI MCP Integration with Gemini CLI

📜 License

This project is open-source under the MIT License.
