#!/usr/bin/env bash
# Quick humanize - add author to articles missing it
cd /home/wahyu/.hermes/workspace/maswahyu-blog
for f in src/content/blog/*.md; do
  if ! head -10 "$f" | grep -q "^author:"; then
    # Add author to frontmatter
    sed -i 's/^heroImage:/author: Mas Wahyu\nauthorTitle: Founder & CEO Qawwa Technology Indonesia\nupdatedDate: 2026-07-14\nheroImage:/' "$f"
    # Add opening "Ditulis oleh" after title
    sed -i '7a\n\n*Ditulis oleh Mas Wahyu, Founder Qawwa Technology Indonesia*\n' "$f"
    echo "Updated: $f"
  fi
done
npm run build && git add -A && git commit -m "docs(author): add author to remaining articles" && git push