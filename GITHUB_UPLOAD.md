# GitHub Upload Instructions

## Step 1: Commit Your Changes

```bash
cd /home/khadijab/fastapi-mcp-demo

# Add all files (already done)
git add .

# Create initial commit
git commit -m "Initial commit: FastAPI MCP Server with Gemini CLI integration"
```

## Step 2: Create GitHub Repository

1. Go to [GitHub](https://github.com)
2. Click the **+** icon in the top right
3. Select **New repository**
4. Repository settings:
   - **Name**: `fastapi-mcp-demo`
   - **Description**: `FastAPI MCP Server for Gemini CLI - Demonstrates Model Context Protocol integration`
   - **Visibility**: Public
   - **DO NOT** initialize with README (we already have one)
5. Click **Create repository**

## Step 3: Link Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these:

```bash
# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/fastapi-mcp-demo.git

# Rename branch to main (if you prefer main over master)
git branch -M main

# Push to GitHub
git push -u origin main
```

## Step 4: Verify Upload

Visit your repository at: `https://github.com/YOUR_USERNAME/fastapi-mcp-demo`

You should see:
- ✓ main.py
- ✓ requirements.txt
- ✓ mcp_config.json
- ✓ README.md
- ✓ GEMINI_CLI_SETUP.md
- ✓ demo_script.sh
- ✓ test_endpoints.sh
- ✓ .gitignore

## Alternative: Using SSH

If you have SSH keys set up:

```bash
# Add remote using SSH
git remote add origin git@github.com:YOUR_USERNAME/fastapi-mcp-demo.git

# Push to GitHub
git push -u origin main
```

## Quick Command Reference

```bash
# Check current status
git status

# View commit history
git log --oneline

# Add more changes later
git add .
git commit -m "Your commit message"
git push

# View remote URL
git remote -v
```

## Adding a GitHub Actions Badge (Optional)

Add this to your README.md to show build status:

```markdown
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg?style=flat&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org)
```

## Repository Topics (Recommended)

Add these topics to your repository for better discoverability:
- `fastapi`
- `mcp-server`
- `model-context-protocol`
- `gemini-cli`
- `google-ai`
- `python`
- `api`
- `rest-api`

## Making it More Professional

### Add a License
```bash
# Add MIT License (example)
echo "MIT License

Copyright (c) 2025 Khadija

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the \"Software\"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE." > LICENSE

git add LICENSE
git commit -m "Add MIT License"
git push
```

### Add a .github/workflows for CI/CD (Optional)
Create `.github/workflows/test.yml` for automated testing.

## Troubleshooting

### Authentication Error
If you get authentication errors:
```bash
# Use GitHub CLI (gh)
gh auth login

# Or use Personal Access Token
# Go to GitHub → Settings → Developer settings → Personal access tokens
# Create token with 'repo' scope
```

### Push Rejected
```bash
# If remote has changes you don't have locally
git pull origin main --rebase
git push
```

