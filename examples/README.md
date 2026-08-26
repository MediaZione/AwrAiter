# Client configuration examples

Ready-to-paste configuration for MCP clients that take a JSON file. The server URL is the
same everywhere:

```
https://awraiter.ai/mcp
```

Clients that support OAuth (Claude web/desktop, Claude Code, ChatGPT in the browser) need no
token — they sign you in on first use. Clients without OAuth take a personal access token
from [awraiter.ai/mcp-connect](https://awraiter.ai/mcp-connect); replace `YOUR_TOKEN` below,
keep the word `Bearer` and the space after it.

| File | Client |
|---|---|
| [`claude-desktop.json`](claude-desktop.json) | Claude Desktop |
| [`vscode-mcp.json`](vscode-mcp.json) | VS Code and other clients using the standard `mcpServers` shape |
| [`gemini-cli.json`](gemini-cli.json) | Gemini CLI (`~/.gemini/settings.json`) |
| [`claude-code.sh`](claude-code.sh) | Claude Code, both OAuth and token variants |

Step-by-step instructions per client are in [../docs/connect.md](../docs/connect.md).
