# Vehicles

The **Gabz vehicle pack**: **140** lore-friendly cars across 15 categories, all with the `gb` spawn code prefix.

- [Spawn Codes](./spawn-codes) – full list with brands, categories and prices
- [Dealership Setup](./dealership) – drop-in data for QBox, QBCore and ESX
- [Add-on Liveries](./liveries) – make your own liveries with YFT Livery Maker
- [Vehicle Issues](/issues/vehicles) – no sound, missing wheels, mod shop problems

## What's in the pack

The pack comes as **6 resources**:

| Resource | What it holds |
| --- | --- |
| `gb_vehicles_a_to_m` | Cars A–M (part 1) |
| `gb_vehicles_a_to_m2` | Cars A–M (part 2) |
| `gb_vehicles_n_to_z` | Cars N–Z (part 1) |
| `gb_vehicles_n_to_z2` | Cars N–Z (part 2) |
| `gb_vehicles_audio` | **Engine sounds** for every car |
| `gb_wheels` | The Gabz wheels pack, for the mod shop wheel menu |

Each car resource also includes:

- `vehicle_spawn_names.txt`: every spawn code in the pack
- `templates/`: livery templates (`gb_<car>_template.png`). See [Add-on Liveries](./liveries).

## Install

1. Download the pack from [Keymaster → Asset grants](https://keymaster.fivem.net/asset-grants).
2. Put all 6 folders in one category folder, e.g. `resources/[gbveh]`.
3. Add it to `server.cfg`:

   ```ini
   ensure [gbveh]
   ```

4. Add the cars to your framework so players can buy and own them (see [Dealership Setup](./dealership)).
5. Restart the server.

::: warning Keep all 6
`gb_vehicles_audio` and `gb_wheels` aren't optional extras. Without them, cars use the wrong engine sounds and Gabz wheels are missing from the mod shop.
:::

::: tip Traffic
Want Gabz cars in AI traffic? Use [Gabz-Traffic](https://github.com/JustBlueDolphin/Gabz-Traffic). It replaces `popgroups.ymt` so the pack spawns in the world.
:::
