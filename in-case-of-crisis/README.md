# In Case of Crisis

A ChatGPT/Codex plugin for retrieving the protocols your signed-in account
is authorized to access within your In Case of Crisis organization. Requires an authorized In Case of Crisis account.

Ask: “Find our workplace fire protocol” or “Browse our emergency response plans.”
The skill searches the connected service, asks you to choose when results are
ambiguous by listing choices in the conversation, and preserves the returned
safety-critical instructions, escalation contacts and citation.

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

`plugin.json` and `mcp.json` are the portable entry points. The `.codex-plugin/`
manifest and `.mcp.json` support compatibility hosts. No credentials or customer
protocols are included. The gateway, OAuth, and actual tool schemas must be
verified in a live installation before public release.

Source archives alone do not publish a plugin in ChatGPT's public directory.
The publisher must upload the complete plugin ZIP with its MCP configuration
and skill through OpenAI's submission flow, obtain approval, and publish. See the repository's publishing
guide for the release process.

Want to add just the connector yourself, without this package? See the
[create-it-yourself instructions](https://github.com/incaseofcrisis/chatgpt#create-the-connector-yourself-chatgpt-and-codex)
for ChatGPT and Codex.

This plugin does not contact emergency services. Do not wait for a lookup in an
immediate emergency; contact local emergency services or your site's responders.

Support: email support@incaseofcrisis.com.

MIT license; see LICENSE. Built by RockDove Solutions, Inc.
