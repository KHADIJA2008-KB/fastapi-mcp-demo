# Screen Recording Guide 🎥

This guide will help you create an impressive demo video showcasing your FastAPI MCP Server.

## Recording Tools

### Linux Options
- **SimpleScreenRecorder**: `sudo apt install simplescreenrecorder`
- **OBS Studio**: `sudo apt install obs-studio`
- **Kazam**: `sudo apt install kazam`
- **FFmpeg (command line)**: `ffmpeg -f x11grab -s 1920x1080 -i :0.0 output.mp4`

### Recommended: OBS Studio
- Professional quality
- Easy to use
- Can add overlays and annotations

## Recording Checklist

### Before Recording
- [ ] Clean up your desktop/background
- [ ] Close unnecessary applications
- [ ] Increase terminal font size (for visibility)
- [ ] Prepare a script/outline
- [ ] Test all commands beforehand
- [ ] Have a browser window ready for API docs

### Demo Script (5-7 minutes)

#### 1. Introduction (30 seconds)
```
"Hello! Today I'll demonstrate a FastAPI MCP Server that integrates with Gemini CLI 
using the Model Context Protocol."
```

#### 2. Show Project Structure (30 seconds)
```bash
cd /home/khadijab/fastapi-mcp-demo
tree -L 2 -I 'venv' || ls -la
cat main.py
```

**Narration**: 
"Here's our project. We have a FastAPI application with two MCP tools: 
a greeting tool and an addition tool."

#### 3. Show Configuration (30 seconds)
```bash
cat mcp_config.json
```

**Narration**: 
"This is our MCP configuration that connects our FastAPI server to Gemini CLI."

#### 4. Start the Server (1 minute)
```bash
# Terminal 1
source venv/bin/activate
uvicorn main:app --reload
```

**Narration**: 
"Let's start the FastAPI server with auto-reload enabled."

**Wait for**: `Uvicorn running on http://127.0.0.1:8000`

#### 5. Show API Documentation (1 minute)
- Open browser to `http://localhost:8000/docs`
- Show the two endpoints
- Click on each to expand them
- Show the Try it out feature

**Narration**: 
"FastAPI automatically generates interactive API documentation. 
Here are our two MCP tools: hello and add."

#### 6. Test Tools via cURL (2 minutes)
```bash
# Terminal 2
echo "Testing Hello Tool..."
curl "http://localhost:8000/tools/hello?name=Khadija"
echo ""

echo "Testing with default name..."
curl "http://localhost:8000/tools/hello"
echo ""

echo "Testing Add Tool..."
curl "http://localhost:8000/tools/add?a=42&b=58"
echo ""
```

**Narration**: 
"Let's test our tools. The hello tool returns a personalized greeting, 
and the add tool performs mathematical operations."

#### 7. Run Demo Script (1 minute)
```bash
./demo_script.sh
```

**Narration**: 
"I've created a demo script that tests all endpoints and shows their responses."

#### 8. Show Gemini CLI Integration (1 minute)
```bash
# If you have Gemini CLI installed
cat GEMINI_CLI_SETUP.md
```

**Narration**: 
"Here's how to connect this server to Gemini CLI. The MCP configuration 
allows Gemini to discover and use our tools."

#### 9. Show GitHub Repository (30 seconds)
```bash
git status
git log --oneline
```

**Narration**: 
"The project is version-controlled with Git and ready for GitHub upload."

#### 10. Conclusion (30 seconds)
```
"That's it! We've created a FastAPI MCP Server with:
- Two working tools
- Interactive API documentation
- MCP configuration for Gemini CLI
- Complete documentation and tests
Thank you for watching!"
```

## Terminal Appearance Tips

### Make it look professional
```bash
# Increase font size
# In GNOME Terminal: View → Zoom In (Ctrl++)

# Use a nice color scheme
# Preferences → Colors → Built-in schemes: Solarized Dark

# Show clear prompt
export PS1="\[\e[32m\]\u@\h:\[\e[34m\]\w\[\e[0m\]$ "
```

## Recording Settings

### Resolution
- **1920x1080** (Full HD) - Recommended
- **1280x720** (HD) - Good for smaller files

### Frame Rate
- **30 FPS** - Smooth, good quality
- **60 FPS** - Very smooth (larger file size)

### Audio
- Use a good microphone
- Record in a quiet environment
- Speak clearly and at a moderate pace
- Pause between sections

## Post-Recording

### Editing (Optional)
- **Kdenlive**: Free video editor for Linux
- **OpenShot**: Simple and easy to use
- **DaVinci Resolve**: Professional (free version available)

### What to Edit
- Cut out mistakes or long pauses
- Add title slide with project name
- Add text overlays for commands
- Add smooth transitions between sections

### Export Settings
- Format: **MP4** (H.264)
- Quality: **High** (for YouTube)
- Resolution: Same as recording

## Upload to YouTube/Vimeo

### Title
"FastAPI MCP Server - Gemini CLI Integration Demo"

### Description
```
Demonstration of a FastAPI application acting as a Model Context Protocol (MCP) 
Server that integrates with Google's Gemini CLI.

🔗 GitHub Repository: https://github.com/YOUR_USERNAME/fastapi-mcp-demo

Features demonstrated:
✅ FastAPI server with RESTful endpoints
✅ MCP tool configuration
✅ Interactive API documentation
✅ Gemini CLI integration
✅ Automated testing scripts

Technologies used:
- Python 3.12
- FastAPI
- Uvicorn
- Model Context Protocol (MCP)
- Google Gemini CLI

⏱️ Timestamps:
0:00 - Introduction
0:30 - Project Overview
1:00 - Configuration
2:00 - Running the Server
3:00 - Testing Tools
5:00 - Gemini CLI Integration
6:00 - Conclusion
```

### Tags
`fastapi`, `python`, `mcp`, `gemini`, `ai`, `api`, `rest`, `tutorial`, `demo`, `google-ai`

## Quick Recording Commands

### Start Recording with SimpleScreenRecorder
```bash
simplescreenrecorder
# Configure: Full screen, 30 FPS, Cursor: Always visible
```

### Start Recording with FFmpeg
```bash
ffmpeg -f x11grab -s 1920x1080 -r 30 -i :0.0 \
       -f pulse -ac 2 -i default \
       -vcodec libx264 -preset ultrafast \
       -acodec aac demo_recording.mp4
```

## Final Tips

✅ **Practice first** - Do a dry run without recording
✅ **Have notes** - Keep the script visible
✅ **Show confidence** - Speak clearly and enthusiastically
✅ **Highlight key points** - Emphasize important features
✅ **Keep it concise** - 5-7 minutes is perfect
✅ **Test everything** - Ensure all commands work before recording
✅ **Good lighting** - If showing yourself

## Ready to Record?

Run this checklist:
```bash
cd /home/khadijab/fastapi-mcp-demo
./demo_script.sh  # Verify everything works
# If all tests pass, you're ready to record! 🎬
```

Good luck with your recording! 🚀

