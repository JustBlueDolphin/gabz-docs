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
      { text: 'MLOs', link: '/mlos/' },
      { text: 'Vehicles', link: '/vehicles/' }
    ],
    sidebar: {
      '/mlos/': [
        {
          text: 'MLOs',
          items: [
            { text: 'Overview', link: '/mlos/' },
            { text: 'Install & Update', link: '/mlos/install' },
            { text: 'Common Errors', link: '/mlos/errors' },
            { text: 'server.cfg Order', link: '/mlos/server-cfg' },
            { text: 'All MLOs', link: '/mlos/list' },
            { text: 'Door Locks', link: '/mlos/doorlocks' },
            { text: 'PDM / Bob74 IPL Fix', link: '/mlos/pdm-bob74-fix' },
            { text: 'MLO Conflicts', link: '/mlos/conflicts' }
          ]
        }
      ],
      '/vehicles/': [
        {
          text: 'Vehicles',
          items: [
            { text: 'Overview', link: '/vehicles/' },
            { text: 'Spawn Codes', link: '/vehicles/spawn-codes' },
            { text: 'Dealership Setup', link: '/vehicles/dealership' },
            { text: 'Add-on Liveries', link: '/vehicles/liveries' }
          ]
        }
      ]
    },
    search: { provider: 'local' },
    socialLinks: [{ icon: 'github', link: 'https://github.com/JustBlueDolphin/gabz-docs' }],
    editLink: {
      pattern: 'https://github.com/JustBlueDolphin/gabz-docs/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    },
    footer: { message: 'Built with VitePress' }
  }
})
