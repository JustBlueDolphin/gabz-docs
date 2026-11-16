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
      { text: 'Vehicles', link: '/vehicles/' },
      { text: 'Common Issues', link: '/issues/' }
    ],
    sidebar: {
      '/mlos/': [
        {
          text: 'MLOs',
          items: [
            { text: 'Overview', link: '/mlos/' },
            { text: 'Install & Update', link: '/mlos/install' },
            { text: 'server.cfg Order', link: '/mlos/server-cfg' },
            { text: 'All MLOs', link: '/mlos/list' },
            { text: 'Door Locks', link: '/mlos/doorlocks' },
            { text: 'PDM / Bob74 IPL Fix', link: '/mlos/pdm-bob74-fix' },
            { text: 'MLO Conflicts', link: '/mlos/conflicts' }
          ]
        }
      ],
      '/issues/': [
        {
          text: 'Common Issues',
          items: [
            { text: 'Quick Finder', link: '/issues/' },
            { text: 'Server Errors', link: '/issues/server-errors' },
            { text: 'Game Crashes', link: '/issues/game-crashes' },
            { text: 'Pool Sizes', link: '/issues/pool-sizes' }
          ]
        },
        {
          text: 'Related',
          items: [
            { text: 'MLO Conflicts', link: '/mlos/conflicts' },
            { text: 'PDM / Bob74 IPL Fix', link: '/mlos/pdm-bob74-fix' }
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
