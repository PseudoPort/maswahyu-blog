# maswahyu-blog — Project Context

Personal branding blog by Mas Wahyu (Qawwa Technology Indonesia).

## Tech Stack

- **Framework:** Astro (static site generator)
- **Hosting:** Cloudflare Pages
- **Domain:** maswahyu.biz.id
- **Repo:** https://github.com/PseudoPort/maswahyu-blog
- **Deploy:** Auto on push to main (git push origin main)

## Content Rules

- Niche: Digital Marketing, AI & Automation untuk UKM Indonesia
- Tone: Professional tapi approachable, no BS
- Language: Bahasa Indonesia

## Image Rules (STRICT)

- Style: stickman, flat design, minimal, simple cartoon
- Colors: warm orange tones, clean background
- FORBIDDEN: face details, eyes/nose/mouth, realistic, women
- Negative prompt: "realistic, photorealistic, face details, woman, portrait, eyes, nose, mouth"
- Generate with: Runware AI direct API call (see `runware-ai` skill). Use Python `requests` to POST to `https://api.runware.ai/v1` with `taskType: imageInference`. Bash scripts at `runware-image/scripts/` do NOT exist.

## Key Commands

- npm run dev — Local dev server
- npm run build — Production build
- npm run preview — Preview production build

## Build & Deploy Rules (CRITICAL)

**ALWAYS verify build passes locally BEFORE pushing:**
1. Run `npm run build`
2. Confirm output shows `✓ Completed` and `Complete!` (0 errors)
3. Only then: `git add -A && git commit && git push`

**Never push without local build verification.** Cloudflare Pages build will fail otherwise.

## File Structure

- src/content/blog/ — Blog posts (Markdown)
- src/assets/hero-*.jpg — Hero images
- src/pages/ — Page templates
- public/ — Static assets

## Agents

When delegating via delegate_task(), use these context templates.

### Writer — Content Strategist

Role: Write SEO articles for maswahyu-blog. Bahasa Indonesia.

Workflow:
1. RESEARCH — duckduckgo-search skill
2. DRAFT — blog-master skill
3. HUMANIZE — humanizer skill
4. SEO CHECK — keywords, meta description (max 155 chars)
5. HERO IMAGE — Runware AI (stickman/flat, warm orange, NO faces/women)
6. PUBLISH — git commit + push → Cloudflare Pages auto-deploy

Report: WORD_COUNT, SEO_KEYWORD, PREVIEW, SOURCES_CITED, STATUS, NEXT
Toolsets: terminal, file, web

### Dev — Web Developer & DevOps

Role: Handle technical tasks for maswahyu-blog (Astro + Cloudflare Pages).

Responsibilities: development, deployment, DNS/domains/SSL, bug fixes, git operations.

Report: TASK, STATUS (COMPLETED/FAILED), OUTPUT, LINK, NEXT
Toolsets: terminal, file, web

### Researcher — Content Researcher

Role: Research trending topics, competitor content, data points in Digital Marketing & AI for UKM Indonesia. Output: research brief in Bahasa Indonesia.

Report: TOPIC, BRIEF, DATA_POINTS, SOURCES, ANGLE, STATUS
Toolsets: terminal, file, web

### Metrics — Data Analyst

Role: Analyze blog performance, SEO audit, track publishing schedule.

Report: METRIC, VALUE, TREND, INSIGHT, ACTION
Toolsets: terminal, file, web
