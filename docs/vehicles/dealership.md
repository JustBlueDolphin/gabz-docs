---
outline: [2, 3]
---

# 🧩 Framework Setup

Ready-made files that add all **108** Gabz cars to your framework, for every popular txAdmin recipe. Download the one for your server, follow the steps, and the cars show up in your dealership, garages and menus.

| txAdmin recipe | File | Goes into |
| --- | --- | --- |
| **Qbox** | <a href="/gabz-docs/downloads/qbox_vehicles.lua" download>qbox_vehicles.lua</a> | `qbx_core/shared/vehicles.lua` |
| **ESX Legacy** | <a href="/gabz-docs/downloads/esx_vehicles.sql" download>esx_vehicles.sql</a> | Your database (`esx_vehicleshop`) |
| **QBCore** *(no longer a txAdmin recipe)* | <a href="/gabz-docs/downloads/qbcore_vehicles.lua" download>qbcore_vehicles.lua</a> | `qb-core/shared/vehicles.lua` |
| **vMenu** | <a href="/gabz-docs/downloads/vmenu_addons.json" download>vmenu_addons.json</a> | `vMenu/config/addons.json` |
| **FiveM Basic Server** | Use the vMenu file | Install vMenu first |
| Anything else | <a href="/gabz-docs/downloads/gabz_vehicles.json" download>gabz_vehicles.json</a> | Plain data: model, name, brand, price, category, type |

::: info Before you start
Install the vehicle pack first (see [Vehicles → Install](./#install)). These files only tell your framework about the cars. They don't contain the cars themselves.

Prices and categories match the [Spawn Codes](./spawn-codes) list. Change any price you like after importing.
:::

## Qbox

1. Download <a href="/gabz-docs/downloads/qbox_vehicles.lua" download>qbox_vehicles.lua</a>.
2. Open `resources/[qbx]/qbx_core/shared/vehicles.lua`.
3. Paste the file's contents **inside** the `return { ... }` table, for example right after `return {`:

   ```lua
   return {
       gb811s2 = {
           name = '811 S2',
           brand = 'Pfister',
           model = 'gb811s2',
           price = 150000,
           category = 'super',
           type = 'automobile',
           hash = `gb811s2`,
       },
       -- ...the rest of the Gabz cars, then the original cars
   ```

4. Restart the **server**.

::: warning Super and Sports cars don't show at PDM by default
The Qbox recipe's `qbx_vehicleshop` only sells some categories at PDM. To sell the Gabz super, sports, commercial, industrial, utility and service cars too, add their categories to a shop in `qbx_vehicleshop/config/shared.lua`:

```lua
categories = {
    -- ...existing categories
    super = 'Super',
    sports = 'Sports',
},
```
:::

## ESX Legacy

1. Download <a href="/gabz-docs/downloads/esx_vehicles.sql" download>esx_vehicles.sql</a>.
2. Open your server's database in **HeidiSQL** or **phpMyAdmin**. It's the one named in `mysql_connection_string` in `server.cfg`.
3. Run the file (HeidiSQL: **File → Run SQL file**; phpMyAdmin: **Import**).
4. Restart the **server**.

The file:

- adds the categories ESX doesn't have yet (commercial, industrial, service, utility). Categories you already have are left alone.
- adds the 108 cars to the `vehicles` table. If a car is already there, its name, price and category are updated, so it's safe to run again.

## QBCore

QBCore isn't in txAdmin's recipe list anymore, but lots of servers still run it.

1. Download <a href="/gabz-docs/downloads/qbcore_vehicles.lua" download>qbcore_vehicles.lua</a>.
2. Open `resources/[qb]/qb-core/shared/vehicles.lua`.
3. Paste the file's contents **inside** the `local Vehicles = { ... }` list.
4. Every car is set to `shop = 'pdm'`. To sell a car somewhere else, change it, e.g. `shop = 'luxury'` or `shop = { 'pdm', 'luxury' }`.
5. Restart the **server**.

## vMenu & FiveM Basic Server

vMenu lists add-on cars under **Vehicle Spawner → Addon Vehicles**. The **FiveM Basic Server** recipe has no way to spawn cars, so install vMenu (it's also a txAdmin recipe) and use this file.

1. Download <a href="/gabz-docs/downloads/vmenu_addons.json" download>vmenu_addons.json</a>.
2. Open `resources/vMenu/config/addons.json`.
3. Replace its `"vehicles": [ ... ]` list with the one from the file, or add the Gabz entries to your existing list. Keep the other sections (`peds`, `weapons` and so on).
4. Restart vMenu or the server.

## Not supported

**StreetKings** and **WarfareTactics** are full game modes with their own vehicle lists. You can't add Gabz cars to them through a config file.

## Emergency vehicles

The 32 police, EMS and fire vehicles aren't in these files, because they aren't in the vehicle pack. They're a separate Gabz pack. See the note on [Spawn Codes → Emergency](./spawn-codes#emergency).

::: tip Restart the server, not the resource
Shared vehicle lists are loaded when the framework starts. If you only restart the resource, the dealership won't see the new cars.
:::
