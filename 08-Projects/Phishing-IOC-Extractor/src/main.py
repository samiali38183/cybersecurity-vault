"""Phishing IOC Extractor - CLI entry point."""
import argparse
import json
import sys
from email import message_from_string
from pathlib import Path

from extractor import extract_all


def read_file(file_path: str) -> str:
    """Read text from a file. Handles .eml files specially."""
    path = Path(file_path)

    if not path.exists():
        print(f"Error: file not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    raw = path.read_text(encoding="utf-8", errors="ignore")

    # If it's an .eml file, parse headers + body using stdlib email module
    if path.suffix.lower() == ".eml":
        msg = message_from_string(raw)
        headers = "\n".join(f"{k}: {v}" for k, v in msg.items())
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    payload = part.get_payload(decode=True)
                    if payload:
                        body += payload.decode("utf-8", errors="ignore")
        else:
            payload = msg.get_payload(decode=True)
            if payload:
                body = payload.decode("utf-8", errors="ignore")
        return headers + "\n\n" + body

    return raw


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract IOCs (IPs, domains, URLs, emails, hashes) from a file.",
    )
    parser.add_argument(
        "file",
        help="Path to input file (.eml, .txt, or any text)",
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path (default: stdout)",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output",
    )
    args = parser.parse_args()

    text = read_file(args.file)
    iocs = extract_all(text)

    indent = 2 if args.pretty else None
    output = json.dumps(iocs, indent=indent)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Wrote IOCs to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
