# Publishing to GitHub and ChatGPT

## GitHub release

1. Use [incaseofcrisis/chatgpt](https://github.com/incaseofcrisis/chatgpt),
   the repository configured as `origin` in this checkout.
2. Upload the source, including the plugin's hidden compatibility files.
3. Run `python3 bin/package-plugin.py` and attach both `dist/` archives to a release.
4. Keep versions in the portable manifest, OpenAI compatibility manifest, and skill
   synchronized. Rebuild archives after changes.

## Public ChatGPT listing

Use OpenAI's [submission guide](https://developers.openai.com/plugins/deploy/submission).
Choose **With MCP** and supply the endpoint from `in-case-of-crisis/mcp.json`.
Attach the generated skills archive in the same draft. GitHub publication and
OpenAI publication are separate steps.

The publisher must provide its verified identity, public support and terms URLs,
reviewer access, domain verification, authentication configuration, and listing
materials. Run Scan Tools and resolve findings. Use the scenarios in
[review-tests.md](review-tests.md), recording actual results. After approval,
publish through the portal.

## Server work outside this repository

The original gateway configuration declares HTTP but supplied no interoperability
results. Verify Streamable HTTP and OAuth against the real host; do not change
transport based solely on a URL suffix. Confirm all three expected tools and
parameter schemas. Check that selection cards work in ChatGPT or return useful
text options. Tool metadata must accurately reflect real server side effects.

Use synthetic protocols in separate test organizations to check access boundaries,
revocation, empty results, and failures. Do not place credentials in this repository
or in public issue reports. Supply reviewer access privately through the portal.

No registered integration ID, support address, terms URL, or test result has been
invented. Complete those publisher-owned details before submitting.
