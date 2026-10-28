# OSINT Field Guide

A compact evidence-first workflow for investigations using public information. Pair it with the [tool directory](../README.md) and the [advanced techniques](../advanced-osint-techniques.md).

## 1. Frame the question

Record a legitimate purpose, the hypothesis, authorized entities, collection methods, exclusions, and collection window. Distinguish **publicly visible** from **authorized to interact with**.

| Decision | Example |
| --- | --- |
| Question | Which public hostnames relate to our company domain? |
| Scope | Organization-owned example.com and public records |
| Allowed methods | Search engines, certificate transparency, passive DNS |
| Exclusions | Account access, exploitation, active probing without permission |
| Standard of evidence | Independent corroboration for important attributions |

Stop when a source asks for bypassing access controls, when personal data is unnecessary, or when a method exceeds permission.

## 2. Choose the smallest useful source set

| Need | Where to start |
| --- | --- |
| Domain footprint | [Website security](../README.md#website-security) |
| Internet-indexed services | [Shodan reference](../shodan-dorks.md) |
| Repository metadata | [GitHub reference](../github-dorks.md) |
| Historical pages | [Web archives](../README.md#other-search-engines--dorks) |
| Geospatial context | [Geo tools](../README.md#geo-tools) |

Search results are leads. Cached pages, copied datasets, and search-index entries may be stale or incorrectly attributed.

## 3. Record evidence with provenance

For every material observation record the exact public URL/query, UTC timestamp, source operator, scope reference, what the source directly showed, evidence artifact identifier, and source limitations. Never place credentials or unnecessary personal data in public issues.

## 4. Keep observations and inferences separate

- **Observation:** What was directly returned by a source?
- **Inference:** What could that observation mean?
- **Alternative:** What else could produce the same observation?
- **Confidence:** Is corroboration independent and recent enough?

Two search tools drawing from the same upstream collection are not two independent confirmations.

## 5. Report uncertainty, not just findings

Include verified facts, possible explanations, evidence dates, conflicting observations, confidence, privacy considerations, and actions that require additional authorization. Use the [report template](report-template.md).

### Example: authorized passive domain inventory

1. Confirm domain ownership and engagement scope for example.com.
2. Inspect public certificate transparency records for associated names.
3. Cross-check with independent passive DNS or official organization documentation.
4. Separate historic certificate names from currently resolving services.
5. Produce an evidence table and document ambiguous attributions.
6. Seek explicit authorization before any active probing.

**Boundary:** A discovered hostname or indexed administrative interface does not grant permission to access or test it.
