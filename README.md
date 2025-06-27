# Steps to configure and run the custom MCP server in python

## Youtube Tutorial

Tech with Tim - <a href="https://youtu.be/-8k9lGpGQ6g" target="_blank">MCP Tutorial</a>

## Resources

<a href="https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file" target="_blank">MCP Resource</a>

## Tips 

1. Install uv and the dependency packages
2. uv add "mcp[cli]"
3. Download Claude desktop app
4. Goto developer mode in Claude desktop and edit claude_desktop_config.json
5. Add complete path of uv like below in claude_desktop_config.json
6. {
  "mcpServers": {
    "Calculator Server": {
      "command": "C:\\Users\\bhara\\.local\\bin\\uv.exe",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "C:\\Users\\bhara\\Downloads\\mcp-server-demo\\calculator.py"
      ]
    },
    "AI Add Note Server": {
      "command": "C:\\Users\\bhara\\.local\\bin\\uv.EXE",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "C:\\Users\\bhara\\Downloads\\mcp-server-demo\\main.py"
      ]
    }
  }
}
7. Run the command -> <b>uv run mcp install .\calculator.py</b> <br>
                      <b>uv run mcp install .\main.py</b>
8. End Claude desktop task from task manager and open claude desktop after adding any new mcp tools
