#!/usr/bin/env python3
"""
Backfill author frontmatter to articles missing it.

Usage:
  python3 scripts/backfill-author.py --preview  # Show what would change
  python3 scripts/backfill-author.py --apply    # Apply changes
"""
import sys
import re
from pathlib import Path
from typing import List, Tuple

BLOG_DIR = Path(__file__).parent.parent / "src" / "content" / "blog"
AUTHOR = "Mas Wahyu"
AUTHOR_TITLE = "Founder & CEO Qawwa Technology Indonesia"


def parse_frontmatter(content: str) -> Tuple[dict, int, int]:
    """
    Parse frontmatter and return (fields_dict, start_pos, end_pos).
    Returns empty dict if no valid frontmatter.
    """
    if not content.startswith("---\n"):
        return {}, -1, -1
    
    # Find closing --- (must be on its own line)
    end_match = re.search(r"\n---\n", content[4:])
    if not end_match:
        return {}, -1, -1
    
    # Calculate positions
    # start_pos = 0 (beginning of "---\n")
    # end_pos = position AFTER closing "---\n"
    start_pos = 0
    end_pos = 4 + end_match.end()  # 4 ("---\n") + match end (after "\n---\n")
    
    # Extract frontmatter body (between opening and closing fences)
    fm_body = content[4:4 + end_match.start()]
    
    fields = {}
    for line in fm_body.split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            fields[key.strip()] = val.strip()
    
    return fields, start_pos, end_pos


def needs_author(fields: dict) -> bool:
    """Check if article needs author fields."""
    return "author" not in fields or "authorTitle" not in fields


def generate_patch(content: str, fields: dict, fm_start: int, fm_end: int) -> str:
    """
    Generate new frontmatter with author fields inserted.
    Preserves order: title, description, pubDate, updatedDate (if exists), heroImage, author, authorTitle
    """
    # Build new frontmatter in canonical order
    new_lines = ["---"]
    
    # Required fields first
    if "title" in fields:
        new_lines.append(f"title: {fields['title']}")
    if "description" in fields:
        new_lines.append(f"description: {fields['description']}")
    if "pubDate" in fields:
        new_lines.append(f"pubDate: {fields['pubDate']}")
    if "updatedDate" in fields:
        new_lines.append(f"updatedDate: {fields['updatedDate']}")
    if "heroImage" in fields:
        new_lines.append(f"heroImage: {fields['heroImage']}")
    
    # Add author fields
    new_lines.append(f"author: {AUTHOR}")
    new_lines.append(f"authorTitle: {AUTHOR_TITLE}")
    
    # Any other fields not explicitly handled
    known = {"title", "description", "pubDate", "updatedDate", "heroImage", "author", "authorTitle"}
    for key, val in fields.items():
        if key not in known:
            new_lines.append(f"{key}: {val}")
    
    new_lines.append("---")
    
    new_fm = "\n".join(new_lines) + "\n"
    return content[:fm_start] + new_fm + content[fm_end:]


def scan_articles() -> List[Tuple[Path, dict]]:
    """Scan blog dir and return articles needing author backfill."""
    articles_to_fix = []
    
    for md_file in sorted(BLOG_DIR.glob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        fields, fm_start, fm_end = parse_frontmatter(content)
        
        if fm_start == -1:
            print(f"⚠️  {md_file.name}: No valid frontmatter, skipping")
            continue
        
        if needs_author(fields):
            articles_to_fix.append((md_file, fields))
    
    return articles_to_fix


def preview_changes(articles: List[Tuple[Path, dict]]) -> None:
    """Show what would be changed."""
    print(f"\n📋 Found {len(articles)} articles needing author frontmatter:\n")
    
    for md_file, fields in articles[:20]:  # Show first 20
        title = fields.get("title", "(no title)")
        has_author = "author" in fields
        has_title = "authorTitle" in fields
        
        status = "✓ has author" if has_author else "✗ missing author"
        status += ", ✓ has authorTitle" if has_title else ", ✗ missing authorTitle"
        
        print(f"  {md_file.name}")
        print(f"    Title: {title}")
        print(f"    Status: {status}")
        print()
    
    if len(articles) > 20:
        print(f"  ... and {len(articles) - 20} more\n")
    
    print(f"Will add to all {len(articles)} articles:")
    print(f"  author: {AUTHOR}")
    print(f"  authorTitle: {AUTHOR_TITLE}\n")


def apply_changes(articles: List[Tuple[Path, dict]]) -> None:
    """Apply author frontmatter to all articles."""
    success_count = 0
    error_count = 0
    
    for md_file, fields in articles:
        try:
            content = md_file.read_text(encoding="utf-8")
            _, fm_start, fm_end = parse_frontmatter(content)
            
            new_content = generate_patch(content, fields, fm_start, fm_end)
            md_file.write_text(new_content, encoding="utf-8")
            
            success_count += 1
            print(f"✓ {md_file.name}")
        except Exception as e:
            error_count += 1
            print(f"✗ {md_file.name}: {e}")
    
    print(f"\n✅ Successfully updated {success_count} articles")
    if error_count > 0:
        print(f"❌ Failed to update {error_count} articles")


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("--preview", "--apply"):
        print(__doc__)
        sys.exit(1)
    
    mode = sys.argv[1]
    
    if not BLOG_DIR.exists():
        print(f"❌ Blog directory not found: {BLOG_DIR}")
        sys.exit(1)
    
    articles = scan_articles()
    
    if not articles:
        print("✅ All articles already have author frontmatter!")
        sys.exit(0)
    
    if mode == "--preview":
        preview_changes(articles)
        print("Run with --apply to make changes")
    else:
        preview_changes(articles)
        print("Applying changes...\n")
        apply_changes(articles)


if __name__ == "__main__":
    main()
