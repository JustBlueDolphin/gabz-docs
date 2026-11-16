# Dealership Setup

Ready-made data for all Gabz vehicles lives in [Gabz-Vehicle-Data](https://github.com/JustBlueDolphin/Gabz-Vehicle-Data).

| Framework | File | Where it goes |
| --- | --- | --- |
| **QBox** | [`QBX/vehicles.lua`](https://github.com/JustBlueDolphin/Gabz-Vehicle-Data/blob/main/QBX/vehicles.lua) | Paste into `qbx_core/shared/vehicles.lua` |
| **QBox** | [`QBX/shared.lua`](https://github.com/JustBlueDolphin/Gabz-Vehicle-Data/blob/main/QBX/shared.lua) | Dealership categories |
| **QBCore** (new) | [`QB/QB_new.lua`](https://github.com/JustBlueDolphin/Gabz-Vehicle-Data/blob/main/QB/QB_new.lua) | Paste into `qb-core/shared/vehicles.lua` |
| **QBCore** (old) | [`QB/QB_old.lua`](https://github.com/JustBlueDolphin/Gabz-Vehicle-Data/blob/main/QB/QB_old.lua) | For older `QBShared.Vehicles` format |
| **ESX** | [`ESX/Gabz.sql`](https://github.com/JustBlueDolphin/Gabz-Vehicle-Data/blob/main/ESX/Gabz.sql) | Import into your database (`vehicles` table) |

## QBox entry example

```lua
gb811s2 = {
    name = '811 S2',
    brand = 'Pfister',
    model = 'gb811s2',
    price = 150000,
    category = 'super',
    type = 'automobile',
    hash = `gb811s2`,
},
```

::: warning
Restart the server after you edit shared vehicle files. If you only restart the resource, the dealership won't see the new cars.
:::
