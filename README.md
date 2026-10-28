# md-visual V1.6

A reusable Agent Skill for making Markdown documents easier to navigate and read, with a frozen Obsidian visual style.

**功能：** 摘要与章节导航、内容形态选择、灰阶说明卡片、表格、Mermaid 图示，以及中文文件名 UTF-8 导出检查。

**设计原则：** 原文语义优先。不会改变业务结论、审批状态、证据或数据契约；项目文件命名规范应独立管理。V1.6 是目前唯一的视觉基线。

## Install in Codex (personal)

Copy `skills/md-visual/` into `~/.agents/skills/md-visual/` on your machine (keep both `SKILL.md` and `assets/`). Restart Codex if it doesn't appear immediately.

For project-only usage, put the same folder under `.agents/skills/md-visual/` in the target project.

You may also ask Codex `$skill-installer` to install from the GitHub folder URL after this repository is published.

## Obsidian appearance

1. Copy `skills/md-visual/assets/md-visual-v1.6-complete.css` to your Vault's `.obsidian/snippets/` directory.
2. In Obsidian, go to **Settings → Appearance → CSS snippets**, refresh and enable it.
3. Add the following frontmatter to notes produced using the V1.6 design:

```yaml
---
cssclasses:
  - wd-visual-v14
---
```

The selector `wd-visual-v14` is a legacy renderer class, **not** the skill version. The CSS also supports `wd-visual`. Disable conflicting older snippets.

## Sample

See [`examples/example.md`](examples/example.md) for a small public example. Its Mermaid diagram should render in compatible readers; custom card styling requires the CSS snippet in Obsidian.

## Limitations

- CSS appearance is Obsidian-specific. Other Markdown renderers may show the card callouts as plain quotes.
- Mermaid rendering depends on the host. Do not expect a Feishu import to render Mermaid automatically.
- File naming rules are external; this Skill validates that an existing intended Unicode filename survives export.
- A Skill is instructions plus resources; it does not automatically deploy CSS to someone else's Obsidian Vault.

## License

MIT; see [LICENSE](LICENSE).
