---
name: md-visual
description: Use whenever creating, saving, updating, appending to, or visually reorganizing Markdown (.md) notes, research, decisions, project documents, plans, or summaries. Turn long explanations into legible structure, cards, tables, and Mermaid only when useful. Apply the frozen V1.6 Obsidian design system, preserve source meaning, and validate UTF-8 filenames and Markdown export integrity.
---

# md-visual V1.6

> **Status:** Frozen functional and visual baseline, 2026-10-28. This is the only active baseline; do not mix older V1.0–V1.5 designs or translation experiments into the output.

## 1. Responsibilities and boundaries

- Improve **how Markdown reads**; do not change product conclusions, decision status, evidence, approval boundaries, or business semantics.
- Select visual representation based on content shape. Favor scanning and decision clarity over decoration.
- Preserve a single editable Markdown source. An Obsidian CSS snippet affects reading only; it does not become content data.
- Honor the project's independently defined file-naming convention. **Do not invent or redefine project naming rules in this skill.** This skill only preserves the name given to its exporter and checks export correctness.
- For publication to platforms other than Obsidian, produce a separate on-demand adapted artifact; do not overwrite the canonical Markdown.

## 2. Visual selection

| Content | Default representation |
|---|---|
| Short single idea | Short paragraph |
| Key conclusion, constraint, warning, unresolved question | Brief callout |
| Parallel explanations or enumerated semantic principles | Grouped cards (`wd-group`) |
| Exact repeated fields, feature comparisons, data contracts | Compact Markdown table |
| Steps or conditional user paths | Mermaid `flowchart` |
| System layers and interactions | Mermaid `flowchart` with selective `subgraph` |
| Actor messages over time | Mermaid `sequenceDiagram` |
| Branching ideas | Mermaid `mindmap` |
| Phases and milestones | Mermaid `timeline` |

- Do not convert tables to cards when users must compare columns precisely. For narrow readers, convert long descriptive records into grouped field cards.
- Keep diagrams purposeful: normally no more than 3 per file, under roughly 12 nodes each; when preserving an existing formal document, retain all evidence-bearing diagrams even if there are more.
- Put diagrams next to their explanatory text and add a one-sentence caption.
- Avoid crossing return arrows when a branch table can preserve the exact cycle semantics more legibly. Never silently remove transitions.

## 3. Reading structure

1. Start with a **1–3 line reading summary** that clearly distinguishes approved decisions from suggestions and unverified claims.
2. For long documents, add a short framework-oriented overview and an in-file **chapter navigation** table. Use verified `[[#Exact Heading|Label]]` Obsidian links; preserve non-Obsidian fallback by keeping headings searchable.
3. Keep prose sections compact. Turn runs longer than roughly five lines into a diagram, comparison table, grouped card, or list when the structure genuinely helps.
4. Use one visual unit per semantic group. Avoid stacking many individual oversized boxes.
5. Update existing summaries and affected visuals during revision instead of appending duplicate summaries and diagrams.
6. Leave code-heavy reference documents and raw payloads principally intact; add only a compact summary and navigation if useful.

## 4. Frozen V1.6 appearance

**Obsidian CSS:** Use the bundled `assets/md-visual-v1.6-complete.css` as the sole enabled complete style snippet. Do not require V1.3/V1.4/V1.5 supplemental snippets.

### Cards and tables

- Neutral grayscale palette. No strong blue title bars, decorative pencil icons, or heavy shadows.
- Card: background `#F7F8F9`; heading background `#F1F2F4`; border `#D9DDE2`; title `#343B45`.
- Card radius: `7px`. One outer card for grouped parallel items; internal hairline separators `#E4E7EB`.
- Tables: compact, readable, pale-neutral headers and light cell rules. Retain precise comparisons.
- Obsidian document frontmatter should contain `cssclasses: [wd-visual-v14]` (the frozen complete V1.6 CSS also supports `wd-visual` for older notes). This class name is a renderer selector, **not the document version**.

### Mermaid nodes

- Rectangular node corner radius: `3px`; no stroke/outline; colored fills at `55%` opacity.
- Connector lines: quiet gray, approximately `1.2px`.
- Semantic colors: input `#4C8FD7`; AI reasoning `#9670CB`; retrieval/data `#31A89B`; confirmed result `#67AE72`; decision `#DAA044`; otherwise neutral `#A6B0BC`.
- Decision diamonds retain their geometry; do not force a rectangular corner radius onto them.
- Ensure adequate text contrast, legible edge labels, and no clipping in the target reader.
- Use ASCII Mermaid node IDs and quote labels containing spaces, Chinese, or punctuation. Keep Markdown syntax out of node labels.

## 5. Export reliability

Run these checks before handing over a Markdown file:

1. Save UTF-8 text with literal Unicode filename characters exactly as supplied by the project naming convention.
2. Never run URL escaping on the filesystem basename. `%E6...` sequences are URL encodings, **not** valid replacements for the intended Chinese filename.
3. Check the actual on-disk basename, not just the download link display label. If it contains `%[0-9A-Fa-f]{2}` in place of user-intended Unicode, stop and fix.
4. Verify nonempty file, valid frontmatter, section headings, Mermaid fences, and intended CSS class.
5. Check Obsidian `[[links]]` and target headings where applicable; warn about unresolved references rather than fabricating targets.
6. Preserve the original Markdown and avoid overwriting unrelated files. Use a uniquely named test deliverable when validating a new exporter.
7. When download delivery could percent-encode the filename, offer an ASCII-named ZIP containing the original Unicode-named Markdown and the single complete CSS file; verify the ZIP listing before delivery.
8. Distinguish file content version (e.g., product `v2.0`) from this skill's visual version (`V1.6`).

## 6. Acceptance checklist

- The original facts and decision status remain unchanged.
- A skimming reader sees the goal, sections, and actionable relationships quickly.
- Grouped cards look like a unified neutral panel, not separate blue alerts.
- Tables remain readable at ordinary Obsidian pane width.
- Flowcharts have no node outlines, use the frozen 3px/55% style, and preserve business paths.
- Output opens in Obsidian with readable Chinese **filename**, not `%E6...` percent escapes.
- A tested fallback exists if the destination renderer does not support Mermaid or Obsidian CSS.

## 7. Bundled assets

`assets/md-visual-v1.6-complete.css` is the exact frozen styling asset. Keep it bundled with the Skill so future users do not reconstruct styling from prose.
