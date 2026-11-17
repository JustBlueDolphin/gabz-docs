---
outline: [2, 3]
---

# 🚗 Vehicle Issues

Common problems with the Gabz vehicle pack and how to fix them. For crashes while loading in, see [Game Crashes](./game-crashes).

## Car doesn't spawn

**"Model doesn't exist" / nothing happens when you spawn it.**

1. **Check the spawn code.** Spawn codes aren't always the folder name. For example, the `[gb_811s2]` folder holds `gb811s2`, and the `[gb_nexus]` folder holds `gbnexus1`. Every code is listed in [Spawn Codes](/vehicles/spawn-codes) and in `vehicle_spawn_names.txt` inside each car resource.
2. **Is it an emergency vehicle?** `gbpol…`, `gbems…` and `gbfirevoyager` are in Gabz's separate emergency pack, not this one.
3. **Check the resource is running.** Type `ensure gb_vehicles_a_to_m` (or the right resource) in the server console and look for errors.
4. **Clear the server cache** and restart.

## Could not find dependency /assetpacks

```ansi
Could not find dependency /assetpacks for resource gb_vehicles_a_to_m.
```

All 6 vehicle resources need a server artifact that supports asset packs. Update FXServer to the latest **recommended** artifact. See [Server Errors](./server-errors#could-not-find-dependency-server-4960-or-assetpacks).

## No engine sound / wrong engine sound

Every car's engine sounds live in **`gb_vehicles_audio`**. Without it, cars fall back to a default GTA sound or make no sound at all.

- Make sure `gb_vehicles_audio` is in your `[gbveh]` folder and starts. `ensure [gbveh]` covers it.
- Don't rename anything inside `sfx/` or `audioconfig/`. The sound names are linked to the folder names.
- Players may need to reconnect after you add it.

## Gabz wheels missing from the mod shop

The wheels are in **`gb_wheels`**. If it isn't running, the Gabz rims don't appear in the wheel menu. Make sure it's in `[gbveh]` and started.

## Name shows as NULL or blank

The display names come from `data/[gb_<car>]/vehicle_names.lua` in each car resource. If you get `NULL`:

- Check you didn't delete or move any `vehicle_names.lua` file.
- If you renamed a car's model, its name entry no longer matches. Put the original name back.

## Mod shop parts missing or wrong

**Wrong spoilers or bumpers show up, or a car's mods are missing.** This usually means two vehicle packs use the same **modkit ID**, so one car's parts overwrite the other's.

1. Run [Modkit-Checker](https://github.com/JustBlueDolphin/Modkit-Checker) on your `resources` folder. It lists every modkit ID used more than once.
2. Change the clashing ID in the **other** pack's `carcols.meta` (both the `<kitName>` and `<id value="..."/>`), and in its `carvariations.meta` if the kit is named there.
3. Restart the server.

::: tip Sirens too
Modkit-Checker also reports duplicate **siren IDs**. If an emergency car has the wrong lights or siren pattern, look for a siren ID clash with another emergency pack.
:::

## Not in the dealership / can't store in garage

The car files alone don't add cars to your framework. Your dealership and garages only know about cars in your shared vehicles list or database. See [Framework Setup](/vehicles/dealership). On Qbox, also check the shop sells that car's category.

## Textures missing, blurry or flickering

- **Whole car or parts look blurry or low-res:** your server streams more textures than players' PCs can hold. Remove packs you don't use. See [Game Crashes → Still crashing at the max?](./game-crashes#still-crashing-at-the-max).
- **Game crashes with `FragmentStore Pool Full`:** see [Game Crashes → FragmentStore](./game-crashes#fragmentstore-pool-full).

## Livery problems

See [Add-on Liveries → Troubleshooting](/vehicles/liveries#troubleshooting).
