"""Simple document agent: planning, retrieval, analysis, and summarization.

Educational local prototype without an LLM or web browsing.
"""
import re
from collections import Counter
from pathlib import Path
from documents_io import load_documents

STOPWORDS = {"avec", "dans", "pour", "des", "les", "une", "sur", "est", "que", "qui", "comment", "quel", "quelle", "quels", "quelles", "the", "and", "what", "how", "are", "documents", "document"}


def keywords(text: str) -> set[str]:
    return {word for word in re.findall(r"\b\w{3,}\b", text.lower()) if word not in STOPWORDS}


def split_passages(text: str, size: int = 600) -> list[str]:
    """Split text into short passages while preserving the original content."""
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    passages = []
    for paragraph in paragraphs:
        for start in range(0, len(paragraph), size):
            passages.append(paragraph[start:start + size])
    return passages


class DocumentAgent:
    def __init__(self, folder: Path):
        self.folder = folder

    def plan(self) -> list[str]:
        return ["Load documents", "Find relevant passages", "Rank results", "Compile extracts with source citations"]

    def run(self, question: str) -> str:
        if not question.strip():
            raise ValueError("The question cannot be empty.")
        documents = load_documents(self.folder)
        query_terms = keywords(question)
        matches = []
        for filename, content in documents:
            for index, passage in enumerate(split_passages(content), start=1):
                passage_terms = keywords(passage)
                score = len(query_terms & passage_terms)
                if score > 0:
                    matches.append((score, filename, index, passage))
        matches.sort(key=lambda item: (-item[0], item[1], item[2]))
        selected = matches[:5]

        lines = ["# Document Research Report", "", f"**Question:** {question}", "", "## Execution Plan"]
        lines.extend(f"- {step}" for step in self.plan())
        lines += ["", f"**Documents analyzed:** {len(documents)}", "", "## Results and Extractive Summary"]
        if not selected:
            lines += ["No relevant passages found. Check your keywords and documents."]
        else:
            lines += ["The excerpts below are ranked by keyword overlap with the question. They are not an LLM-generated summary.", ""]
            for score, filename, index, passage in selected:
                lines += [f"### Source: `{filename}` — passage {index}", f"*Relevance score: {score}*", "", f"> {passage.replace(chr(10), chr(10) + '> ')}", ""]
            word_counts = Counter(word for _, _, _, text in selected for word in keywords(text))
            terms = ", ".join(term for term, _ in word_counts.most_common(8))
            lines += ["## Frequent Topics", terms or "No topics identified."]
        lines += ["", "## Limitations", "Local keyword retrieval only; no web search, advanced autonomous reasoning, or language-model text generation."]
        return "\n".join(lines) + "\n"
