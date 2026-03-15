import argparse
import re


def retrieve_policy(file_path):
    """
    Loads the policy document and extracts numbered clauses.
    Returns a list of (clause_number, clause_text).
    """
    clauses = []

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # match clause numbers like 2.3, 3.2 etc
    pattern = r'(\d+\.\d+)\s+(.*)'
    matches = re.findall(pattern, text)

    for num, clause in matches:
        clauses.append((num.strip(), clause.strip()))

    return clauses


def summarize_policy(clauses):
    """
    Create a structured summary while preserving clause meaning.
    """
    summary_lines = []

    for num, clause in clauses:
        summary = f"Clause {num}: {clause}"
        summary_lines.append(summary)

    return "\n".join(summary_lines)


def main():
    parser = argparse.ArgumentParser(description="Policy Summarization Tool")
    parser.add_argument("--input", required=True, help="Input policy file")
    parser.add_argument("--output", required=True, help="Output summary file")

    args = parser.parse_args()

    # Step 1: Load policy
    clauses = retrieve_policy(args.input)

    if not clauses:
        raise ValueError("No policy clauses found in the document.")

    # Step 2: Generate summary
    summary = summarize_policy(clauses)

    # Step 3: Write summary
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(summary)

    print("Summary generated successfully:", args.output)


if __name__ == "__main__":
    main()
