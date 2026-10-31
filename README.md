# Intelligent Document Research and Analysis Agent — Agentic AI

**Author: Yassir EL Haj Tirari**

## Overview

This educational project is inspired by **Agentic AI**. It is a Python-based assistant that organizes document retrieval, analysis, and **extractive summarization** for local files. It reads `.txt`, `.md`, and text-based `.pdf` files, identifies passages relevant to a question, and generates a Markdown report citing the source documents.

> **Current status: prototype without an LLM.** It does not browse the web or use a language model. Its summary consists of selected passages and common topics, not an AI-generated narrative summary.

## Features

- Explicit planning of document-processing steps
- Loading TXT, Markdown, and text-based PDF files
- Keyword-based passage retrieval
- Ranking results and identifying sources
- Automatically generating a `report.md` file

## Project Structure

```text
agentic-document-ai/
├── main.py                  # Command-line entry point
├── agent.py                 # Planning, retrieval, ranking, report generation
├── documents_io.py          # Document loading
├── documents/
│   └── example.txt          # Sample document
├── requirements.txt         # Python dependencies
├── .gitignore
└── README.md
```

## Installation

Requires Python 3.10 or newer.

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\activate
```

On macOS / Linux:

```bash
source .venv/bin/activate
```

Install dependencies (including PDF support):

```bash
pip install -r requirements.txt
```

## Usage

Add your documents to `documents/` and run:

```bash
python main.py "How does a document analysis agent work?"
```

To specify a different document directory and output filename:

```bash
python main.py "What is agentic AI?" --documents my_documents --output results.md
```

The program prints the results and saves a Markdown report to `report.md` by default.

## Limitations and Future Improvements

- Relevance is based on shared keywords, not semantic search.
- Scanned PDFs without selectable text require OCR, which is not implemented.
- Adding an LLM and external search tools could enable generated summaries, tool use, and more advanced agentic decision-making.

## Author

**Yassir EL Haj Tirari**
