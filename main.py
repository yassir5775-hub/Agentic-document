"""Command-line entry point for the document analysis assistant."""
import argparse
from pathlib import Path
from agent import DocumentAgent


def main():
    parser = argparse.ArgumentParser(description="Document research and analysis agent")
    parser.add_argument("question", help="Question to ask about the documents")
    parser.add_argument("--documents", default="documents", help="Document directory (.txt, .md, .pdf)")
    parser.add_argument("--output", default="report.md", help="Path for the generated report")
    args = parser.parse_args()

    agent = DocumentAgent(Path(args.documents))
    report = agent.run(args.question)
    Path(args.output).write_text(report, encoding="utf-8")
    print(report)
    print(f"\nReport saved: {args.output}")


if __name__ == "__main__":
    main()
