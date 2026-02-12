/**
 * Génère public/writeups.json à partir des MDX dans src/content/docs/writeup/.
 * Utilisé par le site (optionnel) et par le bot Discord pour la commande /writeup.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, '..');
const contentDir = path.join(root, 'src', 'content', 'docs', 'writeup');
const outPath = path.join(root, 'public', 'writeups.json');

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

function walk(dir, base = '') {
  const entries = [];
  const items = fs.readdirSync(dir, { withFileTypes: true });
  for (const item of items) {
    const rel = path.join(base, item.name);
    if (item.isDirectory()) {
      entries.push(...walk(path.join(dir, item.name), rel));
    } else if (item.isFile() && item.name.endsWith('.mdx') && !item.name.includes('Recherche')) {
      const fullPath = path.join(dir, item.name);
      const content = fs.readFileSync(fullPath, 'utf-8');
      const title = extractTitle(content);
      const slug = rel.replace(/\.mdx$/, '').replace(/\\/g, '/');
      const stat = fs.statSync(fullPath);
      entries.push({
        slug: 'writeup/' + slug,
        title: title || slug,
        platform: platformLabel(slug.toLowerCase()),
        updated: stat.mtime.toISOString(),
      });
    }
  }
  return entries;
}

const writeups = walk(contentDir)
  .sort((a, b) => (b.updated || '').localeCompare(a.updated || ''));

fs.mkdirSync(path.dirname(outPath), { recursive: true });
fs.writeFileSync(outPath, JSON.stringify(writeups, null, 2), 'utf-8');
console.log(`Écrit ${writeups.length} writeups dans ${outPath}`);

// Expose les contributeurs (GitHub) pour le bot /contributeurs
const cardsPath = path.join(root, 'src', 'assets', 'cards.json');
const contributorsPath = path.join(root, 'public', 'contributors.json');
if (fs.existsSync(cardsPath)) {
  const cards = JSON.parse(fs.readFileSync(cardsPath, 'utf-8'));
  const list = (cards.data || cards) || [];
  fs.writeFileSync(contributorsPath, JSON.stringify(list, null, 2), 'utf-8');
  console.log(`Écrit ${list.length} contributeurs dans ${contributorsPath}`);
}
