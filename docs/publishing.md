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
Prepare the listing, review cases and demo recording before the final portal
upload. Use the complete `dist/in-case-of-crisis-<version>.zip` as the initial
upload: it includes `mcp.json`, the skill, manifests and assets. The `-skills`
archive omits the MCP configuration and is not the complete remote-MCP submission.
Do not create a skills-only draft intending to add the MCP server later.
GitHub publication and OpenAI publication are separate steps.

Confirmed publisher choices:

- Verified business identity to use: **RockDove Solutions, Inc.** Verification
  itself must still be completed or checked in the intended portal organization.
- Availability: **United States only** (`publication.countries: ["US"]`).
- Subscriptions and payments: handled entirely outside ChatGPT; the plugin does
  not initiate purchases, checkout or payment processing.
- Website and support: the public GitHub repository and its Support and license
  section, which lists support@incaseofcrisis.com.
- Terms: https://www.incaseofcrisis.ai/terms.
- A dedicated demo organization and test account already exist. Reviewers use
  email/password sign-in; the publisher supplies credentials only in the secure
  reviewer-access fields during submission. Never package credentials or private
  reviewer login instructions.

Before submission, confirm the actual demo fixtures and successful reviewer
sign-in. Record and verify a reviewer-accessible demo, run the scenarios in
[review-tests.md](review-tests.md), and retain actual results. Rebuild and inspect
the final ZIP, including its review metadata. Then upload that complete package
as a draft to the intended organization/project and existing plugin identity,
inspect imported values, complete domain verification and authentication setup,
and resolve required tool/skill scan findings. Have the authorized publisher
complete required attestations. Draft upload, submission for review and
publication after approval are separate actions.

## Server work outside this repository

The original gateway configuration declares HTTP but supplied no interoperability
results. Verify Streamable HTTP and OAuth against the real host; do not change
transport based solely on a URL suffix. Confirm both tools (`list_crisis_protocols` and `get_crisis_protocol`) and
their parameter schemas, including required `event_id` on retrieval. Verify
that ambiguous matches are presented as text choices and the selected ID is
used to fetch the protocol. Tool metadata must accurately reflect real server side effects.

Use synthetic protocols in separate test organizations to check access boundaries,
revocation, empty results, and failures. Do not place credentials in this repository
or in public issue reports. Supply reviewer access privately through the portal.

No registered integration ID or runtime test result has been invented.
Confirmed publisher details do not establish portal verification or test success.
