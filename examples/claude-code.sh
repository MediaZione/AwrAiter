#!/usr/bin/env bash
# Claude Code — add the AwrAIter MCP server.

# OAuth: Claude Code walks you through the sign-in on first use.
claude mcp add --transport http awraiter https://awraiter.ai/mcp

# Or with a personal access token from https://awraiter.ai/mcp-connect:
# claude mcp add --transport http awraiter https://awraiter.ai/mcp \
#   --header "Authorization: Bearer YOUR_TOKEN"
