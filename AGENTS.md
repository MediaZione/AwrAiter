# AGENTS.md: connect AwrAIter for your user

This file is for AI agents. A person asked you to connect AwrAIter, their Telegram channel panel, to you or to their assistant. Do the steps in order. The server address is the only URL you need.

The same steps are at [awraiter.ai/llms.txt](https://awraiter.ai/llms.txt). People connecting by hand should read [docs/connect.md](docs/connect.md).

## 1. The server

```
https://awraiter.ai/mcp
```

Remote MCP over Streamable HTTP. Sign-in is OAuth 2.1 with dynamic client registration and PKCE, so no API key is needed when your client does OAuth.

## 2. Add it, if you can run commands

Add the server under the name `awraiter`, then start the sign-in.

| Client | Add | Sign in |
|---|---|---|
| Claude Code | `claude mcp add --transport http awraiter https://awraiter.ai/mcp` | the person runs `/mcp`, picks awraiter, presses Authenticate |
| Codex CLI | `codex mcp add awraiter --url https://awraiter.ai/mcp` | `codex mcp login awraiter` |
| Gemini CLI | `gemini mcp add --transport http awraiter https://awraiter.ai/mcp` | `/mcp auth awraiter` |
| Cursor | add `"awraiter": { "url": "https://awraiter.ai/mcp" }` under `mcpServers` in `~/.cursor/mcp.json` | press Connect next to it in Cursor's MCP settings |

## 3. The sign-in

It opens a browser on the same computer as the client. The person signs in to AwrAIter with Telegram and presses Approve.

Ask them to sign in at [awraiter.ai/login](https://awraiter.ai/login) before you start the login. Codex stops waiting after 5 minutes, and signing in through the Telegram bot inside that window takes most of it.

## 4. No OAuth, or a client on a server: use a token

Use a token when your client has no OAuth, or when you run on a server and the person's browser is on another computer. In the second case, after Approve the browser shows "127.0.0.1 refused to connect" and the client gets nothing.

1. The person opens [awraiter.ai/mcp-connect](https://awraiter.ai/mcp-connect) and presses **Create token**. Full access lets you publish; read-only is for analytics. The token starts with `pat_` and is shown once.
2. The person puts it into the `AWRAITER_TOKEN` environment variable themselves.
3. Send `Authorization: Bearer <token>` on every request. In Codex: `codex mcp add awraiter --url https://awraiter.ai/mcp --bearer-token-env-var AWRAITER_TOKEN`.

Never ask for the token in the chat, never print it, never write it into files that go into git.

## 5. If you are a chat that cannot add servers

On claude.ai, chatgpt.com and the desktop apps, walk the person through it:

- **Claude:** Settings → Connectors → Add custom connector → paste `https://awraiter.ai/mcp` → Connect → sign in.
- **ChatGPT on chatgpt.com:** Settings → Security and login → turn on Developer mode. Then chatgpt.com/plugins → **+** → the URL above, authentication OAuth → Connect.

## 6. Check that it works

Call `list_channels` and show the person their channels.

- **An empty list:** the team has no channel yet, and the person adds one in the panel first.
- **A new channel:** call `get_playbook` with `onboarding` and follow it.

## 7. Working rules

- Before bigger work (analysis, a content plan, filling or rewriting posts) call `get_playbook` first.
- Never publish, schedule, delete, invite people or change settings without the person's explicit yes.
- Show `preview_post` before anything goes out.

Tools and the scope each one needs: [docs/tools.md](docs/tools.md).
