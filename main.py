from fastapi import FastAPI

app = FastAPI(title="FastAPI MCP Server")

# Example MCP tool endpoint
@app.get("/tools/hello")
def hello_tool(name: str = "Student"):
    """
    Example MCP Tool: Returns a greeting message.
    """
    return {"message": f"Hello, {name}! This is your MCP Server speaking 👋"}

@app.get("/tools/add")
def add_tool(a: int, b: int):
    """
    Example MCP Tool: Adds two numbers.
    """
    return {"result": a + b}

