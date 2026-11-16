# 🔧 PDM / Bob74 IPL Conflict Fixes

**bob74_ipl** loads Rockstar's own fixes for the Simeon dealership. These clash with the Gabz PDM (`cfx-gabz-pdm`) and cause broken collisions, duplicate props, or the old building showing through.

::: info
Line numbers are for **bob74_ipl v2.6.0**. In other versions, search for the code shown below instead.
:::

## Collisions

Open `bob74_ipl/dlc_mercenaries/fixes.lua`.

On **line 14**, change `true` to `false`:

```lua{2}
LoadDefault = function()
    MercenariesFixes.Enable(false) -- was true
end
```

## Props

1. Open `bob74_ipl/fxmanifest.lua`.
2. Delete **line 132**:

   ```lua
   , "gta_mpsum2/simeonfix.lua"
   ```

3. Delete the file `bob74_ipl/gta_mpsum2/simeonfix.lua`.

Restart the server afterwards. Restarting only the resource isn't always enough for IPL changes.

## Still Seeing the Default Building?

Another resource is probably still loading the old PDM IPL, `shr_int`. This is usually a dealership script.

1. In VS Code, open your server's `resources` folder and press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F</kbd>.
2. Search for `shr_int`.
3. For every script that calls `RequestIpl('shr_int')` (or similar), remove that line or disable it.

::: tip
Don't forget scripts in `[standalone]` and other subfolders. The search covers every folder under `resources`.
:::
