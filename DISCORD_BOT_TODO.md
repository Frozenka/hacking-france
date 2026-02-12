# Bot Discord Hacking France – Plan et TODO

> **Site** (racine du repo) : build, writeups.json, annonces webhook — déployé comme site web.  
> **Bot** (dossier `BOT/`) : code du bot Discord — déployé sur le **VPS** uniquement, pas sur le site.

---

## Intégration site (ce qui est déployé avec le site)

| Élément | Rôle |
|--------|------|
| **`scripts/generate-writeups.js`** | Génère `public/writeups.json` à chaque build. |
| **`pnpm build`** | Lance le script writeups puis `astro build` → le site expose `/writeups.json`. |
| **`.github/workflows/announce-discord.yml`** | À chaque push sur `main` qui modifie `src/content/docs/`, envoie un message Discord via webhook. Configurer le secret `DISCORD_WEBHOOK_ANNOUNCE`. |

Le dossier **`BOT/`** ne doit pas être inclus dans le déploiement du site (il n’est pas utilisé par Astro).

---

## Bot (déployé sur le VPS)

Tout le code du bot est dans **`BOT/`** :

- `BOT/package.json`, `BOT/src/index.js`, etc.
- Déployer uniquement le contenu de `BOT/` sur le VPS (ou cloner le repo et lancer depuis `BOT/`).
- Le bot récupère les writeups depuis `https://hacking-france.fr/writeups.json` (automatique).
- Voir **`BOT/README.md`** pour l’installation et le déploiement (systemd, pm2, etc.).

Commandes : `/writeup`, `/explorer`, `/events`, `/site`.

---

## Suite éventuelle

- Événements Discord → site (bot écoute les Scheduled Events, met à jour un JSON ou une API).
- Autocomplétion pour `/writeup`, rappels avant événements.

---

## Références

- Site : `https://hacking-france.fr`
- Writeups (pour le bot) : `https://hacking-france.fr/writeups.json`
- Discord : `https://discord.com/invite/3NnqxT6enc`
