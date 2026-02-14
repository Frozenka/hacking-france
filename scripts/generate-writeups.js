/**
 * Génère public/articles.json (tous les articles avec catégorie, auteur, etc.)
 * et public/writeups.json (sous-ensemble writeups pour le bot et la page d'accueil).
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, '..');
const docsDir = path.join(root, 'src', 'content', 'docs');

const platformLabel = (slug) => {
  if (slug.includes('vulnlab')) return 'VulnLab';
  if (slug.includes('hackthebox')) return 'HackTheBox';
  if (slug.includes('tryhackme')) return 'TryHackMe';
  if (slug.includes('goad')) return 'GOAD';
  return 'Writeup';
};

function extractTitle(content) {
  const match = content.match(/^---\s*\n([\s\S]*?)\n---/);
  if (!match) return null;
  const titleLine = match[1].match(/title:\s*(.+)/m);
  return titleLine ? titleLine[1].trim().replace(/^['"]|['"]$/g, '') : null;
}

function extractFrontmatterField(content, fieldName) {
  const match = content.match(/^---\s*\n([\s\S]*?)\n---/);
  if (!match) return null;
  const line = match[1].match(new RegExp(`^${fieldName}:\\s*(.+)$`, 'm'));
  return line ? line[1].trim().replace(/^['"]|['"]$/g, '') : null;
}

function walk(dir, base = '') {
  const entries = [];
  const items = fs.readdirSync(dir, { withFileTypes: true });
  for (const item of items) {
    const rel = path.join(base, item.name);
    if (item.isDirectory()) {
      entries.push(...walk(path.join(dir, item.name), rel));
    } else if (item.isFile() && item.name.endsWith('.mdx')) {
      if (item.name === '404.mdx' || item.name.includes('Recherche')) continue;
      const fullPath = path.join(dir, item.name);
      const content = fs.readFileSync(fullPath, 'utf-8');
      const title = extractTitle(content);
      const slug = rel.replace(/\.mdx$/, '').replace(/\\/g, '/');
      const category = slug ? slug.split('/')[0] : path.basename(rel, '.mdx');
      const stat = fs.statSync(fullPath);
      const author = extractFrontmatterField(content, 'author') || null;
      const authorGitHub = extractFrontmatterField(content, 'authorGitHub') || extractFrontmatterField(content, 'author_github') || extractFrontmatterField(content, 'github') || null;
      const author_github_url = authorGitHub ? `https://github.com/${authorGitHub.replace(/^@/, '')}` : null;
      const platform = category === 'writeup' ? platformLabel(slug.toLowerCase()) : null;
      entries.push({
        slug,
        title: title || slug,
        category,
        platform,
        updated: stat.mtime.toISOString(),
        author,
        author_github_url,
      });
    }
  }
  return entries;
}

const allArticles = walk(docsDir)
  .sort((a, b) => (b.updated || '').localeCompare(a.updated || ''));

const writeups = allArticles
  .filter((a) => a.category === 'writeup')
  .map(({ slug, title, platform, updated, author, author_github_url }) => ({
    slug,
    title,
    platform,
    updated,
    author,
    author_github_url,
  }));

fs.mkdirSync(path.join(root, 'public'), { recursive: true });
fs.writeFileSync(path.join(root, 'public', 'articles.json'), JSON.stringify(allArticles, null, 2), 'utf-8');
console.log(`Écrit ${allArticles.length} articles dans public/articles.json`);

fs.writeFileSync(path.join(root, 'public', 'writeups.json'), JSON.stringify(writeups, null, 2), 'utf-8');
console.log(`Écrit ${writeups.length} writeups dans public/writeups.json`);

// Contributeurs (pour le bot)
const cardsPath = path.join(root, 'src', 'assets', 'cards.json');
const contributorsPath = path.join(root, 'public', 'contributors.json');
if (fs.existsSync(cardsPath)) {
  const cards = JSON.parse(fs.readFileSync(cardsPath, 'utf-8'));
  const list = (cards.data || cards) || [];
  fs.writeFileSync(contributorsPath, JSON.stringify(list, null, 2), 'utf-8');
  console.log(`Écrit ${list.length} contributeurs dans ${contributorsPath}`);
}
