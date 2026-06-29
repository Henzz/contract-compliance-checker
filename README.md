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

## Setup

Clone the repo, then set up a virtual environment and install dependencies:

\`\`\`bash
# Create a virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
\`\`\`

## Usage

\`\`\`bash
python main.py template.docx contract.docx
\`\`\`

Pass the path to your master template and the signed contract you want
to check. The tool will compare the two and report differences.

To deactivate the virtual environment when you're done:

\`\`\`bash
deactivate
\`\`\`

## Tech

- Python
- python-docx (parsing .docx files)
- rapidfuzz (fuzzy text matching, planned)