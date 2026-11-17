"""Build the per-framework Gabz vehicle files served from docs/public/downloads/.

Usage: python scripts/gen-vehicle-data.py "<path to [gbveh]>"
Names, brands, categories and prices come from docs/vehicles/spawn-codes.md;
vehicle types come from the pack's vehicles.meta files.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "public", "downloads")
CATEGORY = {  # spawn-codes.md heading -> framework category key
    "Super": "super", "Sports": "sports", "Sports Classic": "sportsclassics",
    "Muscle": "muscle", "Coupes": "coupes", "Sedans": "sedans", "Compacts": "compacts",
    "SUV": "suvs", "Offroad": "offroad", "Vans": "vans", "Commercial": "commercial",
    "Industrial": "industrial", "Utility": "utility", "Service": "service",
    "Emergency": "emergency",
}
LABEL = {v: k for k, v in CATEGORY.items()} | {"suvs": "SUVs", "sportsclassics": "Sports Classics"}
TYPE = {  # vehicles.meta <type> -> GetVehicleType() name used by Qbox/QBCore
    "VEHICLE_TYPE_CAR": "automobile", "VEHICLE_TYPE_QUADBIKE": "automobile",
    "VEHICLE_TYPE_BIKE": "bike", "VEHICLE_TYPE_BOAT": "boat", "VEHICLE_TYPE_HELI": "heli",
    "VEHICLE_TYPE_PLANE": "plane", "VEHICLE_TYPE_TRAILER": "trailer",
}


def read_cars():
    md = open(os.path.join(ROOT, "docs", "vehicles", "spawn-codes.md"), encoding="utf-8").read()
    cars = []
    for section in re.split(r"^## ", md, flags=re.M)[1:]:
        heading = section.splitlines()[0].strip()
        for code, brand, name, price in re.findall(
                r"^\|\s*(gb[a-z0-9]+)\s*\|\s*([^|]*?)\s*\|\s*([^|]+?)\s*\|[^|]*\|\s*\$([\d,]+)\s*\|", section, re.M):
            cars.append({"model": code, "name": name, "brand": brand,
                         "price": int(price.replace(",", "")), "category": CATEGORY[heading]})
    return cars


def read_types(pack):
    types = {}
    for dirpath, _, files in os.walk(pack):
        if "vehicles.meta" in files:
            s = open(os.path.join(dirpath, "vehicles.meta"), encoding="utf-8", errors="ignore").read()
            for chunk in s.split("<modelName>")[1:]:
                model = chunk.split("<")[0].strip().lower()
                t = re.search(r"<type>\s*([A-Z_]+)", chunk)
                types[model] = TYPE[t.group(1)] if t else "automobile"
    return types


def lua_str(s):
    return "'" + s.replace("\\", "\\\\").replace("'", "\\'") + "'"


def sql_str(s):
    return "'" + s.replace("\\", "\\\\").replace("'", "''") + "'"


def main():
    all_cars = read_cars()
    types = read_types(sys.argv[1])
    assert len(all_cars) == len({c["model"] for c in all_cars}), "duplicate spawn codes"
    # Emergency cars are listed in spawn-codes.md but ship in Gabz's separate emergency pack
    missing = [c for c in all_cars if c["model"] not in types]
    assert all(c["category"] == "emergency" for c in missing), [c["model"] for c in missing if c["category"] != "emergency"]
    cars = [c for c in all_cars if c["model"] in types]
    print(f"skipped {len(missing)} emergency cars not in the pack")
    for c in cars:
        c["type"] = types[c["model"]]
    os.makedirs(OUT, exist_ok=True)

    def write(name, text):
        with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)

    head = "-- Gabz vehicles ({} cars). Generated from the customer pack.\n".format(len(cars))

    # Qbox: entries for the table returned by qbx_core/shared/vehicles.lua
    write("qbox_vehicles.lua", head + "-- Paste inside the `return { ... }` table in qbx_core/shared/vehicles.lua\n" + "".join(
        f"    {c['model']} = {{\n        name = {lua_str(c['name'])},\n        brand = {lua_str(c['brand'])},\n"
        f"        model = '{c['model']}',\n        price = {c['price']},\n        category = '{c['category']}',\n"
        f"        type = '{c['type']}',\n        hash = `{c['model']}`,\n    }},\n" for c in cars))

    # QBCore: entries for the local Vehicles list in qb-core/shared/vehicles.lua
    write("qbcore_vehicles.lua", head + "-- Paste inside the `local Vehicles = { ... }` list in qb-core/shared/vehicles.lua\n" + "".join(
        f"    {{ model = '{c['model']}', name = {lua_str(c['name'])}, brand = {lua_str(c['brand'])}, price = {c['price']}, "
        f"category = '{c['category']}', type = '{c['type']}', shop = 'pdm' }},\n" for c in cars))

    # ESX Legacy: esx_vehicleshop tables (both have primary keys, so re-running is safe)
    used = sorted({c["category"] for c in cars})
    write("esx_vehicles.sql", head.replace("--", "--", 1) +
          "-- Import into your ESX database (esx_vehicleshop).\n\n"
          "INSERT IGNORE INTO `vehicle_categories` (`name`, `label`) VALUES\n" +
          ",\n".join(f"({sql_str(k)}, {sql_str(LABEL[k])})" for k in used) + ";\n\n"
          "INSERT INTO `vehicles` (`name`, `model`, `price`, `category`) VALUES\n" +
          ",\n".join(f"({sql_str(c['name'])}, {sql_str(c['model'])}, {c['price']}, {sql_str(c['category'])})" for c in cars) +
          "\nON DUPLICATE KEY UPDATE `name` = VALUES(`name`), `price` = VALUES(`price`), `category` = VALUES(`category`);\n")

    # vMenu: the "vehicles" list for vMenu/config/addons.json
    write("vmenu_addons.json", json.dumps({"vehicles": [c["model"] for c in cars]}, indent=2) + "\n")

    # Plain data for anything else
    write("gabz_vehicles.json", json.dumps(cars, indent=2) + "\n")
    print(f"wrote {len(cars)} cars to {OUT}")


if __name__ == "__main__":
    main()
