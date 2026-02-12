import { getCollection } from 'astro:content'
import { OGImageRoute } from 'astro-og-canvas'

// Get all entries from the `docs` content collection.
const entries = await getCollection('docs')

// Map the entry array to an object with the page ID as key and the
// frontmatter data as value.
const pages = Object.fromEntries(entries.map(({ data, id }) => [id, { data }]))

export const { getStaticPaths, GET } = OGImageRoute({
  // Pass down the documentation pages.
  pages,
  // Define the name of the parameter used in the endpoint path, here `slug`
  // as the file is named `[...slug].ts`.
  param: 'slug',
  // Define a function called for each page to customize the generated image.
  getImageOptions: (_path, page: (typeof pages)[number]) => {
    return {
      title: page.data.title,
      description: page.data.description ?? 'Communauté francophone de cybersécurité — CTF, talks et entraide.',
      bgGradient: [[24, 24, 27]],
      border: { color: [35, 110, 172], width: 20 },
      padding: 120,
      logo: {
        path: './src/assets/newlogo.png',
        size: [120],
      },
    }
  },
})