# ⚠️ MLO Conflicts

## Why conflicts happen with other MLO creators

Conflicts usually happen when maps from different creators reuse or overlap the same files or the same area. Common causes:

| Cause | What you'll see |
| --- | --- |
| **YMAPs** | Duplicate or missing props, buildings spawning on top of each other |
| **Occlusions** | Walls or whole interiors disappearing at certain angles |
| **Collisions** | Falling through floors, invisible walls, cars sinking into the road |

::: info Collision conflicts
To fix a collision conflict, you may need to ask the other map's creator to change or remove the problem files. If you know how, you can fix them yourself instead.
:::

## Resolving MLO conflicts

Follow these steps to find and fix map conflicts, especially when you use Gabz maps.

### 1. Disable all maps except Gabz

Keep only the Gabz maps running, so you can rule them out.

### 2. Clear the server cache

Delete the server `cache` folder so leftover data doesn't affect the test.

### 3. Test for the issue

Start the server and check whether the problem is gone. If it's fixed, carry on to the next step.

### 4. Add maps back one at a time

Turn your other maps back on **one by one**, and test after each one. The map that brings the problem back is the one that conflicts.

### 5. Fix the conflict

Once you know which map conflicts, either:

- **Disable** one of the two conflicting maps, **or**
- **Fix** it by checking and editing the conflicting files.

## Using Springo Duplicate File Finder

[Springo Duplicate File Finder](https://github.com/springoooo/springo-duplicatefilefinder) makes this much faster. It's a small Windows app that scans a folder for files with the same name, such as two maps streaming the same `.ybn` collision file.

1. Download the `.exe` from the repo's **Releases** page.
2. Run it and pick your `resources` folder.
3. Add filters for files you don't care about, such as `fxmanifest.lua` and `client.lua`. Include the file extension, or the filter won't match.
4. Click **Find duplicate files**. You can save the results to a text file.

::: tip Ignore Gabz files
Ignore anything it flags inside Gabz MLO files. Focus on duplicates in other creators' maps.
:::

## Resources

- **Tool repository:** [springoooo/springo-duplicatefilefinder](https://github.com/springoooo/springo-duplicatefilefinder)
- **Video demo:**

<a href="https://www.youtube.com/watch?v=s7PyQIoMslE" target="_blank" rel="noopener">
  <img src="https://img.youtube.com/vi/s7PyQIoMslE/hqdefault.jpg" alt="Springo Duplicate File Finder video demo" style="border-radius:8px;max-width:480px;width:100%">
</a>
