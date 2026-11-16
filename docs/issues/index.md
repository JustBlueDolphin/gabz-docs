# 🛠️ Common Issues

Find your problem below. Tip: press <kbd>Ctrl</kbd>+<kbd>K</kbd> and paste part of an error message to search every page.

## Quick finder

| What you see | Go to |
| --- | --- |
| `Could not find dependency cfx-gabz-...` in the console | [Server Errors](./server-errors#could-not-find-dependency-cfx-gabz-pdprops) |
| `Couldn't start resource cfx-gabz-...` | [Server Errors](./server-errors) |
| `/gameBuild:2545`, `/server:4960` or `/assetpacks` | [Server Errors](./server-errors#could-not-find-dependency-gamebuild-2545) |
| `You lack the required entitlement` | [Server Errors](./server-errors#you-lack-the-required-entitlement) |
| Game crashes with `... Pool Full, Size == ...` | [Game Crashes](./game-crashes) |
| `TxdStore Pool Full` | [Game Crashes → TxdStore](./game-crashes#txdstore-pool-full) |
| Need the max value for a pool | [Pool Sizes](./pool-sizes) |
| Falling through floors, invisible walls, doubled props | [MLO Conflicts](/mlos/conflicts) |
| PDM has broken collisions or shows the old building | [PDM / Bob74 IPL Fix](/mlos/pdm-bob74-fix) |
| Interior invisible, PD props missing | [Install & Update → Troubleshooting](/mlos/install#troubleshooting) |
| Livery missing from the mod shop | [Add-on Liveries → Troubleshooting](/vehicles/liveries#troubleshooting) |

## First things to try

Most problems go away after these three steps:

1. **Clear the server cache.** Delete the `cache` folder, then restart.
2. **Check the load order.** `cfx-gabz-mapdata` first, then `cfx-gabz-pdprops`, then the maps. See [server.cfg Order](/mlos/server-cfg).
3. **Re-download fresh files.** Never copy new Gabz files over old ones. Delete the old folders first.
