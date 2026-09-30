# Working as a team: inviting people

[Русская версия](team.ru.md) · [Support page](https://awraiter.ai/support/#team)

Several people can run the same channels as one team. The team owner invites them; each member gets a role and, if you want, access to only some of the channels.

**Seats.** Every member takes one seat, the owner included. The free plan has one seat, so inviting people needs a paid plan; the plan cards in the panel show how many seats each plan gives. A pending invite takes no seat until it is accepted. **Settings → Team** shows how many seats are used.

**The owner invites:**

1. Open **Settings → Team** and press **Add member**.
2. Select a role and press **Invite**.
3. Copy the link and send it to the person in any messenger. The link works for 48 hours and for one person; for several people, create a link for each.

**The invited person joins:**

1. Open the link on a device with Telegram. It opens @awraiter_bot; press **Start** if Telegram asks.
2. The bot names the team and your role. Press **Accept invitation**.
3. Press the **Open …** button under the bot's reply. You are signed in and land in the new team.
4. Already in another team? Switch teams at the top of the sidebar (**Switch team**).

**Roles and channels.** The role decides what a member may do; roles are edited in **Settings → Team → Roles**. In **Settings → Team → Members**, the **Channels** column limits a member to the channels you pick; leave it empty for access to every channel. **Remove user** frees the seat.

**If an invite does not work,** the bot says why:

- “This team is on the free plan”: the owner picks a paid plan (**Account → Subscribe**) and sends a new link.
- “This team's subscription is inactive”: the owner renews it (**Account → Manage subscription**).
- “This team has reached its member limit”: the owner removes a member or moves to a plan with more seats.
- “This invitation has expired” or “the invitation was not found”: the link is older than 48 hours, was revoked or was already used. The owner creates a new one.
- Nothing happens after the click: open the link in the Telegram app, not in a browser, and press **Start**.

An AI assistant connected over MCP can walk you through this as well, but it cannot send invites: the team owner creates the link in the panel.

## Over MCP

`get_playbook` with `task: "team"` returns this procedure to the assistant, so ChatGPT, Claude or
any other connected client can answer "how do I add a colleague?" or "why does my invite link
fail?". The connector has no tool that creates, sends or accepts invites; `list_teams` shows
which teams the connected account belongs to.
