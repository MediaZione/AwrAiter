# Security

## Reporting a vulnerability

Report it through **[awraiter.ai/support](https://awraiter.ai/support/)**, or directly to
**[@awraiter_bot](https://t.me/awraiter_bot)** on Telegram. Please do not open a public issue
for a security report.

Include what you need to make it reproducible: the request, the response, the account or
token used (never the token itself), and what you were able to reach that you should not
have been. We will confirm receipt and tell you what we found.

Please do not run automated scanners, load tests, or anything that degrades service for
other users. Test against your own account and your own channels.

## What the connector can and cannot reach

The MCP server acts through your AwrAIter account, not through your Telegram account.

- **No Telegram credentials are involved.** No phone number, no login code, no `.session`
  file. There is nothing of your Telegram account stored on our side to leak.
- **Scope is a team.** A connection reaches the channels of the team it was authorized for,
  and within that team only the channels the account is allowed to touch. Per-member channel
  restrictions from the panel apply to MCP identically.
- **Publishing goes through a service administrator** that you add to your own channel. Remove
  that administrator and publishing stops; nothing else about your account is affected.
- **Every write passes the same access checks as the panel.** MCP is another door into the
  same house, not a side entrance with a different lock.

## Tokens

- Personal access tokens are shown once, at creation, and stored hashed.
- Two scopes: `read` and `full`. A `read` token is not shown write tools at all, and a write
  call made anyway is refused server-side rather than client-side.
- A token is bound to one user, one team and one scope.
- Revoke any token, and see when it was last used, at
  [awraiter.ai/mcp-connect](https://awraiter.ai/mcp-connect).

## OAuth

OAuth 2.1 with PKCE and dynamic client registration. Redirect URIs are restricted to HTTPS
or HTTP loopback, authorization codes are single-use, and refresh tokens rotate on use.

## Rate limits

120 requests per 60 seconds per token. Exceeding it returns `429`; back off rather than retry
immediately.

## Scope of this repository

This repository holds documentation only. The AwrAIter service itself is closed-source, so
there is no application code here to audit. Reports about the running service are still
welcome through the channels above.
