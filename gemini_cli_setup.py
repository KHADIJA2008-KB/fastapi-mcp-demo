#!/usr/bin/env python3
"""
Gemini CLI MCP Integration Helper
This script helps you interact with your FastAPI MCP Server using Gemini-style commands
"""

import requests
import json
import sys

SERVER_URL = "http://localhost:8000"

class GeminiMCPClient:
    """Simple client that mimics Gemini CLI behavior"""
    
    def __init__(self, server_url):
        self.server_url = server_url
        self.config = None
        
    def list_tools(self):
        """List all available MCP tools"""
        try:
            response = requests.get(f"{self.server_url}/mcp-config")
            if response.status_code == 200:
                config = response.json()
                print("\n📋 Available MCP Tools:\n")
                print("="*60)
                
                tools = config['mcpServers']['fastapi-mcp']['tools']
                for i, tool in enumerate(tools, 1):
                    print(f"\n{i}. {tool['name']}")
                    print(f"   Description: {tool['description']}")
                    print(f"   Endpoint: {tool['endpoint']}")
                    print(f"   Method: {tool['method']}")
                
                print("\n" + "="*60)
                print(f"\nTotal tools: {len(tools)}")
                return tools
            else:
                print(f"❌ Error: Unable to fetch tools (Status: {response.status_code})")
                return None
        except requests.exceptions.ConnectionError:
            print("❌ Error: Cannot connect to MCP server at", self.server_url)
            print("   Make sure the server is running: ./start_server.sh")
            return None
    
    def call_tool(self, tool_name, **params):
        """Call a specific MCP tool"""
        try:
            # Map tool names to endpoints
            endpoints = {
                'hello': '/tools/hello',
                'add': '/tools/add',
                'multiply': '/tools/multiply',
                'temp-convert': '/tools/temp-convert',
                'analyze-text': '/tools/analyze-text',
                'sqrt': '/tools/sqrt'
            }
            
            if tool_name not in endpoints:
                print(f"❌ Error: Unknown tool '{tool_name}'")
                print(f"   Available tools: {', '.join(endpoints.keys())}")
                return None
            
            endpoint = endpoints[tool_name]
            url = f"{self.server_url}{endpoint}"
            
            print(f"\n🔧 Calling MCP Tool: {tool_name}")
            print(f"   URL: {url}")
            print(f"   Parameters: {params}")
            print()
            
            response = requests.get(url, params=params)
            
            if response.status_code == 200:
                result = response.json()
                print("✅ Success! Response:")
                print("="*60)
                print(json.dumps(result, indent=2))
                print("="*60)
                return result
            else:
                print(f"❌ Error: {response.status_code}")
                print(response.text)
                return None
                
        except requests.exceptions.ConnectionError:
            print("❌ Error: Cannot connect to MCP server")
            return None
    
    def interactive_mode(self):
        """Interactive mode for testing tools"""
        print("\n" + "="*60)
        print("  🤖 Gemini-style MCP Client - Interactive Mode")
        print("="*60)
        
        while True:
            print("\nCommands:")
            print("  list    - List all available MCP tools")
            print("  call    - Call a specific MCP tool")
            print("  exit    - Exit interactive mode")
            
            cmd = input("\n> ").strip().lower()
            
            if cmd == 'exit':
                print("\n👋 Goodbye!")
                break
            elif cmd == 'list':
                self.list_tools()
            elif cmd == 'call':
                self.interactive_call()
            else:
                print("❌ Unknown command. Try: list, call, or exit")
    
    def interactive_call(self):
        """Interactive tool calling"""
        print("\nAvailable tools:")
        print("  1. hello        - Greeting tool")
        print("  2. add          - Addition calculator")
        print("  3. multiply     - Multiplication calculator")
        print("  4. temp-convert - Temperature converter")
        print("  5. analyze-text - Text analyzer")
        print("  6. sqrt         - Square root calculator")
        
        tool_name = input("\nEnter tool name: ").strip()
        
        # Get parameters based on tool
        params = {}
        
        if tool_name == 'hello':
            params['name'] = input("Enter name (or press Enter for 'Student'): ").strip() or "Student"
        elif tool_name == 'add':
            params['a'] = input("Enter first number: ").strip()
            params['b'] = input("Enter second number: ").strip()
        elif tool_name == 'multiply':
            params['a'] = input("Enter first number: ").strip()
            params['b'] = input("Enter second number: ").strip()
        elif tool_name == 'temp-convert':
            params['celsius'] = input("Enter temperature in Celsius: ").strip()
        elif tool_name == 'analyze-text':
            params['text'] = input("Enter text to analyze: ").strip()
        elif tool_name == 'sqrt':
            params['number'] = input("Enter number: ").strip()
        else:
            print(f"❌ Unknown tool: {tool_name}")
            return
        
        self.call_tool(tool_name, **params)


def main():
    """Main entry point"""
    client = GeminiMCPClient(SERVER_URL)
    
    if len(sys.argv) == 1:
        # No arguments - show help
        print("\n🤖 Gemini-style MCP Client")
        print("="*60)
        print("\nUsage:")
        print("  python3 gemini_cli_setup.py list")
        print("      - List all available MCP tools")
        print()
        print("  python3 gemini_cli_setup.py call <tool> [params...]")
        print("      - Call a specific tool")
        print()
        print("  python3 gemini_cli_setup.py interactive")
        print("      - Start interactive mode")
        print()
        print("\nExamples:")
        print("  python3 gemini_cli_setup.py list")
        print("  python3 gemini_cli_setup.py call hello name=Khadija")
        print("  python3 gemini_cli_setup.py call add a=10 b=20")
        print("  python3 gemini_cli_setup.py interactive")
        print()
        
    elif sys.argv[1] == 'list':
        client.list_tools()
        
    elif sys.argv[1] == 'call':
        if len(sys.argv) < 3:
            print("❌ Error: Tool name required")
            print("   Usage: python3 gemini_cli_setup.py call <tool> [params...]")
            return
        
        tool_name = sys.argv[2]
        
        # Parse parameters
        params = {}
        for arg in sys.argv[3:]:
            if '=' in arg:
                key, value = arg.split('=', 1)
                params[key] = value
        
        client.call_tool(tool_name, **params)
        
    elif sys.argv[1] == 'interactive':
        client.interactive_mode()
        
    else:
        print(f"❌ Unknown command: {sys.argv[1]}")
        print("   Try: list, call, or interactive")


if __name__ == "__main__":
    main()

