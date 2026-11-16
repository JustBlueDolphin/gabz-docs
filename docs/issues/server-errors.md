---
outline: [2, 3]
---

# 🖥️ Server Console Errors

Errors in the server console (txAdmin / FXServer window) and how to fix them. If the *game* crashes instead, see [Game Crashes](./game-crashes). Tip: press <kbd>Ctrl</kbd>+<kbd>K</kbd> and paste part of your error to jump straight here.

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

**Every** Gabz map needs `cfx-gabz-mapdata`. Install it the same way as above and `ensure` it first, above every other Gabz map. See [server.cfg Order](/mlos/server-cfg).

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

## Still stuck?

- Clear the server cache (delete the `cache` folder) and restart.
- Look at the [Install & Update](/mlos/install#troubleshooting) troubleshooting table.
- For map clashes with other creators, see [MLO Conflicts](/mlos/conflicts).
