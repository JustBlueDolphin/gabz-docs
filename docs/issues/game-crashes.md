---
outline: [2, 3]
---

# 💥 Game Crashes

Crashes that close the **game** on the player's PC, usually while joining or loading in. If the error is in the server console instead, see [Server Errors](./server-errors).

## "Pool Full" crashes

```ansi
Original error: <PoolName> Pool Full, Size == <number>
```

The game has a fixed number of slots for each type of thing it loads: textures, models, collisions, interiors and so on. Big servers with lots of MLOs and add-on vehicles run out, and the game closes. The fix is always the same: raise that pool in `server.cfg`.

1. Read the **pool name** from the crash, the word before `Pool Full`.
2. Add `increase_pool_size "<PoolName>" <amount>` near the **top** of `server.cfg`, above your `ensure` lines.
3. Restart the **server**.

Look up the max for any pool in [Pool Sizes](./pool-sizes).

### TxdStore Pool Full

```ansi
Error GTA5_b3258.exe+5D3125
Recursive error: An exception occurred (c0000005 at 0x1405d3125) during execution
of the INIT_SESSION function for CExtraContentWrapper. The game will be terminated.

Original error: TxdStore Pool Full, Size == 105500
```

This is the most common one on Gabz servers. `TxdStore` holds texture dictionaries (`.ytd` files). 70 Gabz maps, a vehicle pack and your clothing and other streamed resources can easily fill it.

```ini
increase_pool_size "TxdStore" 50000   # FiveM max: 50000
```

::: warning 26000 is the RedM limit
Lots of guides and configs use `26000` for TxdStore. That's the **RedM** maximum. On FiveM, you can go up to **50000**.
:::

### FragmentStore Pool Full

`FragmentStore` holds fragment models (`.yft`), which means vehicles and breakable props. You'll hit this with large add-on vehicle packs.

```ini
increase_pool_size "FragmentStore" 30000   # FiveM max: 30000
```

### Interior / occlusion pools

Many MLOs in one server can fill the interior and occlusion pools. If the crash names one of these, raise it:

```ini
increase_pool_size "InteriorProxy" 450
increase_pool_size "StaticBounds" 5000
increase_pool_size "OcclusionInteriorInfo" 20
increase_pool_size "OcclusionPathNode" 5000
increase_pool_size "OcclusionPortalEntity" 750
increase_pool_size "OcclusionPortalInfo" 750
increase_pool_size "PortalInst" 225
```

## Checking it worked

- **Server log:** if a value is too high or the pool can't be raised, the server prints a warning and **ignores** the line.
- **In-game:** press <kbd>F8</kbd> → **Tools → Streaming → Pool Monitor** to see each pool's size.

::: info Players restart once
Players' games restart once the first time they join a server with different pool sizes. That's normal.
:::

## Still crashing at the max?

You're streaming more than the game can hold. The pool limit can't go any higher, so you need to stream less:

- Remove maps and vehicle packs you don't use. Every resource you `ensure` uses slots, even if nobody goes there.
- Check for oversized textures. A 4K `.ytd` on a small prop wastes memory. Shrink them to 2K or 1K.
- Look for duplicate resources, for example the same car pack installed twice.
