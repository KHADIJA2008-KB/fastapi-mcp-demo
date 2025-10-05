# ⚡ Quick Start Guide - Testing Your MCP Server

## 🎮 METHOD 1: Interactive Testing (RECOMMENDED!)

**This is what you wanted - it prompts you for inputs!**

### Step 1: Start Server
```bash
# Terminal 1
cd /home/khadijab/fastapi-mcp-demo
source venv/bin/activate
uvicorn main:app --reload
```

### Step 2: Run Interactive Tester
```bash
# Terminal 2
cd /home/khadijab/fastapi-mcp-demo
python3 interactive_test.py
```

### Step 3: Follow the Prompts!
```
Select a tool (0-6): 1        ← Type 1 for Hello tool
Enter your name: Khadija      ← Type your name
✓ Response shows greeting!
```

**That's it!** No complex commands needed! ✅

---

## 💻 METHOD 2: Command Line (curl)

If you prefer one-liners:

```bash
# Test all 6 tools at once
./comprehensive_test.sh

# Or test individual tools
curl "http://localhost:8000/tools/hello?name=YourName"
curl "http://localhost:8000/tools/add?a=10&b=20"
```

---

## 🌐 METHOD 3: Browser (Visual)

```bash
# Open in browser
firefox http://localhost:8000/docs

# Or
google-chrome http://localhost:8000/docs
```

Click "Try it out" on any tool to test interactively in browser!

---

## 🎯 For Your Demo Video

### Recommended Setup:

**Terminal 1 (Server):**
```bash
cd /home/khadijab/fastapi-mcp-demo
source venv/bin/activate
uvicorn main:app --reload
```

**Terminal 2 (Interactive Tool):**
```bash
python3 interactive_test.py
```

**Browser Tab:**
```
http://localhost:8000/docs
```

### Demo Flow (60 seconds):
1. Show server running (5s)
2. Run interactive tool (30s)
   - Test Hello: type your name
   - Test Add: type 50+50
   - Test Temp: type 25°C
3. Show browser /docs (15s)
4. Show MCP config (10s)

---

## 🔥 Why Interactive Tool is Better

| Feature | curl commands | Interactive Tool |
|---------|--------------|------------------|
| Easy to use | ❌ Complex | ✅ Very easy |
| Prompts for input | ❌ No | ✅ Yes! |
| Error handling | ❌ Manual | ✅ Built-in |
| Visual appeal | ⚠️ Basic | ✅ Colorful |
| Perfect for demo | ⚠️ OK | ✅ Excellent |

---

## 📋 Quick Commands Reference

```bash
# Interactive testing (EASIEST)
python3 interactive_test.py

# Test all tools (automated)
./comprehensive_test.sh

# Test one tool (manual)
curl "http://localhost:8000/tools/hello?name=Test"

# Open API docs
firefox http://localhost:8000/docs

# Check server status
curl http://localhost:8000/

# View MCP config
cat mcp_config.json

# Check git status
git status
```

---

## ✅ What You Have Now

1. ✅ **6 MCP Tools** - all working
2. ✅ **Interactive Tester** - prompts for inputs (NEW!)
3. ✅ **Automated Tests** - comprehensive_test.sh
4. ✅ **API Docs** - at /docs
5. ✅ **MCP Config** - mcp_config.json
6. ✅ **Complete Documentation** - 10+ guides

---

## 🚀 Ready to Submit!

Your project now has THREE ways to test:
1. 🎮 **Interactive** - Type inputs when prompted (best for demo!)
2. 🤖 **Automated** - Run script to test all
3. 🌐 **Browser** - Visual interface

**You have everything you need for an impressive assignment submission!** 🎉

---

## 🎬 Recording Tip

**Use the interactive tool in your video!**

It shows:
- Professional interface ✅
- User interaction ✅
- Real-time input/output ✅
- Clean, colorful display ✅

Much better than showing curl commands!

---

## 💡 Pro Tip

You can run the interactive tool while recording and say:

> "Let me demonstrate my MCP tools using this interactive interface.  
> I'll select the Hello tool... enter my name... and you can see  
> it returns a personalized greeting with a timestamp. Very user-friendly!"

This sounds much more professional than:
> "Let me type this long curl command..."

---

**Try it now:**
```bash
python3 interactive_test.py
```

