#!/bin/bash

echo "Testing FastAPI MCP Server Endpoints"
echo "====================================="
echo ""

echo "1. Testing Hello Tool (default):"
curl -s "http://localhost:8000/tools/hello" | jq .
echo ""

echo "2. Testing Hello Tool (with name):"
curl -s "http://localhost:8000/tools/hello?name=Khadija" | jq .
echo ""

echo "3. Testing Add Tool:"
curl -s "http://localhost:8000/tools/add?a=10&b=25" | jq .
echo ""

echo "4. Opening API Documentation:"
echo "Visit: http://localhost:8000/docs"

