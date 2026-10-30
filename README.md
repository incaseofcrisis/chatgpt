# In Case of Crisis — ChatGPT plugin

Retrieve the protocols available to your signed-in In Case of Crisis account
within your organization through ChatGPT and Codex. Built by RockDove Solutions, Inc. Version **1.2.0**, MIT licensed.

The plugin bundles a workflow skill and a connection to the existing In Case
of Crisis MCP gateway. It includes no customer protocols or credentials.
An active In Case of Crisis account with access to your organization's plans
is required. Public availability of the package does not grant account access.

## Choose your setup

| Setup | Best for | Start here |
| --- | --- | --- |
| **Pre-configured plugin** | Installing the ready-made In Case of Crisis plugin (skill plus connector) from this repository's packages, or publishing it through OpenAI. | [Package contents](#package-contents), [Build downloadable packages](#build-downloadable-packages), [Make it available in ChatGPT](#make-it-available-in-chatgpt) |
| **Create it yourself** | Workspace admins who want to add the In Case of Crisis connector to ChatGPT (or Codex) on their own, with no files from this repository. | [Create the connector yourself](#create-the-connector-yourself-chatgpt-and-codex) |

Both use the same hosted connector and the same per-person sign-in, so
ChatGPT only sees the protocols published for the signed-in person's
organization.

## Try it

- “Find our workplace fire protocol.”
- “Show our severe weather procedures.”
- “Browse our emergency response plans.”

This is a protocol lookup assistant, not an emergency dispatch service.
In immediate danger, contact local emergency services or your site's responders.

## Create the connector yourself (ChatGPT and Codex)

Use this path to add the In Case of Crisis MCP connector to ChatGPT
without the pre-configured plugin in this repository. ChatGPT delivers
custom MCP servers as plugins: a workspace administrator creates it once
(Part 1, about 10 minutes), then each employee installs it and signs in once
(Part 2, about a minute). Part 3 covers Codex for technical staff.

> **In a life-threatening emergency, call 9-1-1 first.** The connector
> returns your organization's approved guidance. It does not contact
> emergency services, send notifications, or file incident reports; use the
> In Case of Crisis app for those actions.

The connector is read-only. Each employee signs in with their own In Case of
Crisis account, so ChatGPT only sees the protocols published for that
person's organization and never sees their In Case of Crisis password.

### Before you start

- Your organization has an active In Case of Crisis subscription, and
  RockDove Solutions has enabled the MCP connector for it. Your Customer
  Success Manager (CSM) can confirm both.
- Your ChatGPT plan supports custom MCP servers. Business, Enterprise, and
  Edu workspaces support the full workflow in this guide. Individual Pro
  accounts can connect custom MCP servers with read access, which covers
  everything this connector does. **Free and Plus do not support custom MCP
  servers.**
- Part 1 needs a workspace Admin or Owner. On Business, only Admins and
  Owners can create and publish plugins for custom MCP servers. On
  Enterprise and Edu, Admins can grant creation to other roles, but only
  Admins and Owners can publish to the workspace.
- You have the connector address:

```
https://mcpgateway.incaseofcrisis.com/mcp
```

### Part 1: Workspace administrator setup (one time)

Developer Mode is no longer a prerequisite. ChatGPT shows a risk
acknowledgement for each custom server instead.

1. **Confirm the permission.** In the Admin console, open **Workspace
   settings → Permissions & roles** and check that **Create plugins with
   MCPs** is on for your role. It is off by default on Enterprise.
2. Open **Plugins** in the ChatGPT sidebar (or go to `chatgpt.com/plugins`),
   select **+**, then **Add custom MCP server**.
3. Enter the name `In Case of Crisis MCP` and this description: *Returns this
   organization's approved crisis, emergency and incident-response
   protocols.* ChatGPT uses the description to decide when to call the
   connector, so keep it specific.
4. Paste the connector address under **Connection** and choose **OAuth** for
   authentication.
5. Select the **I understand and want to continue** checkbox, then **Create
   as a plugin**. Review the discovered tools. You should see two read-only
   tools, one that lists crisis protocols and one that returns a single
   protocol.
6. **Test it before publishing.** Open a new chat, type `@`, choose **In Case
   of Crisis MCP**, sign in, and run the prompts under
   [Verification](#verification).
7. **Publish to the workspace.** In the Admin console, open **Plugins**,
   select **In Case of Crisis MCP**, and publish it. A connector created
   with the earlier **Workspace settings → Apps → Create** flow publishes
   from **Plugins → Manage Legacy Apps → Drafts**. On Enterprise and Edu,
   use **Configure Access** to choose which groups receive it.
8. **Set the installation policy** on the plugin's detail page. *Available*
   lets eligible members install it; *Installed* installs it for them
   automatically. RockDove Solutions recommends **Installed** for anyone who
   may need protocols during an incident, so the connector is ready before
   it is needed.

**Optional: action permissions.** Both In Case of Crisis tools are read
actions. Setting the plugin's **Permissions** to **Allow read actions** stops
ChatGPT asking for approval on every lookup. The trade-off is one fewer
confirmation step for employees; the connector has no write actions to
approve.

### Part 2: Activation for everyone else (about one minute)

1. Open **Plugins** in the ChatGPT sidebar. If your admin chose *Available*,
   select **In Case of Crisis MCP**, then **Install plugin**. If it is
   already installed, skip to step 2.
2. Start a new chat, type `@`, and choose **In Case of Crisis MCP**. You can
   also select it from **Plugins** in the message box.
3. Sign in once. Enter the email address you use for In Case of Crisis, or
   select **Login with Microsoft** if that is how you normally sign in, and
   approve access.

ChatGPT applies a selected plugin to that message. `@`mention **In Case of
Crisis MCP** again when a follow-up question needs fresh information from
the plan.

### Part 3: Codex (technical staff)

The ChatGPT desktop app, the Codex CLI, and the Codex IDE extension share
one configuration file, `~/.codex/config.toml`. Add the connector once and
sign in:

```sh
codex mcp add in-case-of-crisis --url https://mcpgateway.incaseofcrisis.com/mcp
codex mcp login in-case-of-crisis
```

The resulting entry in `config.toml` looks like this:

```toml
[mcp_servers.in-case-of-crisis]
url = "https://mcpgateway.incaseofcrisis.com/mcp"
```

In the desktop app, open **Settings → MCP servers** and select
**Authenticate** if the connector asks for sign-in. Type `/mcp` in the
composer to confirm it is connected. If your workspace has already published
the plugin from Part 1, it is also available in a Codex task under
**Sources → Use plugins**. No client secret or API key is involved; do not
add one to `config.toml`.

### Verification

Start a new chat, `@`mention **In Case of Crisis MCP**, and ask one of
these:

- "Using In Case of Crisis MCP, show me our approved crisis protocols."
- "What does our plan say to do during a flash flood?"
- "Someone smells gas in the break room. What does our plan say?"

The first time, ChatGPT may ask permission to use the tool; select **Allow**.
A working answer leads with your plan, keeps the steps in the plan's order,
and ends with a citation.

### Rollout notes

- **No mobile support.** Custom MCP servers do not work in the ChatGPT mobile
  apps. Anyone who may need protocols away from a desk should use the In
  Case of Crisis app itself.
- **Connect before you need it.** Each person signs in once. Have employees
  complete Part 2 during onboarding, not during an incident.
- **Name the connector in your question.** Selecting or `@`mentioning In Case
  of Crisis MCP is the reliable way to get an answer from your plan.
- **Deep research** can use the connector for read lookups. Expect the
  protocol list as text rather than an interactive card.
- **Tool list updates.** ChatGPT keeps a snapshot of the connector's tools
  once it is approved. If RockDove Solutions announces a new tool, an admin
  refreshes it from the plugin's workspace settings.

### Troubleshooting

| Symptom | Action |
| --- | --- |
| No **Add custom MCP server** option | Your role lacks **Create plugins with MCPs**, or your plan does not support custom servers. |
| Tool scan fails or times out | Check the connector address, including the `/mcp` path. |
| Employees cannot find the plugin | Check it is published and set to *Available* or *Installed* for their group. |
| Organization login not shown | Choose **Login with Microsoft** if your organization uses Microsoft Entra for In Case of Crisis. |
| ChatGPT answers without your plan | `@`mention In Case of Crisis MCP in that message and ask again. |
| A protocol you expect is missing | Contact your CSM; it may not be published to your organization yet. |
| Signed in but access stops | Contact support. Do not delete and recreate the connector. |

Still stuck? See [Support and license](#support-and-license).

*Based on the In Case of Crisis MCP Connector install guide for ChatGPT and
Codex, v2.0 (October 27, 2026).*

## Tools

The connector contract has two tools, used in sequence:

| Tool | Purpose and inputs |
| --- | --- |
| `list_crisis_protocols` | Search approved material with optional `query`; omit it to browse the catalogue. When the discovered server schema supports it, optional `protocol_type`: `All` (default), `Custom` (organization plans), or `Sponsored` (ICC-curated protocols with citations). Set a filter only when requested. |
| `get_crisis_protocol` | Retrieve one protocol's full procedure, escalation contacts and citation. Requires `event_id` from a list result. Pass original user wording as `asked`; `name` is informational only. |

Both tools accept optional `model` audit metadata; the skill leaves it unset.
For ambiguous matches, the assistant lists the returned names and asks the user
to choose, then retrieves the selected ID. There is no separate selection-card
tool in this contract. Same-named protocols must be distinguished by their IDs.

Contract synchronized from the supplied reference project's skill and README on
**2026-10-07**. This is a source-based update, not a successful live MCP discovery.
The connector owns the tool definitions and may change independently of this package.

## Package contents

The installable plugin root is `in-case-of-crisis/`:

- `plugin.json`: portable Agent Plugins manifest with OpenAI presentation metadata.
- `mcp.json`: remote MCP connection for portable hosts.
- `.codex-plugin/plugin.json` and `.mcp.json`: compatibility configuration.
- `skills/in-case-of-crisis/SKILL.md`: protocol lookup workflow.
- `icon.png` and `LICENSE`: branding and redistribution license.

There are no runtime dependencies or local server processes in this repository.

## Build downloadable packages

Requires Python 3.10 or later, with no third-party packages:

```sh
python3 bin/package-plugin.py
```

This creates two archives in `dist/`:

- `in-case-of-crisis-1.2.0.zip`: the complete plugin, including its MCP configuration, for the initial public submission and compatible local hosts.
- `in-case-of-crisis-skills-1.2.0.zip`: a supplementary skill bundle for hosts that explicitly accept it. It omits MCP connection configuration and is not the complete plugin or the initial public submission archive.

The source repository is [incaseofcrisis/chatgpt](https://github.com/incaseofcrisis/chatgpt).
Attach the archives to a GitHub release. Include hidden plugin configuration
files when uploading source.

## Make it available in ChatGPT

GitHub hosts the source and release downloads. Public listing in ChatGPT requires
submission, approval, and publication through OpenAI. Follow
[Publishing](docs/publishing.md) and run the [review scenarios](docs/review-tests.md).

For development, connect the MCP endpoint using ChatGPT's **Add custom MCP
server** flow (see [Create the connector yourself](#create-the-connector-yourself-chatgpt-and-codex);
Developer Mode is no longer required) or
[OpenAI's quickstart](https://developers.openai.com/plugins/quickstart), authorize
a test account, and test the bundled skill in a supported plugin environment.
Local/repository MCP packages have different surface support from a publicly
registered remote MCP plugin; do not promise web/mobile installation from a ZIP. Custom MCP servers do not
work in the ChatGPT mobile apps.

## Data and authentication

The MCP connection uses the public endpoint already supplied in the original
plugin. Authentication is expected to use each user's own account. The server
must enforce authorization and organization isolation; a manifest cannot do so.
Situation text and tool parameters are sent to the service to retrieve protocols.
ChatGPT and the service may process and retain data according to their respective
policies; this repository makes no zero-retention claim.

The supplied [privacy policy](https://www.incaseofcrisis.ai/privacy) must be
reviewed by the publisher for accuracy before release. Never commit demo
credentials, customer plans, tokens, or private test outputs.

## Validation status

Static package checks do not establish server interoperability. Streamable HTTP,
OAuth, tenant isolation, and tool schemas still need live verification.
The two-tool contract above comes from the supplied reference source; the direct
MCP discovery attempt required authentication and did not verify the live tool list.
The gateway implementation and credentials are not included here.

## Support and license

Email support@incaseofcrisis.com for setup help or to report an issue, for
either the pre-configured plugin or the connector you create yourself. For
connector setup, mention "In Case of Crisis MCP connector setup — ChatGPT"
(or Codex). Your Customer Success Manager (CSM) can also confirm whether the
connector is enabled for your organization.

Listing support: [Support and license](https://github.com/incaseofcrisis/chatgpt#support-and-license).
Terms: [In Case of Crisis AI Terms of Service](https://www.incaseofcrisis.ai/terms).
See [LICENSE](LICENSE).
