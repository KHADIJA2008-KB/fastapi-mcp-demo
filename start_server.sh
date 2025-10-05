#!/bin/bash

# FastAPI MCP Server Startup Script
# This script safely starts your MCP server

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  FastAPI MCP Server - Safe Startup Script${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════${NC}"
echo ""

# Check if already in project directory
if [ ! -f "main.py" ]; then
    echo -e "${YELLOW}Navigating to project directory...${NC}"
    cd /home/khadijab/fastapi-mcp-demo || exit 1
fi

echo -e "${YELLOW}[1] Checking for processes on port 8000...${NC}"
if lsof -ti:8000 > /dev/null 2>&1; then
    echo -e "${RED}⚠️  Port 8000 is in use. Killing old processes...${NC}"
    kill -9 $(lsof -ti:8000) 2>/dev/null
    sleep 1
    echo -e "${GREEN}✓ Port 8000 is now free!${NC}"
else
    echo -e "${GREEN}✓ Port 8000 is free!${NC}"
fi
echo ""

echo -e "${YELLOW}[2] Activating virtual environment...${NC}"
if [ -d "venv" ]; then
    source venv/bin/activate
    echo -e "${GREEN}✓ Virtual environment activated!${NC}"
else
    echo -e "${RED}✗ Virtual environment not found!${NC}"
    echo -e "${YELLOW}Creating virtual environment...${NC}"
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
fi
echo ""

echo -e "${YELLOW}[3] Starting FastAPI MCP Server...${NC}"
echo -e "${BLUE}Server will start at: http://localhost:8000${NC}"
echo -e "${BLUE}API Documentation: http://localhost:8000/docs${NC}"
echo ""
echo -e "${GREEN}Press Ctrl+C to stop the server${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════${NC}"
echo ""

# Start the server
uvicorn main:app --reload

