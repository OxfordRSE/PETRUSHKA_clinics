import json

with open("map.json", "r") as f:
    map_data = json.load(f)

assert isinstance(map_data, dict)
assert "CCG_exclusions" in map_data.keys()
assert "clinic_CCGs" in map_data.keys()

for _, v in map_data["clinic_CCGs"].items():
    assert v in map_data["CCG_exclusions"]

print("map.json passed all checks")
