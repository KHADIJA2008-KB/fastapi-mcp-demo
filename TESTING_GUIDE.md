# 🧪 Step-by-Step Testing Guide for Your MCP Server

## Prerequisites Check

Before testing, make sure:
- ✅ Your server is running (you should see it in one terminal)
- ✅ You're in the project directory

---

## 🚀 STEP-BY-STEP TESTING GUIDE

### STEP 1: Open a New Terminal

```bash
# Open a new terminal window (Ctrl+Alt+T or from menu)
# Navigate to your project
cd /home/khadijab/fastapi-mcp-demo
```

### STEP 2: Check If Server Is Running

```bash
# This should return server information
curl http://localhost:8000/
```

**Expected Output:**
```json
{
  "name": "FastAPI MCP Server",
  "version": "1.0.0",
  "status": "running",
  "available_tools": [...]
}
```

✅ If you see this → Server is running!  
❌ If you see "Connection refused" → Server is not running (see Step 3)

---

### STEP 3: Start Server (If Not Running)

**Terminal 1 (Server Terminal):**
```bash
cd /home/khadijab/fastapi-mcp-demo
source venv/bin/activate
uvicorn main:app --reload
```

**Wait for:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

✅ Leave this terminal running!

---

### STEP 4: Test Each Tool Individually

**Open Terminal 2 (Testing Terminal):**

#### Test 1: Hello Tool (Greeting)
```bash
curl "http://localhost:8000/tools/hello?name=Khadija"
```

**Expected:**
```json
{
  "message": "Hello, Khadija! This is your MCP Server speaking 👋",
  "timestamp": "2025-10-04T..."
}
```

#### Test 2: Add Tool (Addition)
```bash
curl "http://localhost:8000/tools/add?a=25&b=75"
```

**Expected:**
```json
{
  "operation": "addition",
  "a": 25,
  "b": 75,
  "result": 100
}
```

#### Test 3: Multiply Tool
```bash
curl "http://localhost:8000/tools/multiply?a=12&b=8"
```

**Expected:**
```json
{
  "operation": "multiplication",
  "a": 12.0,
  "b": 8.0,
  "result": 96.0
}
```

#### Test 4: Temperature Converter
```bash
curl "http://localhost:8000/tools/temp-convert?celsius=25"
```

**Expected:**
```json
{
  "celsius": 25.0,
  "fahrenheit": 77.0,
  "kelvin": 298.15
}
```

#### Test 5: Text Analyzer
```bash
curl "http://localhost:8000/tools/analyze-text?text=Hello%20World%20123"
```

**Expected:**
```json
{
  "text": "Hello World 123",
  "character_count": 15,
  "word_count": 3,
  "uppercase_count": 2,
  "lowercase_count": 8,
  "digit_count": 3
}
```

#### Test 6: Square Root
```bash
curl "http://localhost:8000/tools/sqrt?number=144"
```

**Expected:**
```json
{
  "number": 144.0,
  "square_root": 12.0
}
```

---

### STEP 5: Test All Tools at Once (Automated)

```bash
cd /home/khadijab/fastapi-mcp-demo
./comprehensive_test.sh
```

**Expected:** Beautiful colored output showing all 6 tools working!

---

### STEP 6: View Interactive API Documentation

**Option A: Command Line**
```bash
# Get the docs URL
echo "Open this in browser: http://localhost:8000/docs"
```

**Option B: Open in Browser**
```bash
# If you have firefox
firefox http://localhost:8000/docs

# Or Chrome
google-chrome http://localhost:8000/docs

# Or just manually open browser and go to:
# http://localhost:8000/docs
```

---

### STEP 7: Check MCP Configuration

```bash
# View your MCP config
cat mcp_config.json

# Or with pretty formatting
cat mcp_config.json | python3 -m json.tool
```

---

### STEP 8: Verify All Files Are Ready

```bash
# Check all your project files
ls -lh *.py *.json *.sh *.md

# Count tools in main.py
grep -c "@app.get" main.py
# Should show: 7 (6 tools + 1 root endpoint)

# Check git status
git status
```

---

## 🎯 QUICK ONE-LINE TESTS

Copy and paste these one at a time:

```bash
# Test 1: Server status
curl -s http://localhost:8000/ | python3 -m json.tool

# Test 2: Hello tool
curl -s "http://localhost:8000/tools/hello?name=Test" | python3 -m json.tool

# Test 3: Add tool
curl -s "http://localhost:8000/tools/add?a=10&b=20" | python3 -m json.tool

# Test 4: Multiply tool
curl -s "http://localhost:8000/tools/multiply?a=5&b=7" | python3 -m json.tool

# Test 5: Temp converter
curl -s "http://localhost:8000/tools/temp-convert?celsius=100" | python3 -m json.tool

# Test 6: Text analyzer
curl -s "http://localhost:8000/tools/analyze-text?text=Testing123" | python3 -m json.tool

# Test 7: Square root
curl -s "http://localhost:8000/tools/sqrt?number=64" | python3 -m json.tool
```

---

## 🔍 TROUBLESHOOTING

### Problem: "Connection refused"
**Solution:**
```bash
# Check if server is running
ps aux | grep uvicorn

# If not running, start it:
cd /home/khadijab/fastapi-mcp-demo
source venv/bin/activate
uvicorn main:app --reload
```

### Problem: "Command not found: curl"
**Solution:**
```bash
sudo apt install curl
```

### Problem: Port 8000 already in use
**Solution:**
```bash
# Find and kill the process
kill $(lsof -t -i:8000)

# Then restart server
uvicorn main:app --reload
```

### Problem: Server starts but tools don't work
**Solution:**
```bash
# Check the server logs in Terminal 1
# Look for error messages
# Make sure you see: "Application startup complete"
```

---

## 📊 COMPLETE TEST SEQUENCE

Run all these commands in order:

```bash
# 1. Navigate to project
cd /home/khadijab/fastapi-mcp-demo

# 2. Check server status
curl http://localhost:8000/

# 3. Run comprehensive test
./comprehensive_test.sh

# 4. Check logs (in server terminal)
# Look for 200 OK responses

# 5. View docs
firefox http://localhost:8000/docs
```

---

## ✅ SUCCESS CHECKLIST

After testing, verify:

- [ ] Server responds at http://localhost:8000/
- [ ] All 6 tools return JSON responses
- [ ] No error messages in server logs
- [ ] comprehensive_test.sh runs successfully
- [ ] API docs accessible at /docs
- [ ] All responses have correct format

---

## 🎬 WHAT TO RECORD FOR ASSIGNMENT

**Terminal 1 (visible):**
```bash
cd /home/khadijab/fastapi-mcp-demo
source venv/bin/activate
uvicorn main:app --reload
# Keep this running and visible
```

**Terminal 2 (visible):**
```bash
cd /home/khadijab/fastapi-mcp-demo
./comprehensive_test.sh
# Run this and show the output
```

**Browser (visible):**
```
http://localhost:8000/docs
# Show the interactive documentation
```

---

## 💡 PRO TIPS

1. **Pretty JSON Output:**
   ```bash
   curl -s http://localhost:8000/tools/hello | python3 -m json.tool
   ```

2. **Watch Server Logs:**
   - Keep Terminal 1 visible to see real-time requests
   - Look for "200 OK" status codes

3. **Test with Different Values:**
   ```bash
   curl "http://localhost:8000/tools/add?a=100&b=200"
   curl "http://localhost:8000/tools/temp-convert?celsius=0"
   curl "http://localhost:8000/tools/analyze-text?text=Your%20Name%20Here"
   ```

4. **Copy Server Logs:**
   - The logs show proof your server is working
   - Good to include in screenshots

---

## 🚀 READY FOR RECORDING

Once all tests pass:

1. ✅ Keep Terminal 1 (server) visible
2. ✅ Run comprehensive_test.sh in Terminal 2
3. ✅ Open browser to /docs
4. ✅ Start recording!

**You're all set!** 🎉

