#!/usr/bin/env python3
"""Search public-safe PDF evidence cards."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def iter_cards(path: Path):
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def load_module_indexes(path: Path, module: str | None) -> list[dict]:
    if path.is_file():
        return [json.loads(path.read_text(encoding="utf-8"))]
    if not path.exists():
        return []
    if module:
        module_path = path / f"{module}.json"
        return [json.loads(module_path.read_text(encoding="utf-8"))] if module_path.exists() else []
    indexes = []
    for item in sorted(path.glob("*.json")):
        if item.name != "index.json":
            indexes.append(json.loads(item.read_text(encoding="utf-8")))
    return indexes


def load_term_hits(path: Path, terms: list[str], module: str | None) -> dict[str, list[dict]]:
    hits = {term: [] for term in terms}
    for index in load_module_indexes(path, module):
        for term in terms:
            hits[term].extend(index.get(term, {}).get("citations", []))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description="Search references/pdf-evidence/evidence-cards.jsonl")
    parser.add_argument("terms", nargs="+", help="Chinese terms to search, e.g. 大青龙汤 荥穴")
    parser.add_argument("--evidence-dir", default="references/pdf-evidence", help="PDF evidence directory")
    parser.add_argument("--limit", type=int, default=10, help="Maximum rows to print")
    parser.add_argument("--module", help="Optional module index, e.g. shanghan, bencao, acupuncture")
    args = parser.parse_args()

    evidence_dir = Path(args.evidence_dir)
    cards_path = evidence_dir / "evidence-cards.jsonl"
    term_index_path = evidence_dir / "term-index"
    terms = [term.strip() for term in args.terms if term.strip()]
    term_hits = load_term_hits(term_index_path, terms, args.module)

    if len(terms) == 1 and term_hits.get(terms[0]):
        for hit in term_hits[terms[0]][: args.limit]:
            print(f"{hit['citation']} {hit['source_name']} page {hit['page']}")
            print(hit.get("snippet", ""))
            print()
        return 0

    shown = 0
    for card in iter_cards(cards_path):
        haystack = "\n".join(
            [
                card.get("source_name", ""),
                card.get("excerpt", ""),
                " ".join(card.get("terms", [])),
            ]
        )
        if all(term in haystack for term in terms):
            print(f"{card['citation']} {card['source_name']} {card['locator']}")
            snippets = []
            for term in terms:
                for hit in term_hits.get(term, []):
                    if hit.get("card_id") == card.get("card_id") and hit.get("snippet"):
                        snippets.append(hit["snippet"])
                        break
            print(" / ".join(snippets) if snippets else card["excerpt"])
            print()
            shown += 1
            if shown >= args.limit:
                break
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
