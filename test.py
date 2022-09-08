import json

map = json.loads("map.json")

assert "CCG_exclusions" in map.keys()
assert "clinic_CCGs" in map.keys()

for _, v in map["clinic_CCGs"].items():
  assert v in map["CCG_exclusions"]
