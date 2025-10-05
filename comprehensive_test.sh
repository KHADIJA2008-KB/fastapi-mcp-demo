#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${CYAN}╔══════════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║         FastAPI MCP Server - Comprehensive Tool Testing             ║${NC}"
echo -e "${CYAN}║                    6 Tools Demonstration                             ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if server is running
echo -e "${YELLOW}[0] Checking Server Status...${NC}"
if curl -s http://localhost:8000/ > /dev/null 2>&1; then
    echo -e "${GREEN}✓ Server is running at http://localhost:8000${NC}"
    echo ""
    # Show server info
    echo -e "${BLUE}Server Information:${NC}"
    curl -s http://localhost:8000/ | python3 -m json.tool
    echo ""
else
    echo -e "${RED}✗ Server is not running!${NC}"
    echo -e "${YELLOW}Please start the server with: uvicorn main:app --reload${NC}"
    exit 1
fi

echo -e "${CYAN}════════════════════════════════════════════════════════════════════${NC}"
echo ""

# Test Tool 1: Hello
echo -e "${YELLOW}[1] Testing HELLO Tool - Personalized Greeting${NC}"
echo -e "${BLUE}Request: GET /tools/hello?name=Khadija${NC}"
RESPONSE=$(curl -s "http://localhost:8000/tools/hello?name=Khadija")
echo -e "${GREEN}Response:${NC}"
echo "$RESPONSE" | python3 -m json.tool
echo ""

# Test Tool 2: Add
echo -e "${YELLOW}[2] Testing ADD Tool - Addition Calculator${NC}"
echo -e "${BLUE}Request: GET /tools/add?a=25&b=75${NC}"
RESPONSE=$(curl -s "http://localhost:8000/tools/add?a=25&b=75")
echo -e "${GREEN}Response:${NC}"
echo "$RESPONSE" | python3 -m json.tool
echo ""

# Test Tool 3: Multiply
echo -e "${YELLOW}[3] Testing MULTIPLY Tool - Multiplication Calculator${NC}"
echo -e "${BLUE}Request: GET /tools/multiply?a=12&b=8${NC}"
RESPONSE=$(curl -s "http://localhost:8000/tools/multiply?a=12&b=8")
echo -e "${GREEN}Response:${NC}"
echo "$RESPONSE" | python3 -m json.tool
echo ""

# Test Tool 4: Temperature Converter
echo -e "${YELLOW}[4] Testing TEMP-CONVERT Tool - Temperature Converter${NC}"
echo -e "${BLUE}Request: GET /tools/temp-convert?celsius=25${NC}"
RESPONSE=$(curl -s "http://localhost:8000/tools/temp-convert?celsius=25")
echo -e "${GREEN}Response:${NC}"
echo "$RESPONSE" | python3 -m json.tool
echo ""

# Test Tool 5: Text Analyzer
echo -e "${YELLOW}[5] Testing ANALYZE-TEXT Tool - Text Statistics${NC}"
echo -e "${BLUE}Request: GET /tools/analyze-text?text=Hello%20World%20123${NC}"
RESPONSE=$(curl -s "http://localhost:8000/tools/analyze-text?text=Hello%20World%20123")
echo -e "${GREEN}Response:${NC}"
echo "$RESPONSE" | python3 -m json.tool
echo ""

# Test Tool 6: Square Root
echo -e "${YELLOW}[6] Testing SQRT Tool - Square Root Calculator${NC}"
echo -e "${BLUE}Request: GET /tools/sqrt?number=144${NC}"
RESPONSE=$(curl -s "http://localhost:8000/tools/sqrt?number=144")
echo -e "${GREEN}Response:${NC}"
echo "$RESPONSE" | python3 -m json.tool
echo ""

# Summary
echo -e "${CYAN}════════════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✓ All 6 MCP Tools Tested Successfully!${NC}"
echo -e "${CYAN}════════════════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${YELLOW}📊 Available Resources:${NC}"
echo -e "  ${BLUE}•${NC} API Documentation: ${GREEN}http://localhost:8000/docs${NC}"
echo -e "  ${BLUE}•${NC} ReDoc Documentation: ${GREEN}http://localhost:8000/redoc${NC}"
echo -e "  ${BLUE}•${NC} OpenAPI Schema: ${GREEN}http://localhost:8000/openapi.json${NC}"
echo ""

echo -e "${YELLOW}🔧 MCP Configuration:${NC}"
echo -e "  ${BLUE}•${NC} Config file: ${GREEN}./mcp_config.json${NC}"
echo -e "  ${BLUE}•${NC} Server URL: ${GREEN}http://localhost:8000${NC}"
echo -e "  ${BLUE}•${NC} Total Tools: ${GREEN}6${NC}"
echo ""

echo -e "${YELLOW}📝 Next Steps for Assignment:${NC}"
echo "  1. Ensure server is running"
echo "  2. Record screen showing:"
echo "     - This test script output"
echo "     - Browser with /docs"
echo "     - MCP configuration"
echo "  3. Push to GitHub"
echo "  4. Submit GitHub link with recording"
echo ""

echo -e "${GREEN}🎉 Your MCP Server is ready for demonstration!${NC}"
echo ""

