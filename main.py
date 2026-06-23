"""
Contract Compliance Checker
Compares a signed contract against a master template to flag
missing clauses, altered definitions, and unfilled placeholders.
"""

from docx import Document


def extract_text(file_path):
    """Extract raw paragraph text from a .docx file."""
    doc = Document(file_path)
    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    return paragraphs


def compare_documents(template_path, contract_path):
    """
    Compare a contract against a template.
    Returns a placeholder result for now — real comparison logic comes next.
    """
    template_text = extract_text(template_path)
    contract_text = extract_text(contract_path)

    print(f"Template has {len(template_text)} non-empty paragraphs.")
    print(f"Contract has {len(contract_text)} non-empty paragraphs.")

    # TODO: split into sections/clauses
    # TODO: align matching clauses between template and contract
    # TODO: flag missing / altered / unfilled clauses

    return {
        "status": "stub - comparison logic not yet implemented"
    }


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python main.py <template.docx> <contract.docx>")
        sys.exit(1)

    result = compare_documents(sys.argv[1], sys.argv[2])
    print(result)