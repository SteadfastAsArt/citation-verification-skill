#!/usr/bin/env python3
"""
Extract citations from a document (PDF, Markdown, or text file).
Outputs structured citation data for verification.
"""

import re
import sys
from pathlib import Path
from typing import List, Dict

def extract_citations_from_text(text: str) -> List[Dict[str, str]]:
    """Extract citations from text using common patterns."""
    citations = []

    # Pattern 1: Author et al. (Year). "Title." Journal, Volume(Issue), Pages.
    pattern1 = r'([A-Z][a-z]+(?:\s+et\s+al\.)?)\s+\((\d{4})\)\.\s+"([^"]+)"\.\s+([^,]+),\s+(\d+)\((\d+)\),\s+([\d-]+)'

    # Pattern 2: Author, A. (Year). Title. Journal, Volume, Pages.
    pattern2 = r'([A-Z][a-z]+,\s+[A-Z]\.(?:\s+[A-Z]\.)?)\s+\((\d{4})\)\.\s+([^.]+)\.\s+([^,]+),\s+(\d+),\s+([\d-]+)'

    # Pattern 3: Author (Year) Title. Journal Volume:Pages
    pattern3 = r'([A-Z][a-z]+(?:\s+et\s+al\.)?)\s+\((\d{4})\)\s+([^.]+)\.\s+([^\d]+)\s+(\d+):(\d+-\d+)'

    # Pattern 4: arXiv citations
    pattern4 = r'([A-Z][a-z]+(?:\s+et\s+al\.)?)[,\s]+\((\d{4})\)[,\s]+"([^"]+)"[,\s]+arXiv:(\d+\.\d+)'

    for match in re.finditer(pattern1, text):
        citations.append({
            'authors': match.group(1),
            'year': match.group(2),
            'title': match.group(3),
            'journal': match.group(4),
            'volume': match.group(5),
            'issue': match.group(6),
            'pages': match.group(7),
            'raw': match.group(0)
        })

    for match in re.finditer(pattern2, text):
        citations.append({
            'authors': match.group(1),
            'year': match.group(2),
            'title': match.group(3),
            'journal': match.group(4),
            'volume': match.group(5),
            'pages': match.group(6),
            'raw': match.group(0)
        })

    for match in re.finditer(pattern3, text):
        citations.append({
            'authors': match.group(1),
            'year': match.group(2),
            'title': match.group(3),
            'journal': match.group(4),
            'volume': match.group(5),
            'pages': match.group(6),
            'raw': match.group(0)
        })

    for match in re.finditer(pattern4, text):
        citations.append({
            'authors': match.group(1),
            'year': match.group(2),
            'title': match.group(3),
            'arxiv': match.group(4),
            'raw': match.group(0)
        })

    return citations

def extract_from_pdf(pdf_path: Path) -> str:
    """Extract text from PDF using paper-ladder."""
    try:
        from paper_ladder.extractors import PDFExtractor
        import asyncio

        async def extract():
            extractor = PDFExtractor()
            content = await extractor.extract(str(pdf_path))
            return content.markdown

        return asyncio.run(extract())
    except ImportError:
        print("⚠️  paper-ladder not installed. Install with:")
        print("   pip install git+https://github.com/SteadfastAsArt/paper-ladder.git")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: extract_citations.py <file.pdf|file.md|file.txt>")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        sys.exit(1)

    # Extract text based on file type
    if file_path.suffix.lower() == '.pdf':
        print(f"📄 Extracting text from PDF: {file_path}")
        text = extract_from_pdf(file_path)
    else:
        print(f"📄 Reading text file: {file_path}")
        text = file_path.read_text(encoding='utf-8')

    # Extract citations
    print("🔍 Extracting citations...")
    citations = extract_citations_from_text(text)

    if not citations:
        print("⚠️  No citations found using standard patterns.")
        print("💡 Tip: Copy the references section and paste directly to Claude Code")
        sys.exit(0)

    print(f"\n✅ Found {len(citations)} citations:\n")

    # Output formatted for Claude Code
    for i, cite in enumerate(citations, 1):
        if 'arxiv' in cite:
            print(f"{i}. {cite['authors']} ({cite['year']}). \"{cite['title']}.\" arXiv:{cite['arxiv']}")
        else:
            journal_info = cite.get('journal', '')
            volume_info = f", {cite.get('volume', '')}" if cite.get('volume') else ""
            issue_info = f"({cite.get('issue', '')})" if cite.get('issue') else ""
            pages_info = f", {cite.get('pages', '')}" if cite.get('pages') else ""

            print(f"{i}. {cite['authors']} ({cite['year']}). \"{cite['title']}.\" {journal_info}{volume_info}{issue_info}{pages_info}")

    print("\n📋 Copy the above citations and ask Claude Code:")
    print("   'Verify these citations'")

if __name__ == '__main__':
    main()
