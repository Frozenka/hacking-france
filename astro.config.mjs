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
      },
      logo: {
        light: './src/assets/hfwhite.png',
        dark: './src/assets/hfdark.png'
      },
      defaultLocale: 'root',
      sidebar: [
        { 
          label: 'La communauté', 
          translations: {
            en: 'The Community'
          },
          link: 'community/community' },
        {
          label: 'Événements',
          translations: {
            en: 'Events'
          },
          collapsed: false,
          autogenerate: {
            directory: 'events',
            collapsed: true
          }
        },
        {
          label: 'Certifications',
          translations: {
            en: 'Certifications'
          },
          collapsed: false,
          autogenerate: {
            directory: 'certifications',
            collapsed: true
          }
        },
        {
          label: 'Cybersécurité',
          translations: {
            en: 'Cybersecurity'
          },
          autogenerate: {
            directory: 'cybersecurity',
            collapsed: true
          }
        },
        {
          label: 'Writeup',
          translations: {
            en: 'Writeup'
          },
          collapsed: true,
          autogenerate: {
            directory: 'writeup',
            collapsed: true
          }
        },
        {
          label: 'Outils',
          translations: {
            en: 'Tools'
          },
          collapsed: false,
          autogenerate: {
            directory: 'tools',
            collapsed: true
          }
        },
                {
          label: 'Autre',
          translations: {
            en: 'Misc'
          },
          collapsed: false,
          autogenerate: {
            directory: 'misc',
            collapsed: true
          }
        },
        { 
          label: 'Contribuer', 
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
        discord: 'https://discord.gg/TgM4S5KqR8',
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
