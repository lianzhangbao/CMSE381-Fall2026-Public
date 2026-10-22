#!/usr/bin/env bash
# Build the site: render every slide deck, build the book, copy the slide HTML in.
set -e
cd "$(dirname "$0")"
for q in Lectures/*/Fall2026/*.qmd; do quarto render "$q" --to revealjs; done
jupyter-book build .
# copy rendered slides (and their *_files folders) into the built site
( cd . && find Lectures -name "*.html" -o -type d -name "*_files" | grep -v "^Lectures$" ) | while read p; do
  mkdir -p "_build/html/$(dirname "$p")"; cp -r "$p" "_build/html/$(dirname "$p")/"
done
echo "Done. Open _build/html/index.html"
