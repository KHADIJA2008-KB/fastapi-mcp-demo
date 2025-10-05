# 🎮 Interactive Testing Guide

## What is This?

The **interactive_test.py** script allows you to test all your MCP tools by **typing inputs directly** in the terminal, just like a real application!

Instead of writing long curl commands, you just:
1. Select which tool to use
2. Type the values when prompted
3. See the results instantly!

---

## 🚀 How to Use

### Step 1: Make sure your server is running

**Terminal 1 (Server):**
```bash
cd /home/khadijab/fastapi-mcp-demo
source venv/bin/activate
uvicorn main:app --reload
```

Keep this running!

### Step 2: Run the Interactive Tester

**Terminal 2 (Interactive Tester):**
```bash
cd /home/khadijab/fastapi-mcp-demo
python3 interactive_test.py
```

### Step 3: Follow the Prompts!

You'll see a menu:
```
Available MCP Tools:
  1. Hello Tool - Personalized greeting
  2. Add Tool - Addition calculator
  3. Multiply Tool - Multiplication calculator
  4. Temperature Converter - Celsius to Fahrenheit & Kelvin
  5. Text Analyzer - Analyze text statistics
  6. Square Root - Calculate square root
  0. Exit

Select a tool (0-6):
```

Just type the number and press Enter!

---

## 📝 Example Usage

### Example 1: Hello Tool
```
Select a tool (0-6): 1

🔹 Hello Tool - Personalized Greeting
This tool creates a personalized greeting message.

Enter your name (or press Enter for 'Student'): Khadija

Calling tool with name: Khadija

✓ Hello Tool - Response:
{
  "message": "Hello, Khadija! This is your MCP Server speaking 👋",
  "timestamp": "2025-10-04T..."
}
```

### Example 2: Add Tool
```
Select a tool (0-6): 2

🔹 Add Tool - Addition Calculator
This tool adds two numbers together.

Enter first number: 25
Enter second number: 75

Calculating: 25 + 75

✓ Add Tool - Response:
{
  "operation": "addition",
  "a": 25,
  "b": 75,
  "result": 100
}
```

### Example 3: Temperature Converter
```
Select a tool (0-6): 4

🔹 Temperature Converter
Converts Celsius to Fahrenheit and Kelvin.

Enter temperature in Celsius: 25

Converting 25.0°C to Fahrenheit and Kelvin...

✓ Temperature Converter - Response:
{
  "celsius": 25.0,
  "fahrenheit": 77.0,
  "kelvin": 298.15
}
```

### Example 4: Text Analyzer
```
Select a tool (0-6): 5

🔹 Text Analyzer
Analyzes text and returns statistics.

Enter text to analyze: Hello World 123

Analyzing: "Hello World 123"

✓ Text Analyzer - Response:
{
  "text": "Hello World 123",
  "character_count": 15,
  "word_count": 3,
  "uppercase_count": 2,
  "lowercase_count": 8,
  "digit_count": 3
}
```

---

## 🎯 Features

✅ **User-Friendly** - No need to remember curl commands
✅ **Interactive Prompts** - Asks you for each input
✅ **Colored Output** - Easy to read results
✅ **Error Handling** - Validates your inputs
✅ **Menu-Driven** - Simple number selection
✅ **Repeat Testing** - Test multiple tools without restarting
✅ **Server Check** - Verifies server is running first

---

## 🎬 Perfect for Screen Recording!

This interactive tool is **PERFECT** for your assignment demo because:
- ✅ Shows professional, user-friendly interface
- ✅ Easy to demonstrate each tool
- ✅ Clear input/output flow
- ✅ Looks impressive on video
- ✅ No complex commands to type

---

## 💡 Tips for Your Demo

1. **Keep both terminals visible** (server + interactive tool)
2. **Test 3-4 different tools** to show variety
3. **Use interesting values**:
   - Your name for Hello
   - Easy numbers for math (like 25+75=100)
   - Common temp like 25°C or 100°C
   - Your name or sentence for text analyzer
   - Perfect squares for sqrt (16, 64, 144)

4. **Narrate as you go**:
   > "Let me select the Hello tool... I'll enter my name... 
   > And here's the response with a personalized greeting and timestamp!"

---

## 🆚 Comparison: Old Way vs New Way

### Old Way (curl):
```bash
curl "http://localhost:8000/tools/add?a=25&b=75"
# Hard to remember, not interactive
```

### New Way (interactive):
```
Select a tool (0-6): 2
Enter first number: 25
Enter second number: 75
# Much easier and more impressive!
```

---

## 🔧 Quick Commands

```bash
# Run the interactive tester
python3 interactive_test.py

# Or make it easier
alias test-mcp="cd /home/khadijab/fastapi-mcp-demo && python3 interactive_test.py"

# Then just run:
test-mcp
```

---

## 🎮 What Each Tool Asks For

| Tool | Inputs Required | Example |
|------|----------------|---------|
| Hello | Name (optional) | "Khadija" or press Enter |
| Add | Two integers | 25, 75 |
| Multiply | Two numbers | 12.5, 8 |
| Temp Convert | Celsius temperature | 25 |
| Text Analyzer | Any text | "Hello World" |
| Square Root | Positive number | 144 |

---

## ✅ Success Indicators

You'll know it's working when:
- ✅ Menu appears with 6 tools
- ✅ Server status shows green checkmark
- ✅ Each tool prompts for inputs
- ✅ Results display in formatted JSON
- ✅ Can test multiple tools in one session

---

## 🆘 Troubleshooting

### "Server is not running!"
**Solution:**
```bash
# In another terminal:
cd /home/khadijab/fastapi-mcp-demo
source venv/bin/activate
uvicorn main:app --reload
```

### "ModuleNotFoundError: requests"
**Solution:**
```bash
pip install requests
# It should already be installed, but just in case
```

### Script won't run
**Solution:**
```bash
# Make sure it's executable
chmod +x interactive_test.py

# Run with python3
python3 interactive_test.py
```

---

## 🎯 For Your Assignment Recording

### Recommended Demo Flow:

1. **Show the menu** (2 seconds)
2. **Test Hello Tool** with your name (10 seconds)
3. **Test Add Tool** with 50+50=100 (10 seconds)
4. **Test Temp Converter** with 100°C (10 seconds)
5. **Test Text Analyzer** with "MCP Server Demo" (10 seconds)
6. **Exit gracefully** (2 seconds)

**Total time: ~45 seconds** - Perfect for a demo!

---

## 🌟 Why This Is Better

**Before (manual curl):**
- Hard to type
- Easy to make mistakes
- Not user-friendly
- Boring to watch

**After (interactive):**
- Easy to use
- Professional appearance
- User-friendly interface
- Impressive to watch
- Shows programming skills

---

## 🚀 You're Ready!

This interactive tool makes your MCP server look **professional and polished**. 

Use it in your screen recording to show how easy it is to use your MCP tools!

**Command to run:**
```bash
python3 interactive_test.py
```

**Enjoy testing your tools interactively!** 🎉

