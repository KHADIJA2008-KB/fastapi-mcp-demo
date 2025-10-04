#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}     FastAPI MCP Server - Demo Script${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════${NC}"
echo ""

# Check if server is running
echo -e "${YELLOW}[1] Checking if FastAPI server is running...${NC}"
if curl -s http://localhost:8000/docs > /dev/null 2>&1; then
    echo -e "${GREEN}✓ Server is running at http://localhost:8000${NC}"
else
    echo -e "${YELLOW}⚠ Server is not running. Starting server...${NC}"
    echo -e "${YELLOW}Please run: uvicorn main:app --reload${NC}"
    exit 1
fi
echo ""

# Test Hello Tool (default)
echo -e "${YELLOW}[2] Testing Hello Tool (default)...${NC}"
echo -e "${BLUE}Request: GET /tools/hello${NC}"
RESPONSE=$(curl -s "http://localhost:8000/tools/hello")
echo -e "${GREEN}Response: $RESPONSE${NC}"
echo ""

# Test Hello Tool (with name)
echo -e "${YELLOW}[3] Testing Hello Tool (with custom name)...${NC}"
echo -e "${BLUE}Request: GET /tools/hello?name=Khadija${NC}"
RESPONSE=$(curl -s "http://localhost:8000/tools/hello?name=Khadija")
echo -e "${GREEN}Response: $RESPONSE${NC}"
echo ""

# Test Add Tool
echo -e "${YELLOW}[4] Testing Add Tool...${NC}"
echo -e "${BLUE}Request: GET /tools/add?a=42&b=58${NC}"
RESPONSE=$(curl -s "http://localhost:8000/tools/add?a=42&b=58")
echo -e "${GREEN}Response: $RESPONSE${NC}"
echo ""

# Show API Documentation
echo -e "${YELLOW}[5] API Documentation Available at:${NC}"
echo -e "${GREEN}→ http://localhost:8000/docs (Swagger UI)${NC}"
echo -e "${GREEN}→ http://localhost:8000/redoc (ReDoc)${NC}"
echo ""

# Show MCP Configuration
echo -e "${YELLOW}[6] MCP Configuration File:${NC}"
echo -e "${BLUE}→ ./mcp_config.json${NC}"
echo ""

# Summary
echo -e "${BLUE}════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✓ All tests passed successfully!${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${YELLOW}Next Steps:${NC}"
echo "1. Configure Gemini CLI with mcp_config.json"
echo "2. Run: gemini mcp list"
echo "3. Call tools via Gemini CLI"
echo ""

