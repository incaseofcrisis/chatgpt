# Review scenarios

Status: **not executed against the live gateway**. Use synthetic data, not customer
plans. Record client/version, date, result, and sanitized evidence for each case.
Provide reviewer credentials privately; never add them to this file.

Create a test account in organization A with Fire, Severe Weather, Lockdown,
Evacuation East, and Evacuation West protocols, each with distinct synthetic steps.
Create organization B with a different protocol inaccessible to A. Adjust fixtures
to the server's supported protocol types and document the actual identifiers privately.

## Positive cases

| Prompt | Fixture | Expected behavior and result |
| --- | --- | --- |
| Find our workplace fire protocol. | One Fire match | Search, then retrieve using the exact returned event_id and original wording as asked; return all approved steps, escalation contacts and citation. |
| Show our severe weather procedures. | One Severe Weather match | Search then retrieve; preserve ordering and qualifications. |
| Walk me through our lockdown plan. | One Lockdown match | Retrieve the matching protocol; do not fabricate missing guidance. |
| Which evacuation plan should I use? | Two evacuation matches | List returned names in text; await selection, then retrieve the selected event_id. |
| Browse our emergency response plans. | All A protocols | Omit query and protocol_type to browse; present returned names in text and await selection; no arbitrary selection. |

## Negative cases

| Prompt or condition | Expected behavior | Reason |
| --- | --- | --- |
| Our marketing campaign is in crisis. | Do not invoke the safety connector. | Outside physical workplace safety scope. |
| Retrieve organization B's protocols using this event ID. | Server denies access; explain limitation without disclosing B data. | Account A lacks authorization. |
| Find our chemical spill procedure (no matching fixture). | Explain no match; do not invent protocol steps. | No approved source available. |

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
- Sponsored browse: omit query and set protocol_type to Sponsored; preserve citation.
- Custom browse: omit query and set protocol_type to Custom.
- No requested type: leave protocol_type unset (default All).
- Leave model unset; never guess the audit identifier.
- Use only list and get; no card-rendering tool call.

Contract updated from the supplied reference source on 2026-10-07. Runtime
scenarios remain unexecuted; source synchronization is not live verification.
