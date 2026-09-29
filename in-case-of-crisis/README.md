# In Case of Crisis

A ChatGPT/Codex plugin for retrieving your organization's approved workplace
emergency protocols. Requires an authorized In Case of Crisis account.

Ask: “Find our workplace fire protocol” or “Browse our emergency response plans.”
The skill searches the connected service, asks you to choose when results are
ambiguous, and preserves the returned safety-critical instructions.

`plugin.json` and `mcp.json` are the portable entry points. The `.codex-plugin/`
manifest and `.mcp.json` support compatibility hosts. No credentials or customer
protocols are included. The gateway, OAuth, and actual tool schemas must be
verified in a live installation before public release.

Source archives alone do not publish a plugin in ChatGPT's public directory.
The publisher must submit the remote endpoint and skill through OpenAI's
With MCP flow, obtain approval, and publish. See the repository's publishing
guide for the release process.

This plugin does not contact emergency services. Do not wait for a lookup in an
immediate emergency; contact local emergency services or your site's responders.

MIT license; see LICENSE. Built by RockDove Solutions.
