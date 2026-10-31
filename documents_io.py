"""Read local documents."""
from pathlib import Path


def load_documents(folder: Path) -> list[tuple[str, str]]:
    """Return a list of (filename, text) pairs."""
    if not folder.is_dir():
        raise FileNotFoundError(f"Directory not found: {folder}")

    documents = []
    for path in sorted(folder.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() in {".txt", ".md"}:
            content = path.read_text(encoding="utf-8")
        elif path.suffix.lower() == ".pdf":
            try:
                from pypdf import PdfReader
            except ImportError as exc:
                raise RuntimeError("Install the PDF dependency: pip install -r requirements.txt") from exc
            content = "\n".join(page.extract_text() or "" for page in PdfReader(str(path)).pages)
        else:
            continue
        if content.strip():
            documents.append((str(path.relative_to(folder)), content))
    return documents
