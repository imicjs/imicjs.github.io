# IMIC Laboratory English Website

English website for the Intelligent Medical Image Computing Laboratory at
Nanjing University of Information Science & Technology.

The site is built with [Hugo](https://gohugo.io/) and
[Hugoplate](https://github.com/zeon-studio/hugoplate). Its content was
translated and structured from the laboratory's Chinese website.

## Development

Requirements: Node.js 22+, Go 1.25+, and Hugo Extended 0.158+.

```bash
npm install
npm run dev
```

Build the production site with:

```bash
npm run build
```

## Content and images

- English content: `content/english/`
- Local content thumbnails: `assets/images/content/`
- Source metadata: `metadata/content.jsonl`
- Thumbnail provenance: `metadata/thumbnail-manifest.json`
- Migration script: `scripts/migrate_imic.py`

## Deployment

Pushes to `main` deploy automatically to GitHub Pages. Netlify uses the build
configuration in `netlify.toml`.
