# 🎨 Add-on Liveries

Add your own liveries to Gabz cars with **[YFT Livery Maker](https://github.com/JustBlueDolphin/YftLiveryMaker)**, a free Windows tool. Pick the car, drop in your artwork and click **Make liveries**. It writes the livery `.yft` files and the texture (DXT5, 10 mipmaps), and adds the `carcols.meta` and `vehicle_names.lua` entries so the livery shows up in the mod shop.

<a href="https://github.com/JustBlueDolphin/YftLiveryMaker/releases/latest" target="_blank" rel="noopener"><strong>⬇ Download the latest release</strong></a>

::: info Requirements
Windows 10 or 11 (.NET Framework 4.8 is already installed). There's nothing to install: unzip it and run `YftLiveryMaker.exe`.

The app isn't code-signed. If Windows shows **Windows protected your PC**, click **More info**, then **Run anyway**.
:::

## 1. Paint your livery

Every Gabz car comes with a template next to its `fxmanifest.lua`, for example `gb_archerpro2/gb_archerpro2_template.png` (4096×2048).

1. Open the template in Photoshop, GIMP or Paint.NET.
2. Paint your design on top of the template's layout.
3. Hide the template guide lines and export as **PNG** with a transparent background. PSD, TGA, JPG, BMP, TIFF and DDS also work.

## 2. Make the livery

1. **Pick the car.** Click **Open car folder** and choose the car's folder (e.g. `gb_archerpro2`), or the whole vehicle pack.
2. **Add your images.** For each image, use **Save as** to either:
   - **Add as a new livery** (it takes the next free number), or
   - **Replace** one of the car's existing liveries. You can also drag an image onto a livery in the list.
3. **Texture.** Leave it on **DXT5**, **Same as the car's livery**, **10 mipmaps**.
4. **Output.**
   - **New folder:** a copy laid out like the car's resource, ready to drop over it. Safest option.
   - **Into resource:** writes straight into the car's folder. It backs up every file it changes first.
5. Click **Make liveries**.

## 3. Load it in-game

Restart the car's resource, or the whole server. Your livery is in the mod shop under **Livery**.

::: tip Why 10 mipmaps?
Each mipmap is half the size of the one above, and DXT can't go below 4×4. That means a 2048×2048 texture holds exactly 10. Keep **Size** on **Same as the car's livery**, or you'll get fewer mipmaps and blurry or flickering liveries at a distance.
:::

## What it changes

| File | Change |
| --- | --- |
| `stream/.../<car>_livery_N.yft` | New livery model. A copy of the car's own livery file with only the texture swapped |
| `carcols.meta` | New `VMT_LIVERY_MOD` entry in the car's mod kit |
| `vehicle_names.lua` | The livery's name in the mod shop |
| `HOW_TO_INSTALL.txt` / `WHAT_CHANGED.txt` | A list of everything it did, file by file |

## Cars that support add-on liveries

These 51 Gabz cars use YFT liveries, so the tool can add to them. The other Gabz cars don't have livery `.yft` files and won't show up in the tool.

<details>
<summary>Show all 51 cars</summary>

| Car | Spawn code | Liveries included |
| --- | --- | ---: |
| 811 S2 | `gb811s2` | 23 |
| Archer Pro II | `gbarcherpro2` | 12 |
| Argento 2F | `gbargento2f` | 10 |
| Argento 7F | `gbargento7f` | 26 |
| Argento 7F Sportback | `gbargento7fs` | 10 |
| Bison HF | `gbbisonhf` | 28 |
| Boxboy Food Truck | `gbboxboyft` | 10 |
| Brioso Fulmine | `gbbriosof` | 25 |
| Buffalo Hellfire | `gbbuffalohf` | 23 |
| Caracara GSX | `gbcaracaragsx` | 19 |
| Club XR | `gbclubxr` | 11 |
| Deliver-E | `gbdelivere` | 11 |
| Dominator GSX | `gbdominatorgsx` | 18 |
| Dominator LE | `gbdomle` | 24 |
| Echelon | `gbechelon` | 11 |
| Echelon Sportback | `gbechelons` | 11 |
| Elegy RH2 | `gbelegyrh2` | 13 |
| Fenrir | `gbfenrir` | 4 |
| G46 | `gbg46` | 3 |
| Harmann | `gbharmann` | 7 |
| Hurricane | `gbhurricane` | 14 |
| Impaler Deluxe | `gbimpalerdlx` | 13 |
| Issi Metro | `gbissimetro` | 7 |
| Komoda GT | `gbkomodagt` | 18 |
| Laner 4FH | `gblaner4fh` | 15 |
| Meteor | `gbmeteor` | 9 |
| Morpheus | `gbmorpheus` | 5 |
| Nexus | `gbnexus1` | 10 |
| Nexus RR | `gbnexusrr` | 11 |
| Patriot EV | `gbpatriotev` | 18 |
| Prospero | `gbprospero` | 28 |
| Raidillon | `gbraidillon` | 5 |
| Retinue Lozspeed | `gbretinueloz` | 16 |
| Romulus | `gbromulus` | 12 |
| Schrauber | `gbschrauber` | 18 |
| Scout GSX | `gbscoutgsx` | 14 |
| Scout GSX Police | `gbpolscoutgsx` | 10 |
| Shogun | `gbshogun` | 7 |
| Sidewinder | `gbsidewinder` | 19 |
| Solace | `gbsolace` | 13 |
| Solace Vitesse | `gbsolacev` | 8 |
| Steed | `gbsteedvan` | 8 |
| Tomahawk V-STR | `gbtomahawk` | 13 |
| Torero XPR-1 | `gbtoreroxpr1` | 11 |
| Turismo Mugello | `gbmugello` | 11 |
| Vigero Rattler | `gbvigerorat` | 27 |
| Vivant GrB | `gbvivantgrb` | 3 |
| Zeitgeist | `gbzeitgeist` | 10 |
| Zero | `gbzero` | 14 |
| Zeta Rallye | `gbzeta` | 14 |
| ZR350 | `gbzr350` | 17 |

</details>

## Troubleshooting

| Problem | Fix |
| --- | --- |
| Car doesn't show in the tool | It has no livery `.yft` files. See the list above. |
| File starts with `FXAP` / won't open | It's locked by FiveM Asset Escrow. Pick another of the car's livery files. Gabz livery files aren't locked. |
| Livery not in the mod shop | Restart the server, not just the resource, and check `WHAT_CHANGED.txt` to see which files changed. |
| Dark outline around the design | Export with transparency. The tool cleans up transparent edges for you. |

## Advanced

- **Command line:** `yftlivery.exe` in the zip does the same job in batch, for example `yftlivery make "<car folder>" art1.png --install`.
- **AI apps:** turn on **AI apps** in the tool to use it from Claude Desktop, Cursor, VS Code and other MCP apps. See the [README](https://github.com/JustBlueDolphin/YftLiveryMaker#use-it-from-ai-apps).

::: warning
Only make liveries for cars you're allowed to modify, and don't share paid cars.
:::
