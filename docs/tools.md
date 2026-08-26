# Tool reference

All 25 tools the AwrAIter MCP server exposes, and the scope each one needs.

[Русская версия](tools.ru.md) · [Connection guide](connect.md) · [← back to the README](../README.md)

## Scopes

A connection is either an OAuth grant (full rights of the account that authorized it) or a
[personal access token](https://awraiter.ai/mcp-connect) with one of two scopes:

| Scope | What it can do |
|---|---|
| `read` | Read-only tools only. Write tools are **not listed** to the client and are refused server-side if called anyway. |
| `full` | Everything the account can do in the panel. |

Every call is additionally bound to one team and to the channels that team may touch — a
token cannot reach a channel its owner cannot reach in the panel.

## Teams and channels

| Tool | Scope | What it does |
|---|---|---|
| `list_teams` | `read` | Teams you belong to; marks the active one. |
| `switch_team` | `full` | Switches the active team. Membership is verified server-side, so this cannot be used to reach a team you are not in. |
| `list_channels` | `read` | Channels of the active team. |
| `get_channel` | `read` | One channel's profile: name, chat id, language, description. |

## Analytics

| Tool | Scope | What it does |
|---|---|---|
| `get_channel_stats` | `read` | Subscribers, reach, ER/ERR and their dynamics over 1–90 days. |
| `get_channel_insights` | `read` | What works for this audience: top and flop posts scored against the channel's own 30-day median, plus statistically-backed patterns (best weekday, posting window, length, question-at-the-end) once the channel has 20 or more scored posts. |
| `get_recent_posts` | `read` | Most recent published posts, newest first. |
| `search_channel_content` | `read` | Semantic search across the channel's own posts and source material. |
| `deep_analyze` | `full` | Deep AI analysis of one channel, or a comparison across several. Runs a frontier model on our servers and **spends the team's AI credits** — which is why it needs `full`. Every other tool here is free. |

## Sources and drafting

| Tool | Scope | What it does |
|---|---|---|
| `search_sources` | `read` | Searches the sources bound to the channel. |
| `draft_from_sources` | `read` | The freshest scraped sources that have not been used in a post yet — raw material to write from. |
| `check_uniqueness` | `read` | Checks a draft for near-duplicates against the team's own posts and sources. |
| `score_post` | `read` | Scores a draft against this channel's own history, not a generic rubric. |
| `preview_post` | `read` | The exact message that would be sent: title, body, media, formatting. |

## Publishing

| Tool | Scope | What it does |
|---|---|---|
| `create_post_from_text` | `full` | Saves a ready draft from text the assistant wrote. Accepts images and videos by URL; media is all-or-nothing, so a partially downloadable set fails rather than publishing half of it. |
| `schedule_post` | `full` | Publishes a draft now, or schedules it for a given time. |
| `cancel_scheduled_post` | `full` | Cancels a scheduled post by its plan id. |

## Content plans

| Tool | Scope | What it does |
|---|---|---|
| `get_content_plan` | `read` | The channel's plan configuration and its slots. |
| `find_free_slot` | `read` | The earliest slot in the plan with no post in it yet. |
| `create_content_plan` | `full` | Creates a content plan for a channel. |
| `get_playbook` | `read` | A step-by-step operator playbook for one workflow: analyze, create a plan, fill it, improve, or rewrite. |

## Channel memory

The brand brief and the banlist are what keep generated posts sounding like the channel
rather than like a language model.

| Tool | Scope | What it does |
|---|---|---|
| `get_channel_memory` | `read` | The channel's brand brief and banlist. |
| `set_brand_brief` | `full` | Replaces the channel's brand and tone guidance. |
| `add_banlist_entry` | `full` | Adds a forbidden word to the channel's banlist. |
| `remove_banlist_entry` | `full` | Removes a word from the banlist. |

## Limits

- **Rate limit:** 120 requests per 60 seconds per token. An agent in a tight loop should back off.
- **Availability:** every plan, including the free one.
- **Idempotency:** publishing tools are idempotency-keyed, so a retried call after a dropped
  connection does not post twice.
