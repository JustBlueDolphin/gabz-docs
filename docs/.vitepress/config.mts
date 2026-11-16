import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Gabz Docs',
  description: 'Documentation for the Gabz FiveM server setup',
  base: '/gabz-docs/', // must match the GitHub repo name
  cleanUrls: true,
  lastUpdated: true,
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Guide', link: '/guide/getting-started' }
    ],
    sidebar: [
      {
        text: 'Guide',
        items: [
          { text: 'Getting Started', link: '/guide/getting-started' },
          { text: 'Installation', link: '/guide/installation' },
          { text: 'Configuration', link: '/guide/configuration' }
        ]
      }
    ],
    search: { provider: 'local' },
    socialLinks: [{ icon: 'github', link: 'https://github.com/JustBlueDolphin/gabz-docs' }],
    editLink: {
      pattern: 'https://github.com/JustBlueDolphin/gabz-docs/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    },
    footer: { message: 'Built with VitePress' }
  }
})
