---
outline: [2, 3]
---

# 🚨 Common Errors

Server console errors and game crashes you'll see with Gabz maps, and how to fix them. Tip: press <kbd>Ctrl</kbd>+<kbd>K</kbd> and paste part of your error to jump straight here.

## Could not find dependency cfx-gabz-pdprops

```ansi
[  c-resources-core] Could not find dependency cfx-gabz-pdprops for resource cfx-gabz-pacificbank.
[citizen-server-impl] Couldn't start resource cfx-gabz-pacificbank.
```

**What it means:** the map needs `cfx-gabz-pdprops`, but the server can't find that resource anywhere in `resources`. The map refuses to start.

These maps need `cfx-gabz-pdprops`:

| Map | Needs |
| --- | --- |
| `cfx-gabz-davispd` | `cfx-gabz-pdprops` |
| `cfx-gabz-lamesapd` | `cfx-gabz-pdprops` |
| `cfx-gabz-pacificbank` | `cfx-gabz-pdprops` |
| `cfx-gabz-paletopd` | `cfx-gabz-pdprops` |
| `cfx-gabz-sandypd` | `cfx-gabz-pdprops` |
| `cfx-gabz-townhall` | `cfx-gabz-pdprops` |

**Fix:**

1. Check that the `cfx-gabz-pdprops` folder is in your `resources` (e.g. `resources/[gabzmaps]/cfx-gabz-pdprops`). If it's missing, download it from [Keymaster → Asset grants](https://keymaster.fivem.net/asset-grants). It's in the same Gabz package.
2. Check the folder name is exactly `cfx-gabz-pdprops`. No `-main`, no `(1)`, and not nested inside another folder of the same name.
3. Add it to `server.cfg` **before** the PDs:

   ```ini
   ensure cfx-gabz-mapdata
   ensure cfx-gabz-pdprops
   ensure cfx-gabz-pacificbank
   ```

4. Type `refresh` in the server console (or restart the server) so it finds the new folder.

::: tip Don't need the PDs?
If you don't use any of those six maps, remove their `ensure` lines (or delete the folders) and the error goes away. You don't need `cfx-gabz-pdprops` for anything else.
:::

## Could not find dependency cfx-gabz-mapdata

```ansi
Could not find dependency cfx-gabz-mapdata for resource cfx-gabz-xxx.
```

**Every** Gabz map needs `cfx-gabz-mapdata`. Install it the same way as above and `ensure` it first, above every other Gabz map. See [server.cfg Order](./server-cfg).

## Could not find dependency /gameBuild:2545

```ansi
Could not find dependency /gameBuild:2545 for resource cfx-gabz-xxx.
```

Your server runs an older game build. Set this in `server.cfg`, then restart:

```ini
sv_enforceGameBuild 2545   # or newer, e.g. 3258
```

## Could not find dependency /server:4960 or /assetpacks

```ansi
Could not find dependency /server:4960 for resource cfx-gabz-xxx.
Could not find dependency /assetpacks for resource cfx-gabz-xxx.
```

Your server artifact is too old. Update FXServer to the latest **recommended** artifact (at least **5128**). In txAdmin, the link is in the console header.

## You lack the required entitlement

```ansi
You lack the required entitlement to use cfx-gabz-xxx
```

Your server's license key belongs to a Cfx.re account that doesn't own the Gabz package. Use a key from the account that bought it, or transfer the asset on [Keymaster](https://keymaster.fivem.net/asset-grants).

## Game crash: TxdStore Pool Full

```ansi
Error GTA5_b3258.exe+5D3125
Recursive error: An exception occurred (c0000005 at 0x1405d3125) during execution
of the INIT_SESSION function for CExtraContentWrapper. The game will be terminated.

Original error: TxdStore Pool Full, Size == 105500
```

**What it means:** this is a crash in the **game**, not a server console error. The game has a fixed number of slots for texture dictionaries (`.ytd` files). With 70 Gabz maps, a vehicle pack and your other streamed resources, players run out of slots while loading in, and the game closes.

**Fix:** raise the limit in `server.cfg`. Put it near the **top**, above your `ensure` lines:

```ini
increase_pool_size "TxdStore" 26000   # Max: 26000
```

Restart the **server** (not just a resource). Players don't need to change anything. The new limit is sent to them when they connect.

::: warning 26000 is the max
Anything higher is ignored. The server log shows a warning, and the crash keeps happening. Don't copy `50000` or `65500` from old forum posts.
:::

**Check it worked:** in-game, press <kbd>F8</kbd> → **Tools → Streaming → Pool Monitor** and look for `TxdStore`.

### Other "Pool Full" crashes

The same command fixes other pool crashes. Use the pool name from the error message:

```ini
increase_pool_size "FragmentStore" 14000          # Max: 14000 (lots of add-on vehicles)
increase_pool_size "StaticBounds" 5000            # Max: 5000  (collisions, lots of MLOs)
increase_pool_size "OcclusionPathNode" 5000       # Max: 5000
increase_pool_size "OcclusionPortalEntity" 750    # Max: 750
increase_pool_size "OcclusionPortalInfo" 750      # Max: 750
increase_pool_size "PortalInst" 225               # Max: 225
increase_pool_size "ScaleformStore" 200           # Max: 200
increase_pool_size "CMoveObject" 75               # Max: 75
increase_pool_size "OcclusionInteriorInfo" 20     # Max: 20
```

::: tip Still crashing at the max?
You're streaming more than the game can hold. Remove maps and vehicle packs you don't use. Every resource you `ensure` takes up slots, even if nobody goes there.
:::

## Still stuck?

- Clear the server cache (delete the `cache` folder) and restart.
- Look at the [Install & Update](./install) troubleshooting table.
- For map clashes with other creators, see [MLO Conflicts](./conflicts).
