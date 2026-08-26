# Changelog

Changes to the public interface of the AwrAIter MCP server — tools, scopes, authentication and
limits. Changes inside the AwrAIter panel that do not alter this interface are not listed here.

Dates are in UTC. This file starts at the first public release of the documentation; the state
described under 1.0.0 is what the live server has been serving up to that date.

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
