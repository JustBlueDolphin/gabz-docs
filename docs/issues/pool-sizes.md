# 📊 Pool Sizes

Every pool FiveM lets you raise with `increase_pool_size`, and the **maximum** for each. Values above the max are ignored. The server prints a warning, and the crash keeps happening.

```ini
increase_pool_size "<PoolName>" <amount>
```

| Pool | FiveM max increase | Holds |
| --- | ---: | --- |
| `AnimStore` | **20480** | Animation dictionaries (`.ycd`) |
| `AttachmentExtension` | **430** | Entities attached to other entities |
| `Building` | **500** | Buildings from map files |
| `CDoorSyncData` | **20** | Networked door states (door lock scripts) |
| `CMoveObject` | **600** | Moving objects |
| `CNetObjDoor` | **20** | Networked doors |
| `CWeaponComponentInfo` | **2048** | Weapon attachments (add-on weapons) |
| `EntityDescPool` | **20480** | Entity definitions from map files |
| `fragInstGta` | **2000** | Breakable or fragment objects placed in the world |
| `FragmentStore` | **30000** | Fragment models (`.yft`): vehicles and breakable props |
| `fwDynamicArchetypeComponent` | **30000** | Model archetypes from `.ytyp` files (custom props, MLOs) |
| `InteriorProxy` | **450** | MLO interiors |
| `LightEntity` | **1000** | Lights on props and in MLOs |
| `netGameEvent` | **400** | Queued network game events |
| `Object` | **2000** | Spawned objects and props |
| `ObjectIntelligence` | **512** | Objects running tasks |
| `OcclusionInteriorInfo` | **20** | MLO occlusion |
| `OcclusionPathNode` | **5000** | MLO occlusion paths |
| `OcclusionPortalEntity` | **750** | Entities in MLO portals |
| `OcclusionPortalInfo` | **750** | MLO portals |
| `PortalInst` | **225** | MLO portal instances |
| `ScaleformStore` | **200** | Scaleform UI movies (`.gfx`) |
| `StaticBounds` | **5000** | Static collisions (`.ybn`) |
| `TxdStore` | **50000** | Texture dictionaries (`.ytd`) |

*Limits from the [official FiveM docs](https://docs.fivem.net/docs/server-manual/server-commands/#increase_pool_size-poolname-increase), last updated November 2026. Cfx.re can change them at any time. The server log tells you if a value is rejected.*

## Recommended for a Gabz server

A starting point for a server running the full Gabz map pack plus a big vehicle pack. Put it at the **top** of `server.cfg`:

```ini
# --- Pool sizes (stop "Pool Full" crashes) ---
increase_pool_size "TxdStore" 50000
increase_pool_size "FragmentStore" 30000
increase_pool_size "InteriorProxy" 450
increase_pool_size "StaticBounds" 5000
increase_pool_size "OcclusionInteriorInfo" 20
increase_pool_size "OcclusionPathNode" 5000
increase_pool_size "OcclusionPortalEntity" 750
increase_pool_size "OcclusionPortalInfo" 750
increase_pool_size "PortalInst" 225
```

::: tip Only raise what you need
Bigger pools use more memory on players' PCs. Start with the pool your crash names, and add others only if they crash too.
:::

## Good to know

- **Startup only.** Pool sizes are read when the server starts. Restart the server after you change them.
- **Players restart once.** The first time someone joins with different pool sizes, their game restarts. That's normal.
- **Pool Monitor.** In-game, <kbd>F8</kbd> → **Tools → Streaming → Pool Monitor** shows each pool's size.
- **Don't use `set moo 31337` on a live server.** It skips the limits for local testing only. Cfx.re doesn't support it in production.
