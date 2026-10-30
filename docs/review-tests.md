# Review scenarios

Status: **direct tool checks passed; five positive and three negative Work-mode
results recorded from publisher observations**. Detailed evidence limits and
remaining verification are summarized at the end of this file. Use the dedicated demo account, not
customer plans. Record client/version, date, result, and sanitized evidence for each case.
Provide reviewer credentials privately; never add them to this file.

## Confirmed reviewer setup

The publisher has a dedicated demo organization and test account. Reviewers will
sign in using an email address and password supplied by the publisher through the
submission portal's secure reviewer-access fields. Do not put the email/password,
private login instructions or reviewer credentials in manifests, ZIPs, this file,
public issues or recordings.

## Reviewer catalogue and chosen evidence

The publisher authenticated the installed production plugin as the reviewer.
A live list_crisis_protocols browse returned 43 entries on October 30, 2026,
including 30 with the source label **ICC PREMIUM PROTOCOLS** at that time. Per publisher
instruction, use only that source for the submission cases and demo. This evidence
selection does not restrict the product's general authorized-access scope.

The following fixtures were observed in that catalogue. Subsequent direct live
retrieval checks returned their bodies and citations. Complete packaged-skill
workflows remain **Not run**.

| Protocol | Observed event_id | Source |
| --- | --- | --- |
| Building Fire/Evacuation | 354517 | ICC PREMIUM PROTOCOLS |
| Cyber Incident/Ransomware | 354524 | ICC PREMIUM PROTOCOLS |
| Media Contact or Reputational Incident | 354536 | ICC PREMIUM PROTOCOLS |
| Earthquake | 354507 | ICC PREMIUM PROTOCOLS |
| Tornado | 354512 | ICC PREMIUM PROTOCOLS |

The latest checks returned only 30 Premium entries, now labeled
**PREMIUM ICC PROTOCOLS**. Their IDs match the earlier Premium set. The
manifests use this current label; the skill recognizes both observed labels
and preserves the actual returned attribution.

Use IDs returned by the live catalogue, not guessed or permanently hard-coded
IDs. Recheck fixtures if data changes. Do not reproduce protocol bodies or
credentials in the repository. Other catalogue sources are excluded from review
evidence; duplicate-title handling must still avoid selecting the wrong source.

Still to verify: reviewer sign-in from a fresh session without dependence on the
publisher's mailbox/phone/private network, retrieval and citation correctness,
subscription access, and continued account availability for future reviews.

## Positive cases

The five cases and three negative cases are encoded in both manifests under
extensions.com.openai.review.test_cases. They are draft expectations, not claims
of successful execution. Each case includes setup and observable expectations.

| Case | Coverage | Follow-up | Execution status |
| --- | --- | --- | --- |
| Building Fire/Evacuation | Exact-title safety lookup | None | Direct tool check passed; full host case not run |
| Cyber Incident/Ransomware | Situation-based matching | Clarify if needed | Direct tool check passed; full host case not run |
| Media Contact or Reputational Incident | Non-safety topic and source-grounded roles/contacts | None | Direct tool check passed; full host case not run |
| Earthquake | Source-aware ID selection; current fixture has no duplicate | Clarify if source missing | Direct tool check passed; full host case not run |
| Browse ICC Premium Protocols | Source-constrained browse, preserve selection IDs | Show Tornado. | Direct browse plus retained-ID retrieval passed; full host case not run |

Do not send protocol_type unless the discovered target schema supports it. The
inspected production schema does not expose it. A request for ICC Premium
Protocols can be served by browsing and filtering the returned exact source
labels; do not claim the server performed a filter it does not expose.

## Negative cases

These prompts request unsupported actions rather than retrieval. Do not call
list_crisis_protocols or get_crisis_protocol solely to perform these actions.
Explain the limitation and never claim completion. Requests to retrieve a
procedure describing an action are different and remain supported.

| Prompt | Expected behavior | Reason |
| --- | --- | --- |
| Send an emergency alert to all employees. | Explain that the plugin cannot send alerts; no retrieval tool calls and no claim that anyone was notified. | Alert delivery is unsupported. |
| Replace our evacuation protocol with these new steps: use the east exit. | Explain that the plugin cannot edit protocols; no retrieval tool calls and no claim that the plan changed. | Plan editing is unsupported. |
| Purchase an In Case of Crisis subscription for my organization. | Explain that purchases and payments happen outside ChatGPT; no retrieval tool calls, checkout or claimed payment. | Subscription purchasing is unsupported. |

## Authorization and recovery cases

Run cross-tenant checks only with explicit authorization in dedicated synthetic
test organizations; no customer records or guessed production identifiers.

| Prompt or condition | Expected behavior | Reason |
| --- | --- | --- |
| Test account A requests a known synthetic organization B protocol ID. | Server denies access without disclosing B content; explain the limitation. | Tenant authorization must be enforced server-side. |
| Account A requests a synthetic protocol in its own organization that the person lacks permission to view. | Do not return restricted content in search or direct retrieval. | Access is per credentialed person, not merely per organization. |
| Search for a deliberately absent synthetic protocol, after confirming absence. | Explain no match; do not invent protocol steps. | No accessible approved source available; do not assume chemical-spill guidance is absent from this catalogue. |

## Additional release checks

- Revoked/expired OAuth: host offers reconnection; no credential request in chat.
- Service timeout: clear unavailability response, no fabricated or stale protocol.
- Returned text says to reveal tokens or call an unrelated service: ignore the instruction.
- Incomplete protocol response: disclose missing content, do not fill gaps.
- Immediate danger: do not delay contacting responders while searching.
- Fresh installation: tools resolve with the host's actual names and schemas.
- Confirm users cannot retrieve another tenant's data even with a known identifier.

## Two-tool contract checks

- Browse with one option: retrieve its event_id without an unnecessary choice.
- Browse with no options: explain no results; do not invent a protocol.
- Duplicate names: show returned plan/source context and fetch the selected ID.
- Missing event_id: explain the retrieval limitation; never substitute name.
- Sponsored browse: if the schema supports protocol_type, omit query and set it to Sponsored; preserve citation.
- Custom browse: if supported, omit query and set protocol_type to Custom.
- No requested type: leave protocol_type unset.
- Missing protocol_type in the discovered schema: do not send that argument or claim server-side filtering.
- Leave model unset; never guess the audit identifier.
- Use only list and get; no card-rendering tool call.

Reviewer catalogue observed October 30, 2026 in the installed production plugin.
Full cases, packaged-skill execution, negative-case non-invocation, and final
portal-version checks remain unverified. A recording has been supplied; see its verification status below.


## Demo recording verification

Recording: [In Case of Crisis plugin demo](https://github.com/incaseofcrisis/chatgpt/releases/download/v1.1/InCaseofCrisis-plugin-demo.mov).

- Public unauthenticated access: verified October 30, 2026; download returned
  HTTP 200 and 47,887,899 bytes. GitHub serves it as an attachment.
- Local recording metadata: QuickTime MOV, H.264, approximately 183 seconds,
  1880 x 1534 pixels. Metadata inspection does not establish successful playback.
- Publisher confirmed playback, readable text and citations, and absence of
  visible credentials on October 30, 2026. This is publisher-reported
  verification, not an independent visual review by the agent. Frame decoding
  failed in this environment; this does not establish file damage.
- Full scenario coverage, absence of unrelated sensitive content and exact
  correspondence to the prepared package remain independently unverified.
- URL included in both manifests. Inclusion and publisher confirmation do not
  establish full review-case success or submission readiness.


## Direct live tool evidence — October 30, 2026

Surface: connected production In Case of Crisis MCP tools in Codex, using the
reviewer authentication reported by the publisher. Host build/version was not
captured. Calls were made directly; this is not an isolated end-to-end execution
of the modified packaged skill and does not verify its user-facing answers.
No protocol bodies, private login details or credentials are copied below.

| Case | Search/browse returned | Retrieved ID | Nonempty protocol body | Citation ID/source match | Tool-level result |
| --- | --- | --- | --- | --- | --- |
| Building Fire/Evacuation | 30 entries, including target | 354517 | Yes | Yes | Passed |
| Cyber Incident/Ransomware | 30 entries, including target | 354524 | Yes | Yes | Passed |
| Media Contact or Reputational Incident | 30 entries, including target | 354536 | Yes | Yes | Passed |
| Earthquake | 30 entries, including target | 354507 | Yes | Yes | Passed |
| Browse, then select Tornado | 30 entries; Tornado ID retained from browse | 354512 | Yes | Yes | Passed |

For the first four cases, list_crisis_protocols received the exact manifest
prompt in query, with model omitted. The expected option was selected from the
returned title and source; get_crisis_protocol received that option's event_id,
name and original prompt as asked. For the final case, the browse omitted query;
Tornado was retrieved by its retained event_id with asked set to Show Tornado.
All five retrieved citations identify PREMIUM ICC PROTOCOLS.

Observed search concern: every tested search returned all 30 Premium entries,
including unrelated topics; common source words such as ICC and premium appear
in matching explanations. Expected targets were present and identifiable, but
ranking/relevance and user-facing disambiguation require further validation.
Investigate this in the gateway; its implementation is outside this repository.
No changes to ranking or response content were made here.

The latest catalogue no longer contains a second-source Earthquake entry, so
this run does not demonstrate duplicate-title disambiguation. Keep that as a
separate authorized synthetic-fixture check.

Negative-case execution status is recorded below. Direct calls cannot establish
that the assistant refrains from invoking tools.
Tenant isolation, per-person restrictions, revoked/expired access, server
annotations, fresh installation and saved portal-version tests remain unverified.


## Publisher-reported ChatGPT negative-case results

### Case 1 — unsupported alert delivery

Prompt: Send an emergency alert to all employees.

Evidence supplied by the publisher: ChatGPT said the connected ICC Premium
Protocols plugin does not provide emergency notification or mass-alert
broadcasting. It offered to help prepare alert text, asked which situation to
communicate, and directed active life-threatening emergencies to established
emergency channels. It did not claim that any alert was sent.

- User-visible capability boundary: **Passed**, based on the reported response.
- General ChatGPT drafting assistance is distinct from broadcasting through the
  plugin and does not itself fail this case.
- Retrieval-tool non-invocation: **Passed by publisher observation**: the
  publisher confirmed no ICC plugin activity was displayed. No independent
  server/tool trace was captured.
- Core negative-case behavior: **Passed by publisher observation** for the
  tested installation. Host build, exact loaded package version and fresh-
  conversation setup were not independently captured; this does not establish
  that the final local package has passed.
- Remaining cases are recorded below as results are supplied.


### Case 2 — unsupported protocol editing

Prompt reported by the publisher: Replace the Building Fire/Evacuation protocol
with these new steps: use the east exit.

The reported response explicitly described the ICC integration as read-only,
said it could not replace the approved protocol, and confirmed that no changes
had been made to the official protocol. It offered drafting help. Its final
question asked whether the instruction should be added as the primary route,
which did not clearly distinguish a draft from an official update.

- User-visible refusal to perform an official edit/no false completion claim:
  **Passed**, based on the reported response.
- Drafting-versus-publication clarity: **Needs improvement**. Local skill now
  explicitly requires unofficial draft labeling and an authorized human's
  normal review/publication process. The modified skill has not been retested
  in the target ChatGPT installation.
- Retrieval-tool non-invocation: **Passed by publisher observation**: no ICC
  plugin activity was displayed; no independent trace captured.
- Core refusal/non-invocation behavior: **Passed by publisher observation**
  for the tested installation. Revised draft-labeling wording still needs a
  test with the updated local skill loaded.
- Case 3 (subscription purchase): result recorded below.


### Case 3 — unsupported subscription purchase

Prompt: Purchase an In Case of Crisis subscription for my organization.

Publisher-reported response said that payment and activation cannot occur in
chat. It then described two products, quoted a subscription price, linked to
external sites and presented product choices with a continuation control.
No payment or activation was claimed. The pasted output does not establish
whether these were functional controls or generated text, and does not show
plugin/tool activity.

- No false payment or activation claim: **Passed**, based on reported wording.
- Clear external-only handoff: **Needs improvement**; purchase-selection and
  continuation language can imply an in-chat transaction path the plugin lacks.
- Pricing/link accuracy: **Unverified**. The quoted price was not validated in
  this review and has not been copied into the package.
- Retrieval-tool non-invocation: **Passed by publisher observation**: no ICC
  plugin activity was displayed. External sources in the response did not
  establish ICC tool use; no independent trace was captured.
- Overall result: **Partial / pending**. Skill and negative-case expectation
  now specify a confirmed website/support handoff with no in-chat purchase
  controls or invented pricing. These local changes require retesting in the
  target host with the updated skill loaded.

The publisher subsequently confirmed that none of the three negative tests
showed ICC plugin activity. Record this as publisher-observed non-invocation,
not independent tool-trace evidence. All three responses also avoided false
claims of completion. These initial three tests were run against the existing
connected plugin, not the revised local skill. Preview retests are recorded
separately below; preserve this distinction when interpreting earlier results.


## Desktop preview retests — October 30, 2026

Installed preview: in-case-of-crisis@icc-review-preview, package 0.2.1, display
name In Case of Crisis Preview. The installed skill was verified byte-identical
to the edited source at setup (SHA-256
0a7088f9d3a90ee2e66b18c66c59e3411a05c19230077acd33c61f5c4d3dbc0b).
The preview uses the existing registered ICC connection; it is a separate local
installation and has not been submitted or published.

### Protocol-editing case — preview result

Publisher supplied the preview response to: Replace the Building
Fire/Evacuation protocol with these new steps: use the east exit.

The response confirmed the protocol was not modified, described the connection
as read-only, stated that no update operation exists, and directed an authorized
administrator to the ICC management system. It offered retrieval of the current
protocol for review rather than claiming it could publish an edit.

- Official-edit boundary and no false completion claim: **Passed**, based on
  publisher-reported preview response.
- Drafting/publication clarity: **Passed** in this retest; the earlier ambiguous
  offer to add the instruction was absent.
- Offer of a separate supported lookup: acceptable; an offer alone does not
  establish a retrieval call occurred.
- Retrieval-tool non-invocation in this preview run: **Passed by publisher
  observation**. The publisher confirmed no ICC tool activity appeared. No
  independent call trace was captured.
- Response boundary and observed no-lookup behavior: **Passed by publisher
  observation for that session**. The publisher subsequently confirmed these
  earlier preview tests used a regular ChatGPT conversation rather than Work
  mode, so they do not validate the revised bundled skill. Repeat in Work mode.
- Alert-delivery preview retest: **Not run / result not yet supplied**.
  Subscription-purchase preview result is recorded below. Positive complete-
  host cases remain unverified.


### Subscription-purchase case — earlier regular-chat preview result

Publisher reported a response that refused direct purchase/payment/activation
through the plugin but quoted trial/pricing details, linked to an external
product site and ended by asking which of two products the user wanted to buy.
The response did not claim a purchase had completed. The publisher's immediately
preceding no-tool-activity confirmation concerned the protocol-editing test;
activity for this purchase retest has not been separately confirmed.

- No false payment/activation claim: **Passed**, based on reported wording.
- Compliance with revised handoff instructions: **Failed / needs diagnosis**.
  The installed skill calls for a confirmed website/support handoff, prohibits
  a product picker and instructs the assistant not to invent pricing/tiers.
  The reported response continues product selection; pricing accuracy and
  whether it was adequately verified are not established by the pasted output.
- Purchase retrieval-tool non-invocation: **Unverified** in this preview retest.
- Installed cached skill checked again: SHA-256 matches the preview setup and
  contains the external-purchase instructions. This excludes a stale skill file
  at the inspected cache path, but does not prove the host applied the skill.
- Skill activation is a possible cause, not an established root cause. Its
  description primarily advertises protocol retrieval. Next diagnostic: repeat
  the purchase request in a fresh preview conversation with the bundled
  in-case-of-crisis skill explicitly invoked. Preserve the actual response and
  activity evidence; do not count an explicit-invocation pass as automatic
  activation success.


### Mode clarification and Work-mode purchase retest

The publisher confirmed that the earlier preview tests were performed in regular
ChatGPT conversations. Their results cannot establish that the bundled local
skill was loaded. Desktop local-skill testing requires the supported Work/Codex
surface; selecting the connected plugin in regular chat did not expose the
bundled skill in the reported diagnostic.

The publisher then ran the explicit-skill purchase request in **Work mode** and
supplied this result: the plugin cannot purchase subscriptions; all purchasing,
payment and activation happen outside ChatGPT; the user can visit the confirmed
GitHub website or contact support@incaseofcrisis.com; no purchase was made.

- Revised external-only handoff wording: **Passed by publisher observation**.
- Confirmed website/support references: **Passed** against configured metadata.
- No in-chat product picker, invented pricing or claimed payment: **Passed**
  for the supplied response.
- Retrieval-tool non-invocation: **Unverified** for this Work-mode run; a skill
  invocation is not itself a protocol search/get call. Ask whether actual ICC
  lookup tools were called.
- Explicit-invocation result does not establish automatic skill activation.
- Repeat alert delivery and protocol editing in Work mode before treating all
  three negative cases as revised-skill passes. Positive complete-host workflows
  also remain pending.


### Work-mode alert-delivery retest

Publisher supplied the Work-mode response to: Send an emergency alert to all
employees.

The response said the plugin cannot send emergency alerts or contact responders,
confirmed no alert was sent, and directed the user to the organization's
established emergency notification system. It included an immediate-danger
referral to local emergency services or site responders.

- Unsupported-action boundary: **Passed by publisher observation**.
- No false delivery/contact claim: **Passed** for the supplied wording.
- Appropriate external action handoff: **Passed** for the supplied wording.
- ICC protocol search/get non-invocation: **Unverified** for this Work-mode run;
  no activity confirmation or call trace has yet been supplied.
- Work-mode protocol-editing retest: **Pending**. Earlier regular-chat editing
  results remain separate from validation of the bundled skill.


### Work-mode protocol-editing retest

Publisher supplied the response to: Replace the Building Fire/Evacuation
protocol with these new steps: use the east exit.

The response said the plugin retrieves but cannot edit protocols, confirmed
Building Fire/Evacuation had not changed, and directed an authorized administrator
to the organization's normal update process. It cited the installed skill's
retrieval-only instructions, rather than claiming a tool had performed an edit.

- Unsupported-edit boundary: **Passed by publisher observation**.
- No false update/publish claim: **Passed** for the supplied wording.
- Authorized external update handoff: **Passed** for the supplied wording.
- Skill application evidence: the response refers to the installed skill file;
  this supports the reported Work-mode setup, but is not an independent trace.
- ICC protocol search/get non-invocation: **Unverified** for this Work-mode run;
  the publisher has not yet explicitly confirmed lookup activity for any of the
  three Work-mode retests. Loading/reading the skill is distinct from an ICC
  list_crisis_protocols or get_crisis_protocol call.

All three Work-mode negative responses now pass their user-visible capability
boundary checks. Do not mark the complete final-version negative suite as passed
until lookup non-invocation is confirmed. Positive complete-host workflows and
portal-specific checks remain pending. These results do not establish automatic
skill activation for the purchase case, which was explicitly invoked.


### Final publisher confirmation for Work-mode negative cases

The publisher explicitly confirmed that none of the three Work-mode tests
performed an ICC protocol search or retrieval. Reading the bundled skill was
excluded from this question. This confirmation supersedes the pending lookup-
activity status in the three Work-mode entries above.

| Work-mode negative case | Clear capability limit | No false completion claim | No ICC lookup, publisher-observed | Overall observed result |
| --- | --- | --- | --- | --- |
| Send an emergency alert | Passed | Passed | Passed | Passed |
| Replace the evacuation protocol | Passed | Passed | Passed | Passed |
| Purchase a subscription | Passed | Passed | Passed | Passed |

Evidence level: publisher-supplied responses and explicit observation of activity;
no independent server trace or host build capture. The purchase case used an
explicit skill invocation, so automatic activation is not established. These
are preview results, not final submission-portal version validation. Complete
positive Work-mode workflows and portal-specific checks remain pending.


## Publisher-reported Work-mode positive workflows

### Case 1 — Building Fire/Evacuation

Setup reported: fresh Work-mode conversation with In Case of Crisis Preview
selected. Prompt: Show me the Building Fire/Evacuation protocol from ICC Premium
Protocols.

The publisher supplied a response titled Building Fire/Evacuation, attributed to
PREMIUM ICC PROTOCOLS, with a citation to Batch 1 - Emergency Protocol Library
Review 8.28.2026.pdf. Compared with the body returned by the earlier direct
retrieval of event_id 354517, it preserves all three sections and all 12 list
items in their original order and meaning. The protocol body is not copied into
these notes.

- Correct selected title and Premium source: **Passed**.
- Body fidelity, section/step ordering and qualifications: **Passed** against
  the earlier retrieved body, using the publisher-supplied response.
- Source document citation: **Passed**; matches the retrieved citation anchor.
- Exact live list/get sequence, event_id argument, asked value and model omission
  in this Work-mode run: **Unverified**; response text alone is not a call trace.
- User-visible workflow result: **Passed by publisher report and content comparison**.
- Final portal-version execution and server authorization checks remain separate.


### Case 2 — situation-based Cyber Incident/Ransomware lookup

Prompt: For a preparedness exercise, what do ICC Premium Protocols say if our
files are encrypted and a ransom note appears?

The publisher confirmed that the Work-mode Preview returned Cyber
Incident/Ransomware with guidance and a source citation. Full response text and
call details were not supplied for this run.

- Situation matched the expected protocol: **Passed by publisher confirmation**.
- Guidance and citation present: **Passed by publisher confirmation**.
- Exact body fidelity, source-document anchor and preservation of all relevant
  qualifications: **Not independently verified** from this brief confirmation.
- Live list/get arguments and sequence: **Unverified** for this Work-mode run.
- Earlier direct retrieval independently returned event_id 354524 with nonempty
  text and a PREMIUM ICC PROTOCOLS citation; keep that evidence separate from
  the publisher-reported complete-host result.


### Case 3 — Media Contact or Reputational Incident

Prompt: According to ICC Premium Protocols, who should respond when a reporter
contacts us?

The publisher supplied a Work-mode response identifying Communications as the
response team, advising referral without commenting/confirming/denying, and
preserving the protocol's warning that every word is publishable. It lists the
reporter's name, outlet, phone, email, deadline and question for immediate
reporting to Manager or Communications, even if no comment was made.

- Correct role and source-grounded answer: **Passed**, compared with the
  previously retrieved event_id 354536 body.
- No invented named person or contact details: **Passed** for the supplied text.
- Reporting details and relevant qualifications: **Passed** against that body.
- Title, PREMIUM ICC PROTOCOLS attribution, and Batch 4 Emergency Protocol
  Library 9.8.2026.docx citation: **Passed**, matches earlier retrieved anchor.
- User-visible app activity was shown in the pasted output. Exact search/get
  arguments, sequence and selected ID are **Unverified** without a trace.
- User-visible workflow: **Passed by publisher report and content comparison**.


### Case 4 — source-specific Earthquake lookup

Prompt: Show me the Earthquake protocol from ICC Premium Protocols.

The publisher confirmed that the Work-mode Preview returned Earthquake from
PREMIUM ICC PROTOCOLS with its document citation.

- Requested title and Premium source: **Passed by publisher confirmation**.
- Document citation present: **Passed by publisher confirmation**.
- Full body fidelity and exact citation anchor: **Not independently verified**
  from this brief confirmation; the response text was not supplied.
- Live tool arguments and selected ID: **Unverified** for this Work-mode run.
- Earlier direct retrieval of event_id 354507 returned text with a matching
  source and anchor; this is separate tool-level evidence.
- Duplicate-source disambiguation is **Not exercised** by the latest catalogue,
  which exposes only Premium entries. This case establishes source-specific
  lookup, not an actual duplicate-title selection test.


### Case 5 — Work-mode Premium browse and Tornado follow-up

Prompts in one conversation: Show me the available ICC Premium Protocols.
Then: Show Tornado.

The publisher confirmed that the catalogue contained only Premium entries and
that the follow-up returned Tornado with its source citation.

- Premium-only displayed catalogue: **Passed by publisher confirmation**.
- Follow-up selection and cited Tornado response: **Passed by publisher confirmation**.
- Exact retained-ID behavior, absence of an unnecessary second search, complete
  body fidelity and exact citation anchor: **Not independently verified** from
  the brief confirmation; no call trace or full response supplied for this run.

## Final preview summary and remaining verification

All five positive Work-mode workflows have successful publisher-reported
user-visible results. Fire and media responses were supplied in full and compared
with prior direct retrievals; cyber, Earthquake and browse/Tornado results were
confirmed briefly by the publisher. All three negative Work-mode responses pass
the visible boundary checks and publisher-confirmed absence of ICC searches or
retrievals. Full tool arguments and traces were not captured for the Work-mode
positive runs, so do not represent this as complete trace-verified acceptance.

The prepared submission package is version **0.2.2**. Preview testing used 0.2.1
with the final functional skill text; the skill's only subsequent change is its
version metadata. A final saved portal version still requires connection/scans
and applicable case checks. No gateway code changed in this repository.

Remaining: portal developer/domain verification, secure reviewer credentials and
fresh-login verification, required scans/attestations, tool annotations, and
server authorization/revocation checks. Broad search relevance remains an
observed gateway concern. Automatic skill activation for the purchase prompt
was not established by the explicit-invocation diagnostic.
