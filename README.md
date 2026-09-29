# In Case of Crisis — ChatGPT plugin

Retrieve your organization's approved workplace emergency protocols through
ChatGPT and Codex. Built by RockDove Solutions. Version **0.2.0**, MIT licensed.

The plugin bundles a workflow skill and a connection to the existing In Case
of Crisis MCP gateway. It includes no customer protocols or credentials.
An active In Case of Crisis account with access to your organization's plans
is required. Public availability of the package does not grant account access.

## Try it

- “Find our workplace fire protocol.”
- “Show our severe weather procedures.”
- “Browse our emergency response plans.”

This is a protocol lookup assistant, not an emergency dispatch service.
In immediate danger, contact local emergency services or your site's responders.

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

- `in-case-of-crisis-0.2.0.zip`: the standalone plugin and MCP configuration for compatible local hosts.
- `in-case-of-crisis-skills-0.2.0.zip`: a skill bundle to attach to a **With MCP** submission. It deliberately omits connection configuration; it is not a functional standalone skills-only service.

The source repository is [incaseofcrisis/chatgpt](https://github.com/incaseofcrisis/chatgpt).
Attach the archives to a GitHub release. Include hidden plugin configuration
files when uploading source.

## Make it available in ChatGPT

GitHub hosts the source and release downloads. Public listing in ChatGPT requires
submission, approval, and publication through OpenAI. Follow
[Publishing](docs/publishing.md) and run the [review scenarios](docs/review-tests.md).

For development, connect the MCP endpoint through ChatGPT developer mode using
[OpenAI's quickstart](https://developers.openai.com/plugins/quickstart), authorize
a test account, and test the bundled skill in a supported plugin environment.
Local/repository MCP packages have different surface support from a publicly
registered remote MCP plugin; do not promise web/mobile installation from a ZIP.

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
OAuth, tenant isolation, tool schemas, and card rendering need live verification.
The gateway implementation and credentials are not included here.

## Support and license

Contact your RockDove Solutions account representative for service support.
Publish a public support URL and terms URL before submitting the listing.
See [LICENSE](LICENSE).
