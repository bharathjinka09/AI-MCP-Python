# Steps to configure and run the custom MCP server in python

## Youtube Tutorial

Tech with Tim - <a href="https://youtu.be/-8k9lGpGQ6g" target="_blank">MCP Tutorial</a>

## Resources

<a href="https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file" target="_blank">MCP Resource</a>

## Tips 

1. Download Claude desktop app
2. Goto developer mode in Claude desktop and edit claude_desktop_config.json
3. Add complete path of uv like below in claude_desktop_config.json
4. {
  "mcpServers": {
    "Demo": {
      "command": "C:\\Users\\bhara\\.local\\bin\\uv.exe",
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
5. Run the command -> uv run mcp install .\main.py
6.  End Claude desktop task from task manager and open claude desktop after adding any new mcp tools
