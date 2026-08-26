# AwrAIter MCP Server

[![MCP Registry](https://img.shields.io/badge/MCP%20Registry-ai.awraiter%2Ftelegram-5A5AFF)](https://registry.modelcontextprotocol.io)
[![Transport](https://img.shields.io/badge/transport-streamable--http-1f6feb)](https://modelcontextprotocol.io)
[![Auth](https://img.shields.io/badge/auth-OAuth%202.1%20%C2%B7%20PKCE-2ea043)](#authentication)
[![Docs](https://img.shields.io/badge/docs-awraiter.ai%2Fmcp--server-8957e5)](https://awraiter.ai/mcp-server/)

A remote MCP server for the **Telegram channels you administer**: read analytics, draft posts from your own scraped sources, build content plans, schedule and publish — from inside ChatGPT, Claude, or any MCP-capable client.

**Not a userbot.** No phone number, no login code, no `.session` file. The server acts through your AwrAIter account and reaches only the channels of the team you authorize.

[Русская версия](README.ru.md) · [Connection guide](docs/connect.md) · [Tool reference](docs/tools.md) · [awraiter.ai](https://awraiter.ai)

---

## Server

| | |
|---|---|
| **URL** | `https://awraiter.ai/mcp` |
| **Transport** | Streamable HTTP |
| **Authentication** | OAuth 2.1 (PKCE, dynamic client registration) or a personal access token |
| **Registry name** | `ai.awraiter/telegram` |
| **Availability** | Every plan, including the free tier |

## Quick start

You need an AwrAIter account ([sign in with Telegram](https://awraiter.ai/login)) and at least one connected channel.

### Claude (web / desktop)

**Settings → Connectors → Add custom connector**, paste the URL, press **Connect**, and confirm access for the team you want.

```
https://awraiter.ai/mcp
```

### Claude Code

```bash
claude mcp add --transport http awraiter https://awraiter.ai/mcp
```

### ChatGPT

In the browser, **Settings → Connectors** offers OAuth — paste the URL and press **Connect**.
The ChatGPT/Codex desktop form has no OAuth option; connect it with a token instead (see below).

### Clients that take a JSON config

```json
{
  "mcpServers": {
    "awraiter": {
      "type": "http",
      "url": "https://awraiter.ai/mcp"
    }
  }
}
```

### Clients without OAuth (token auth)

Create a token in the panel under [**MCP connection**](https://awraiter.ai/mcp-connect) — it is shown once — and send it as a header:

```
Authorization: Bearer YOUR_TOKEN
```

Step-by-step instructions for Claude, Claude Code, ChatGPT, Codex, Gemini CLI and Qwen Code are in
**[docs/connect.md](docs/connect.md)**; ready-to-paste config files are in **[examples/](examples/)**.

## Tools

25 tools. The ones that change something are marked ✍️ — everything else is read-only.

| Tool | What it does |
|---|---|
| `list_teams` | Teams you belong to; marks the active one |
| `switch_team` ✍️ | Switch the active team (membership is verified server-side) |
| `list_channels` | Channels owned by the active team |
| `get_channel` | One channel's profile: name, chat id, language, description |
| `get_channel_stats` | Subscribers, reach, ER and dynamics over 1–90 days |
| `get_channel_insights` | What works for this audience, scored against the channel's own 30-day median |
| `get_recent_posts` | Most recent published posts, newest first |
| `search_channel_content` | Semantic search over the channel's own posts and source material |
| `search_sources` | Search the channel's bound sources |
| `draft_from_sources` | Freshest scraped sources not yet used in a post |
| `deep_analyze` ✍️ | Deep AI analysis of channel performance — the one tool that spends the team's AI credits |
| `check_uniqueness` | Is this draft a near-duplicate of existing posts or a copy of a source? |
| `score_post` | Data-grounded quality signal for a draft, specific to this channel |
| `preview_post` | Exact message that would be sent — title, body, media, formatting |
| `create_post_from_text` ✍️ | Save a ready-to-publish draft from text the assistant wrote |
| `schedule_post` ✍️ | Publish a draft now, or schedule it for a given time |
| `cancel_scheduled_post` ✍️ | Cancel a scheduled post by its plan id |
| `get_content_plan` | The channel's plan configuration and its slots |
| `create_content_plan` ✍️ | Create a content plan for a channel |
| `find_free_slot` | Earliest slot in the plan with no post yet |
| `get_channel_memory` | The channel's brand brief and banlist |
| `set_brand_brief` ✍️ | Replace the channel's brand/tone guidance |
| `add_banlist_entry` ✍️ | Add a forbidden word to the channel's banlist |
| `remove_banlist_entry` ✍️ | Remove a word from the banlist |
| `get_playbook` | Step-by-step operator playbook for a workflow |

What each tool returns, and the exact scope it needs, is in **[docs/tools.md](docs/tools.md)**.

## Authentication

OAuth 2.1 with PKCE and dynamic client registration; redirect URIs are restricted to HTTPS or HTTP loopback, authorization codes are single-use, and refresh tokens rotate. A token is bound to one user, one team and one scope.

Personal access tokens come in two scopes:

| Scope | Allows |
|---|---|
| `read` | Read-only tools; every ✍️ tool is refused server-side |
| `full` | Everything the account can do in the panel |

Tokens are listed, and can be revoked, in the panel under [MCP connection](https://awraiter.ai/mcp-connect).

## Security model

|  | Userbot-style Telegram MCP servers | AwrAIter |
|---|---|---|
| What you hand over | Phone number, login code, session file | An OAuth grant to your own account |
| What it can reach | Everything your account can — DMs, groups, private material | Only the channels of the team you authorized |
| How it publishes | As you | Through the panel's own service admin, with the same permission checks as the UI |
| If the token leaks | Your whole Telegram account | Revoke the token in the panel; nothing else is exposed |

Every write goes through the same channel-level access control as the panel, and rate limits apply per token.
The full model, and how to report a vulnerability, are in **[SECURITY.md](SECURITY.md)**.

## About AwrAIter

AwrAIter is a panel for people who run Telegram channels: weekly content plans, AI drafts in your channel's tone, scheduled publishing, and analytics for everything published — growth, reach, ER/ERR, per-post performance, channel comparison, export to XLSX or Google Sheets. One channel is free forever; paid plans start at €9/month. See [awraiter.ai](https://awraiter.ai).

## Support and legal

- Questions and issues: [awraiter.ai/support](https://awraiter.ai/support/)
- [Terms of Service](https://awraiter.ai/legal/terms/) · [Privacy Policy](https://awraiter.ai/legal/privacy/)
- Operated by Mediazione Italia S.r.l. Payments are handled by Stripe; we never see card numbers.
- Your channel content stays yours — we do not train models on it unless you explicitly opt in (off by default).

## License

Documentation and examples in this repository are released under the [MIT License](LICENSE). The AwrAIter service itself is proprietary.
