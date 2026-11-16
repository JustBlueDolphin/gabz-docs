# Door Locks

`cfx-gabz-mapdata/gabz-doorlocks/` ships one door config file per map (66 files), with coordinates, model hashes and default jobs already filled in.

They use the `Config.DoorList` format from **nui_doorlock**, so you can copy them straight into that resource:

```lua
-- bennys.lua: front garage door
table.insert(Config.DoorList, {
	objCoords = vector3(-230.812, -1326.999, 30.24859),
	objHash = -48831039,
	objHeading = 270.0,
	maxDistance = 6.0,
	locked = true,
	garage = true,
	slides = true,
	authorizedJobs = { ['bennys'] = 0 },
})
```

::: tip Using ox_doorlock?
The coordinates and `objHash` values still apply. Create each door in-game with `/doorlock`, or convert the file. The job names in `authorizedJobs` must match your framework's job names.
:::
