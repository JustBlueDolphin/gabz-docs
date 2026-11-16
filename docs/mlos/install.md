# Install & Update

## First install

1. Download the maps from [Keymaster → Asset grants](https://keymaster.fivem.net/asset-grants).
2. Drop every `cfx-gabz-xxx` folder into `resources/[gabzmaps]`.
3. Add the `ensure` lines to `server.cfg` (see [server.cfg Order](./server-cfg)).
4. Clear the server cache (delete the `cache` folder).
5. Restart the server.

::: danger Don't touch the files
Never rename, move or delete anything inside a `cfx-gabz-xxx` folder. The maps are encrypted, and updates will break.
:::

## Updating

1. Delete all existing `cfx-gabz-xxx` folders. Don't copy the new ones over the old ones.
2. Clear the server cache.
3. Download a fresh copy from Keymaster.
4. Check that `server.cfg` includes any new maps.
5. Restart.

## Troubleshooting

Seeing an error in the console? Check [Common Issues](/issues/) first.

| Problem | Fix |
| --- | --- |
| `You lack the required entitlement to use cfx-gabz-xxx` | The server key belongs to a Cfx.re account that doesn't own the pack. Transfer the asset on Keymaster, or use the owner's key. |
| Interior is invisible or you fall through the floor | `cfx-gabz-mapdata` isn't running or starts too late. Move it to the top. |
| PD has missing props | Start `cfx-gabz-pdprops` before the PD maps. |
| Ottos is broken | Ottos needs both `cfx-gabz-247` and `cfx-gabz-pizzeria`. |
| PDM has broken collisions or props, or the old building shows | See [PDM / Bob74 IPL Fix](./pdm-bob74-fix). |
| Floors or walls missing, or props doubled near another creator's map | See [MLO Conflicts](./conflicts). |
| Game crashes on join with `TxdStore Pool Full` | Add `increase_pool_size "TxdStore" 50000` to `server.cfg`. See [Game Crashes](/issues/game-crashes#txdstore-pool-full). |
| Maps load as old versions | Clear the server cache and restart. |
