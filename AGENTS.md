# Agent Definitions (Maswahyu Blog Project)

## Agents

| Agent | Role | Toolsets | Template |
|-------|------|----------|----------|
| Dev | Web Developer | terminal, file, web | agents/dev.md |
| Researcher | Content Researcher | terminal, file, web | agents/researcher.md |
| Writer | Content Strategist | terminal, file, web | agents/writer.md |
| Metrics | Data Analyst | web, terminal | agents/metrics.md |

## Pipeline

```
Research Brief → Writer → Humanize → Hero Image → Build → Push → Deploy
     ↑
  Researcher
```

## Project Info
- Blog: Astro + Cloudflare Pages
- Domain: maswahyu.biz.id
- Repo: https://github.com/PseudoPort/maswahyu-blog
- Agents: ~/.hermes/workspace/agents/*.md (detailed templates)
- Tasks: ~/.hermes/workspace/tasks/queue.md
- Content Plans: ~/.hermes/workspace/research/content-plan-*.md
