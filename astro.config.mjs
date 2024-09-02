import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightImageZoom from 'starlight-image-zoom';
import embeds from 'astro-embed/integration';
import mdx from '@astrojs/mdx';
import astroD2 from 'astro-d2';

export default defineConfig({
  prefetch: {
    defaultStrategy: 'viewport'
  },
  site: 'https://hacking-france.fr',
  integrations: [
    starlight({
      credits: false,
      lastUpdated: true,
      favicon: '/favicon.ico',
      customCss: ['./src/styles/custom.css'],
      plugins: [starlightImageZoom()],
      title: 'Hacking France',
      components: {
        Head: "./src/components/starlight/Head.astro",
        Hero: './src/components/starlight/Hero.astro',
      },
      head: [
        {
          tag: 'meta',
          attrs: {
            property: 'og:image',
            content: '/hf.png'
          }
        },
        {
          tag: 'meta',
          attrs: {
            property: 'og:description',
            content: "La communauté Hacking France unit des passionnés de cybersécurité qui s'entraident sur tout sujets liés à l'informatique. Nous sommes actif sur Discord, et organisons des évènements réguliers."
          }
        },
        {
          tag: 'meta',
          attrs: {
            property: 'twitter:image',
            content: '/hf.png'
          }
        },
        {
          tag: 'meta',
          attrs: {
            property: 'og:description',
            content: "La communauté Hacking France unit des passionnés de cybersécurité qui s'entraident sur tout sujets liés à l'informatique. Nous sommes actif sur Discord, et organisons des évènements réguliers."
          }
        }
      ],
      logo: {
        src: './src/assets/hf.png',
      },
      defaultLocale: 'root',
      sidebar: [
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
          label: 'Offensif',
          translations: {
            en: 'Offensive'
          },
          autogenerate: {
            directory: 'offensive',
            collapsed: true
          }
        },
        {
          label: 'Defensif',
          translations: {
            en: 'Defensive'
          },
          collapsed: false,
          autogenerate: {
            directory: 'defensive',
            collapsed: true
          }
        },
        {
          label: 'Opsec',
          translations: {
            en: 'Opsec'
          },
          collapsed: false,
          autogenerate: {
            directory: 'opsec',
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
        }
      ],
      locales: {
        root: {
          label: '🇫🇷 Français',
          lang: 'fr'
        },
        en: {
          label: '🇬🇧 English',
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