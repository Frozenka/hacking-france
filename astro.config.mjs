import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightImageZoom from 'starlight-image-zoom';
import embeds from 'astro-embed/integration';
import mdx from '@astrojs/mdx';
import astroD2 from 'astro-d2';
import starlightHeadingBadges from 'starlight-heading-badges';

export default defineConfig({
  prefetch: {
    defaultStrategy: 'viewport'
  },
  site: 'https://hacking-france.fr',
  integrations: [
    starlight({
      credits: false,
      editLink: {
        baseUrl: 'https://github.com/frozenka/hacking-france/edit/main/',
      },
      expressiveCode: {
        themes: ['houston', 'catppuccin-latte'],
      },
      lastUpdated: true,
      favicon: '/favicon.ico',
      customCss: ['./src/styles/custom.css'],
      plugins: [starlightImageZoom(), starlightHeadingBadges()],
      title: 'Hacking France',
      components: {
        Head: "./src/components/starlight/Head.astro",
        Hero: './src/components/starlight/Hero.astro',
        Pagination: './src/components/starlight/Pagination.astro',
        PageSidebar: './src/components/starlight/PageSidebar.astro',
        Footer: './src/components/starlight/Footer.astro',
        ThemeSelect: './src/components/starlight/ThemeSelect.astro',
      },
      logo: {
        light: './src/assets/newlogo.png',
        dark: './src/assets/newlogo.png',
        replacesTitle: true
      },
      defaultLocale: 'root',
      sidebar: [
        {
          label: 'À propos',
          translations: { en: 'About' },
          link: 'about'
        },
        {
          label: 'La communauté',
          badge: { text: 'Nouveau', variant: 'note' },
          translations: {
            en: 'The Community'
          },
          link: 'community' },
        {
          label: 'Événements',
          translations: {
            en: 'Events'
          },
          collapsed: true,
          autogenerate: {
            directory: 'events',
            collapsed: true
          }
        },
        {
          label: 'Articles',
          translations: { en: 'Articles' },
          collapsed: false,
          items: [
            { label: 'Tutoriels', collapsed: true, autogenerate: { directory: 'articles', collapsed: true } },
            { label: 'Certifications', collapsed: true, autogenerate: { directory: 'certifications', collapsed: true } },
            { label: 'Cheat sheet & outils', collapsed: true, autogenerate: { directory: 'tools', collapsed: true } }
          ]
        },
        {
          label: 'Parcours & guides',
          translations: {
            en: 'Learning paths & guides'
          },
          collapsed: true,
          autogenerate: {
            directory: 'cybersecurity',
            collapsed: true
          }
        },
        {
          label: 'Writeups',
          translations: { en: 'Writeups' },
          collapsed: true,
          autogenerate: {
            directory: 'writeup',
            collapsed: true
          }
        },
        {
          label: 'Ressources',
          translations: {
            en: 'Resources'
          },
          collapsed: true,
          autogenerate: {
            directory: 'misc',
            collapsed: true
          }
        },
        { 
          label: 'Contribuer',
          badge: { text: 'Guide', variant: 'success' },
          translations: {
            en: 'Contribute'
          },
          link: 'contribute/' },
      ],
      locales: {
        root: {
          label: 'Français',
          lang: 'fr'
        },
        en: {
          label: 'English',
          lang: 'en'
        }
      },
      social: {
        discord: 'https://discord.com/invite/3NnqxT6enc',
        github: 'https://github.dev/Frozenka',
        linkedin: 'https://www.linkedin.com/company/hacking-france/'
      }
    }),
    embeds(),
    mdx(),
    astroD2({
      skipGeneration: true
    })
  ]
});
