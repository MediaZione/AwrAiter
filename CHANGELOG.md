# Changelog

Changes to the public interface of the AwrAIter MCP server — tools, scopes, authentication and
limits. Changes inside the AwrAIter panel that do not alter this interface are not listed here.

Dates are in UTC. This file starts at the first public release of the documentation; the state
described under 1.0.0 is what the live server has been serving up to that date.

## Unreleased

- **`review_posts`** (new, `read`, live since 2026-10-16). How recent posts did against the channel's own posts at the
  same age: one post by `postId`/`tgMsgId` or the last `days` (default 7, max 30), up to 20; posts under
  6 hours are counted in `summary.too_early` instead of listed.
  Verdict `above` / `on_par` / `below` / `too_early` / `no_baseline`, plus `viewsScore` and
  `engagementScore`; paid plans also get the excerpt and opening features.
- **Learnings journal** (live since 2026-10-16). `add_channel_learning` and `remove_channel_learning` (new, `full`) keep up
  to 30 hypotheses and learnings per channel; `get_channel_memory` now returns `learnings`.
- **`set_assist_mode`** (new, `full`, live since 2026-10-16). How much the assistant coaches the user: `quiet`, `normal`
  or `coach`. The server instructions now carry the user's mode and, until one is chosen, ask the
  assistant to ask once. Warnings stay in every mode.
- **`get_playbook` task `onboarding`** (live since 2026-10-16). A first session with a channel:
  read its history and numbers, build an audience portrait from the data and the operator's
  answers, draft a brand brief and banlist (saved only on the operator's yes), propose rubrics
  and a posting rhythm, interlink posts (navigation post, links to earlier posts, series,
  digests), then hand over to the content plan. Nothing is published. New MCP prompt
  `onboard_channel` starts it. The server instructions now offer it once when a channel has no
  brand brief, and carry short post-craft rules.
- **`get_channel`: `url` and `postLinkBase`.** The channel's public t.me link (null for a private
  channel) and the prefix for links to its posts: append `/<message id>`.
- **`get_channel_insights`: `link` on top/flop posts** when the channel's link is known.
- **`create_post_from_text`: `audioUrls` and `rightsConfirmed`** (live since 2026-10-15). Up to 5
  direct links to audio files (MP3, M4A, OGG, WAV, FLAC, up to 49 MB each), sent as music tracks;
  several tracks form an album. Cannot be combined with `imageUrls`/`videoUrls`. Requires
  `rightsConfirmed: true`, otherwise the call fails with `rights_not_confirmed`. See
  [media by URL](docs/tools.md#media-by-url).
- **`get_playbook` task `team`.** Returns how inviting people works: seats, the 48-hour
  one-person invite link, the owner's and the invitee's steps, and what each refusal from the
  bot means. The connector still cannot create, send or accept invites.
- New guide: [team and invites](docs/team.md) ([ru](docs/team.ru.md)).

## 1.0.0 — 2026-08-26

First public release of this repository.

The server at `https://awraiter.ai/mcp` exposes 25 tools over Streamable HTTP, authenticated
either by OAuth 2.1 with PKCE and dynamic client registration, or by a personal access token
issued at [awraiter.ai/mcp-connect](https://awraiter.ai/mcp-connect).

- **Two token scopes.** `read` and `full`. A `read` connection is not shown the nine tools that
  change something, and a write call made anyway is refused server-side rather than hidden in
  the client.
- **Team-bound connections.** Every call resolves against one team, and within it only the
  channels the account may touch — per-member channel restrictions from the panel apply
  identically over MCP.
- **Idempotent publishing.** `create_post_from_text` and `schedule_post` are idempotency-keyed,
  so a retry after a dropped connection does not post twice.
- **Media by URL.** `create_post_from_text` accepts images and videos by URL, all-or-nothing:
  a set that only partly downloads fails instead of publishing half of it.
- **Credit metering.** `deep_analyze` is the only tool that spends the team's AI credits. Every
  other tool is free on every plan, including the free tier.
- **Rate limit.** 120 requests per 60 seconds per token, answered with `429`.
- **Registry.** Published as `ai.awraiter/telegram`; the manifest lives in
  [`server.json`](server.json).

Documentation in this release: [connection guide](docs/connect.md)
([ru](docs/connect.ru.md)), [tool reference](docs/tools.md) ([ru](docs/tools.ru.md)),
[security model](SECURITY.md), and [client configuration examples](examples/).
