#!/usr/bin/env python3
"""
Interactive MCP Tool Tester
Allows you to test all MCP tools with interactive prompts
"""

import requests
import json
from datetime import datetime

# Colors for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

SERVER_URL = "http://localhost:8000"

def print_header():
    """Print the welcome header"""
    print(f"\n{Colors.CYAN}{'='*70}")
    print(f"  🚀 FastAPI MCP Server - Interactive Tool Tester")
    print(f"{'='*70}{Colors.END}\n")

def print_menu():
    """Print the tool selection menu"""
    print(f"{Colors.YELLOW}Available MCP Tools:{Colors.END}")
    print(f"  {Colors.BOLD}1.{Colors.END} Hello Tool - Personalized greeting")
    print(f"  {Colors.BOLD}2.{Colors.END} Add Tool - Addition calculator")
    print(f"  {Colors.BOLD}3.{Colors.END} Multiply Tool - Multiplication calculator")
    print(f"  {Colors.BOLD}4.{Colors.END} Temperature Converter - Celsius to Fahrenheit & Kelvin")
    print(f"  {Colors.BOLD}5.{Colors.END} Text Analyzer - Analyze text statistics")
    print(f"  {Colors.BOLD}6.{Colors.END} Square Root - Calculate square root")
    print(f"  {Colors.BOLD}0.{Colors.END} Exit\n")

def check_server():
    """Check if the server is running"""
    try:
        response = requests.get(f"{SERVER_URL}/", timeout=2)
        if response.status_code == 200:
            print(f"{Colors.GREEN}✓ Server is running at {SERVER_URL}{Colors.END}\n")
            return True
    except requests.exceptions.RequestException:
        print(f"{Colors.RED}✗ Server is not running!{Colors.END}")
        print(f"{Colors.YELLOW}Please start the server with:{Colors.END}")
        print(f"  cd /home/khadijab/fastapi-mcp-demo")
        print(f"  source venv/bin/activate")
        print(f"  uvicorn main:app --reload\n")
        return False

def display_response(response_data, tool_name):
    """Display the tool response in a formatted way"""
    print(f"\n{Colors.CYAN}{'─'*70}{Colors.END}")
    print(f"{Colors.GREEN}✓ {tool_name} - Response:{Colors.END}")
    print(f"{Colors.CYAN}{'─'*70}{Colors.END}")
    print(json.dumps(response_data, indent=2))
    print(f"{Colors.CYAN}{'─'*70}{Colors.END}\n")

def tool_hello():
    """Hello Tool - Interactive"""
    print(f"\n{Colors.BLUE}🔹 Hello Tool - Personalized Greeting{Colors.END}")
    print(f"{Colors.YELLOW}This tool creates a personalized greeting message.{Colors.END}\n")
    
    name = input(f"{Colors.BOLD}Enter your name (or press Enter for 'Student'): {Colors.END}").strip()
    if not name:
        name = "Student"
    
    print(f"\n{Colors.CYAN}Calling tool with name: {name}{Colors.END}")
    
    try:
        response = requests.get(f"{SERVER_URL}/tools/hello", params={"name": name})
        if response.status_code == 200:
            display_response(response.json(), "Hello Tool")
        else:
            print(f"{Colors.RED}Error: {response.status_code}{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.END}")

def tool_add():
    """Add Tool - Interactive"""
    print(f"\n{Colors.BLUE}🔹 Add Tool - Addition Calculator{Colors.END}")
    print(f"{Colors.YELLOW}This tool adds two numbers together.{Colors.END}\n")
    
    while True:
        try:
            a = int(input(f"{Colors.BOLD}Enter first number: {Colors.END}"))
            b = int(input(f"{Colors.BOLD}Enter second number: {Colors.END}"))
            break
        except ValueError:
            print(f"{Colors.RED}Please enter valid integers!{Colors.END}\n")
    
    print(f"\n{Colors.CYAN}Calculating: {a} + {b}{Colors.END}")
    
    try:
        response = requests.get(f"{SERVER_URL}/tools/add", params={"a": a, "b": b})
        if response.status_code == 200:
            display_response(response.json(), "Add Tool")
        else:
            print(f"{Colors.RED}Error: {response.status_code}{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.END}")

def tool_multiply():
    """Multiply Tool - Interactive"""
    print(f"\n{Colors.BLUE}🔹 Multiply Tool - Multiplication Calculator{Colors.END}")
    print(f"{Colors.YELLOW}This tool multiplies two numbers.{Colors.END}\n")
    
    while True:
        try:
            a = float(input(f"{Colors.BOLD}Enter first number: {Colors.END}"))
            b = float(input(f"{Colors.BOLD}Enter second number: {Colors.END}"))
            break
        except ValueError:
            print(f"{Colors.RED}Please enter valid numbers!{Colors.END}\n")
    
    print(f"\n{Colors.CYAN}Calculating: {a} × {b}{Colors.END}")
    
    try:
        response = requests.get(f"{SERVER_URL}/tools/multiply", params={"a": a, "b": b})
        if response.status_code == 200:
            display_response(response.json(), "Multiply Tool")
        else:
            print(f"{Colors.RED}Error: {response.status_code}{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.END}")

def tool_temp_convert():
    """Temperature Converter - Interactive"""
    print(f"\n{Colors.BLUE}🔹 Temperature Converter{Colors.END}")
    print(f"{Colors.YELLOW}Converts Celsius to Fahrenheit and Kelvin.{Colors.END}\n")
    
    while True:
        try:
            celsius = float(input(f"{Colors.BOLD}Enter temperature in Celsius: {Colors.END}"))
            break
        except ValueError:
            print(f"{Colors.RED}Please enter a valid number!{Colors.END}\n")
    
    print(f"\n{Colors.CYAN}Converting {celsius}°C to Fahrenheit and Kelvin...{Colors.END}")
    
    try:
        response = requests.get(f"{SERVER_URL}/tools/temp-convert", params={"celsius": celsius})
        if response.status_code == 200:
            display_response(response.json(), "Temperature Converter")
        else:
            print(f"{Colors.RED}Error: {response.status_code}{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.END}")

def tool_analyze_text():
    """Text Analyzer - Interactive"""
    print(f"\n{Colors.BLUE}🔹 Text Analyzer{Colors.END}")
    print(f"{Colors.YELLOW}Analyzes text and returns statistics.{Colors.END}\n")
    
    text = input(f"{Colors.BOLD}Enter text to analyze: {Colors.END}").strip()
    
    if not text:
        print(f"{Colors.RED}Text cannot be empty!{Colors.END}")
        return
    
    print(f"\n{Colors.CYAN}Analyzing: \"{text}\"{Colors.END}")
    
    try:
        response = requests.get(f"{SERVER_URL}/tools/analyze-text", params={"text": text})
        if response.status_code == 200:
            display_response(response.json(), "Text Analyzer")
        else:
            print(f"{Colors.RED}Error: {response.status_code}{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.END}")

def tool_sqrt():
    """Square Root - Interactive"""
    print(f"\n{Colors.BLUE}🔹 Square Root Calculator{Colors.END}")
    print(f"{Colors.YELLOW}Calculates the square root of a number.{Colors.END}\n")
    
    while True:
        try:
            number = float(input(f"{Colors.BOLD}Enter a number: {Colors.END}"))
            if number < 0:
                print(f"{Colors.RED}Cannot calculate square root of negative number!{Colors.END}\n")
                continue
            break
        except ValueError:
            print(f"{Colors.RED}Please enter a valid number!{Colors.END}\n")
    
    print(f"\n{Colors.CYAN}Calculating √{number}...{Colors.END}")
    
    try:
        response = requests.get(f"{SERVER_URL}/tools/sqrt", params={"number": number})
        if response.status_code == 200:
            display_response(response.json(), "Square Root")
        else:
            print(f"{Colors.RED}Error: {response.status_code}{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.END}")

def main():
    """Main interactive loop"""
    print_header()
    
    # Check if server is running
    if not check_server():
        return
    
    while True:
        print_menu()
        choice = input(f"{Colors.BOLD}Select a tool (0-6): {Colors.END}").strip()
        
        if choice == "0":
            print(f"\n{Colors.GREEN}Thank you for using the MCP Tool Tester! 👋{Colors.END}\n")
            break
        elif choice == "1":
            tool_hello()
        elif choice == "2":
            tool_add()
        elif choice == "3":
            tool_multiply()
        elif choice == "4":
            tool_temp_convert()
        elif choice == "5":
            tool_analyze_text()
        elif choice == "6":
            tool_sqrt()
        else:
            print(f"{Colors.RED}Invalid choice! Please select 0-6.{Colors.END}\n")
        
        # Ask if user wants to continue
        print(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        input()
        print("\n" * 2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Interrupted by user. Goodbye! 👋{Colors.END}\n")
    except Exception as e:
        print(f"\n{Colors.RED}Unexpected error: {e}{Colors.END}\n")

