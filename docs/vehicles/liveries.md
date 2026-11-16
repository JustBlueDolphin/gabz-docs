# 🎨 Add-on Liveries

Add your own liveries to Gabz cars with **[YFT Livery Maker](https://github.com/JustBlueDolphin/YftLiveryMaker)**, a free Windows tool. Pick the car, drop in your artwork and click **Make liveries**. It writes the livery `.yft` files and the texture (DXT5, 10 mipmaps), and adds the `carcols.meta` and `vehicle_names.lua` entries so the livery shows up in the mod shop.

<a href="https://github.com/JustBlueDolphin/YftLiveryMaker/releases/latest" target="_blank" rel="noopener"><strong>⬇ Download the latest release</strong></a>

::: info Requirements
Windows 10 or 11 (.NET Framework 4.8 is already installed). There's nothing to install: unzip it and run `YftLiveryMaker.exe`.

The app isn't code-signed. If Windows shows **Windows protected your PC**, click **More info**, then **Run anyway**.
:::

## 1. Paint your livery

The templates come with the pack, in each car resource's `templates` folder:

```
[gbveh]/gb_vehicles_a_to_m/templates/gb_archerpro2_template.png
```

1. Open the template in Photoshop, GIMP or Paint.NET.
2. Paint your design on top of the template's layout.
3. Hide the template guide lines and export as **PNG** with a transparent background. PSD, TGA, JPG, BMP, TIFF and DDS also work.

## 2. Make the livery

1. **Pick the car.** Click **Open car folder** and choose the resource the car is in, e.g. `gb_vehicles_a_to_m`. The table below shows which one. You can also pick the whole `[gbveh]` folder. Every car with liveries is listed.
2. **Add your images.** For each image, use **Save as** to either:
   - **Add as a new livery** (it takes the next free number), or
   - **Replace** one of the car's existing liveries. You can also drag an image onto a livery in the list.
3. **Texture.** Leave it on **DXT5**, **Same as the car's livery**, **10 mipmaps**.
4. **Output.**
   - **New folder:** a copy laid out like the resource, ready to drop over it. Safest option.
   - **Into resource:** writes straight into the resource. It backs up every file it changes first.
5. Click **Make liveries**.

## 3. Load it in-game

Restart the server. Your livery is in the mod shop under **Livery**.

::: tip Why 10 mipmaps?
Each mipmap is half the size of the one above, and DXT can't go below 4×4. That means a 2048×2048 texture holds exactly 10. Keep **Size** on **Same as the car's livery**, or you'll get fewer mipmaps and blurry or flickering liveries at a distance.
:::

## What it changes

| File | Change |
| --- | --- |
| `stream/[gb_<car>]/liveries/*.yft` | New livery model. A copy of the car's own livery file with only the texture swapped |
| `data/[gb_<car>]/carcols.meta` | New `VMT_LIVERY_MOD` entry in the car's mod kit |
| `data/[gb_<car>]/vehicle_names.lua` | The livery's name in the mod shop |
| `HOW_TO_INSTALL.txt` / `WHAT_CHANGED.txt` | A list of everything it did, file by file |

## Cars that support add-on liveries

These 97 cars ship with livery `.yft` files, so the tool can add to them. The others don't have livery `.yft` files and won't show up in the tool.

<details>
<summary>Show all 97 cars</summary>

| Car | Spawn code | Resource | Liveries included |
| --- | --- | --- | ---: |
| 811 S2 | `gb811s2` | `gb_vehicles_a_to_m` | 25 |
| Admiral | `gbadmiral` | `gb_vehicles_a_to_m` | 12 |
| Archer Pro II | `gbarcherpro2` | `gb_vehicles_a_to_m` | 12 |
| Argento 2F | `gbargento2f` | `gb_vehicles_a_to_m` | 10 |
| Argento 7F | `gbargento7f` | `gb_vehicles_a_to_m` | 26 |
| Argento 7F Sportback | `gbargento7fs` | `gb_vehicles_a_to_m` | 10 |
| Banshee S | `gbbanshees` | `gb_vehicles_a_to_m` | 25 |
| Bison HF | `gbbisonhf` | `gb_vehicles_a_to_m` | 28 |
| Bison STX | `gbbisonstx` | `gb_vehicles_a_to_m` | 23 |
| Boxboy | `gbboxboy` | `gb_vehicles_a_to_m` | 18 |
| Boxboy Food Truck | `gbboxboyft` | `gb_vehicles_a_to_m` | 10 |
| Brioso Fulmine | `gbbriosof` | `gb_vehicles_a_to_m` | 25 |
| Buffalo Hellfire | `gbbuffalohf` | `gb_vehicles_a_to_m2` | 23 |
| Caracara GSX | `gbcaracaragsx` | `gb_vehicles_a_to_m2` | 19 |
| Club XR | `gbclubxr` | `gb_vehicles_a_to_m` | 11 |
| Comet Classic | `gbcometcl` | `gb_vehicles_a_to_m` | 25 |
| Comet Classic Florio | `gbcometclf` | `gb_vehicles_a_to_m` | 25 |
| Comet S1 Turbo | `gbcomets1t` | `gb_vehicles_a_to_m` | 40 |
| Comet S1 Turbo Florio | `gbcomets1tf` | `gb_vehicles_a_to_m` | 40 |
| Comet S2R | `gbcomets2r` | `gb_vehicles_a_to_m` | 27 |
| Comet S2RC | `gbcomets2rc` | `gb_vehicles_a_to_m` | 25 |
| Cypher GTS | `gbcyphergts` | `gb_vehicles_a_to_m` | 13 |
| Deliver-E | `gbdelivere` | `gb_vehicles_a_to_m` | 11 |
| Dice | `gbdice` | `gb_vehicles_a_to_m2` | 12 |
| Dominator GSX | `gbdominatorgsx` | `gb_vehicles_a_to_m` | 18 |
| Dominator LE | `gbdomle` | `gb_vehicles_a_to_m2` | 24 |
| E-Rotiq | `gberotiq` | `gb_vehicles_a_to_m` | 7 |
| e-Surfer | `gbesurfer` | `gb_vehicles_a_to_m2` | 7 |
| Echelon | `gbechelon` | `gb_vehicles_a_to_m` | 11 |
| Echelon Sportback | `gbechelons` | `gb_vehicles_a_to_m` | 11 |
| Elegy RH2 | `gbelegyrh2` | `gb_vehicles_a_to_m` | 13 |
| Emerus | `gbemerus` | `gb_vehicles_a_to_m2` | 11 |
| Emerus SB1 | `gbemerussb1` | `gb_vehicles_a_to_m` | 6 |
| Eon | `gbeon` | `gb_vehicles_a_to_m` | 14 |
| Gresley STX | `gbgresleystx` | `gb_vehicles_a_to_m` | 41 |
| Grotti Cheetah S | `gbcheetahs` | `gb_vehicles_a_to_m` | 6 |
| Hades | `gbhades` | `gb_vehicles_a_to_m2` | 10 |
| Harmann | `gbharmann` | `gb_vehicles_a_to_m2` | 7 |
| Hedra | `gbhedra` | `gb_vehicles_a_to_m2` | 10 |
| Hedra Kombi | `gbhedrakombi` | `gb_vehicles_a_to_m2` | 10 |
| Hurricane | `gbhurricane` | `gb_vehicles_a_to_m2` | 11 |
| Impaler Deluxe | `gbimpalerdlx` | `gb_vehicles_a_to_m2` | 13 |
| Impaler LE | `gbimpaler` | `gb_vehicles_a_to_m2` | 17 |
| Iris Z | `gbirisz` | `gb_vehicles_a_to_m2` | 14 |
| Issi Metro | `gbissimetro` | `gb_vehicles_a_to_m2` | 7 |
| Kisai RS | `gbkisairs` | `gb_vehicles_a_to_m2` | 9 |
| Komoda GT | `gbkomodagt` | `gb_vehicles_a_to_m2` | 18 |
| Laner 4FH | `gblaner4fh` | `gb_vehicles_a_to_m2` | 15 |
| LOD-4 | `gblod4` | `gb_vehicles_a_to_m2` | 27 |
| Meteor | `gbmeteor` | `gb_vehicles_a_to_m2` | 9 |
| Milano GTS | `gbmilano` | `gb_vehicles_a_to_m2` | 20 |
| Mochi | `gbmochi` | `gb_vehicles_a_to_m2` | 28 |
| Mojave | `gbmojave` | `gb_vehicles_a_to_m2` | 12 |
| Neon Cross Turismo | `gbneonct` | `gb_vehicles_n_to_z` | 6 |
| Nexus | `gbnexus1` | `gb_vehicles_n_to_z2` | 10 |
| Nexus RR | `gbnexusrr` | `gb_vehicles_n_to_z` | 11 |
| Nobile | `gbnobile` | `gb_vehicles_n_to_z2` | 24 |
| Prospero | `gbprospero` | `gb_vehicles_n_to_z` | 28 |
| Raidillon | `gbraidillon` | `gb_vehicles_n_to_z` | 5 |
| Retinue Lozspeed | `gbretinueloz` | `gb_vehicles_n_to_z` | 16 |
| Romulus | `gbromulus` | `gb_vehicles_n_to_z` | 11 |
| Ronin | `gbronin` | `gb_vehicles_n_to_z` | 8 |
| Rumina | `gbrumina` | `gb_vehicles_n_to_z` | 23 |
| Rumpo Esperta | `gbesperta` | `gb_vehicles_a_to_m2` | 16 |
| Sapphire | `gbsapphire` | `gb_vehicles_n_to_z` | 29 |
| Schrauber | `gbschrauber` | `gb_vehicles_n_to_z` | 10 |
| Schwartzer S | `gbschwartzers` | `gb_vehicles_n_to_z` | 14 |
| Scout GSX | `gbscoutgsx` | `gb_vehicles_n_to_z` | 14 |
| Sentinel GTS-R | `gbsentinelgts` | `gb_vehicles_n_to_z` | 14 |
| Shogun | `gbshogun` | `gb_vehicles_n_to_z2` | 7 |
| Sidewinder | `gbsidewinder` | `gb_vehicles_n_to_z` | 19 |
| Solace | `gbsolace` | `gb_vehicles_n_to_z` | 13 |
| Solace Vitesse | `gbsolacev` | `gb_vehicles_n_to_z` | 7 |
| Stanier LE | `gbstanierle` | `gb_vehicles_n_to_z` | 9 |
| Starlight | `gbstarlight` | `gb_vehicles_n_to_z` | 22 |
| Steed | `gbsteedvan` | `gb_vehicles_n_to_z` | 11 |
| Steed Crewmate | `gbsteedcrew` | `gb_vehicles_n_to_z` | 8 |
| Sultan RSx | `gbsultanrsx` | `gb_vehicles_n_to_z` | 20 |
| Tempesta Fuoristrada | `gbtempestafs` | `gb_vehicles_n_to_z` | 8 |
| Terrorizer | `gbterrorizer` | `gb_vehicles_n_to_z` | 19 |
| Tokage (JDM) | `gbtokage2` | `gb_vehicles_n_to_z2` | 16 |
| Tokage (USDM) | `gbtokage` | `gb_vehicles_n_to_z2` | 16 |
| Torero XPR-1 | `gbtoreroxpr1` | `gb_vehicles_n_to_z2` | 11 |
| TR3-S | `gbtr3s` | `gb_vehicles_n_to_z2` | 7 |
| Turismo 300GT | `gbturismogt` | `gb_vehicles_n_to_z2` | 5 |
| Turismo 300GT Spider | `gbturismogts` | `gb_vehicles_n_to_z2` | 5 |
| Turismo Mugello | `gbmugello` | `gb_vehicles_a_to_m2` | 11 |
| Vigero Rattler | `gbvigerorat` | `gb_vehicles_n_to_z2` | 27 |
| Vivant | `gbvivant` | `gb_vehicles_n_to_z2` | 10 |
| Vivant GrB | `gbvivantgrb` | `gb_vehicles_n_to_z2` | 3 |
| Voyager 4x2-B | `gbvoyagerb2` | `gb_vehicles_n_to_z2` | 9 |
| Voyager 6x2-H | `gbvoyagerh` | `gb_vehicles_n_to_z2` | 24 |
| Voyager 6x4-B | `gbvoyagerb` | `gb_vehicles_n_to_z2` | 11 |
| Voyager Trash Truck | `gbvoyagerg` | `gb_vehicles_n_to_z2` | 13 |
| Zeitgeist | `gbzeitgeist` | `gb_vehicles_n_to_z2` | 10 |
| Zero | `gbzero` | `gb_vehicles_n_to_z2` | 14 |
| ZR350 | `gbzr350` | `gb_vehicles_n_to_z2` | 17 |
</details>

## Troubleshooting

| Problem | Fix |
| --- | --- |
| Car doesn't show in the tool | It has no livery `.yft` files. See the list above. |
| File starts with `FXAP` / won't open | It's locked by FiveM Asset Escrow. The Gabz livery files aren't locked, so check you picked the `liveries` folder and not `model`. |
| Livery not in the mod shop | Restart the server, not just the resource, and check `WHAT_CHANGED.txt` to see which files changed. |
| Dark outline around the design | Export with transparency. The tool cleans up transparent edges for you. |

## Advanced

- **Command line:** `yftlivery.exe` in the zip does the same job in batch, for example `yftlivery make "<resource folder>" art1.png --car gbarcherpro2 --install`.
- **AI apps:** turn on **AI apps** in the tool to use it from Claude Desktop, Cursor, VS Code and other MCP apps. See the [README](https://github.com/JustBlueDolphin/YftLiveryMaker#use-it-from-ai-apps).

::: warning
Only make liveries for cars you're allowed to modify, and don't share paid cars.
:::
