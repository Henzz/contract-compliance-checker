# Contract Compliance Checker

**Status:** in progress

## Problem

Reviewing signed contracts against a master template by hand is slow
and error-prone — missing clauses, altered definitions, and unfilled
placeholders are easy to miss in long documents. This tool automates
that comparison.

## How it works (planned)

1. Extract text from both the template and the signed contract (.docx)
2. Split each into sections/clauses
3. Match corresponding clauses between the two documents
4. Flag: missing clauses, altered wording, unfilled placeholders
5. Output a clause-by-clause compliance report

## Usage

\`\`\`bash
python main.py template.docx contract.docx
\`\`\`

## Tech

- Python
- python-docx (parsing .docx files)
- rapidfuzz (fuzzy text matching, planned)