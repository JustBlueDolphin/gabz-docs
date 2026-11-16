# MLOs

Our server runs the full **Gabz** map pack: 70 resources, including interiors, gang hoods, PDs, shops and banks.

- [Install & Update](./install) – first-time setup and how to update safely
- [Common Errors](./errors) – console errors like `Could not find dependency` and how to fix them
- [server.cfg Order](./server-cfg) – copy-paste `ensure` list in the right order
- [All MLOs](./list) – every map with its version and dependencies
- [Door Locks](./doorlocks) – preset door configs that ship with the pack
- [PDM / Bob74 IPL Fix](./pdm-bob74-fix) – fix PDM collisions and props when using bob74_ipl
- [MLO Conflicts](./conflicts) – find and fix clashes with other creators' maps

## Requirements

| What | Minimum |
| --- | --- |
| Server artifact | **5128** |
| Game build (`sv_enforceGameBuild`) | **2545** |
| Cfx.re account | Must own the Gabz package (checked automatically) |

To check your versions, type `version` and `sv_enforceGameBuild` in the server console.

## Dependencies at a glance

| Resource | Needed by |
| --- | --- |
| `cfx-gabz-mapdata` | **Every** Gabz map. Start it first |
| `cfx-gabz-pdprops` | davispd, lamesapd, paletopd, sandypd, pacificbank, townhall |
| `cfx-gabz-247` + `cfx-gabz-pizzeria` | ottos |

::: tip See them in-game first
Gabz runs a public showcase server. Press F8 and type `connect showcase.gabzv.com`.
:::
