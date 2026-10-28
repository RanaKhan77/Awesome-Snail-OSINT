# Contributing

Help maintain Awesome Snail OSINT as a reliable, readable, and privacy-respecting directory.

## Suggest a resource

Search existing entries and issues first. Then submit an issue or focused pull request with the resource's **name**, **canonical URL**, **specific OSINT use case**, **README category**, **access model** (free/freemium/paid), **date manually checked** (YYYY-MM-DD), and **known limitations**.

Prefer official documentation and direct publisher URLs. Avoid affiliate redirects and link shorteners. Use clear link labels and a one-sentence description when the purpose is not obvious.

## Correct a resource

For a broken link, report the existing URL, the actual error or changed content, the date checked, and a verified replacement if available. Do not assume an automated 403/429 response means the service is defunct.

## Pull request checklist

1. Confirm the entry is relevant and not duplicated.
2. Remove personal data, credentials, tokens, private investigation artifacts, or live exploit results.
3. Use authorized, reproducible examples only.
4. Run the documentation checker and its unit tests before submitting:
   - python3 scripts/check_docs.py
   - python3 -m unittest discover -s tests -v
5. Explain additions, corrections, and the evidence for any link replacement.

The maintainers review usefulness, provenance, privacy impact, accuracy, and categorization. Inclusion does not imply endorsement.

Read [the maintenance policy](docs/resource-quality.md) and [the field guide](docs/field-guide.md).
