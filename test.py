import json

print("Checking map.json:\n")
with open("map.json", "r") as f:
    map_data = json.load(f)

assert isinstance(map_data, list)
for ccg in map_data:
    print(f"- Checking ccg {map_data.index(ccg)}")
    assert isinstance(ccg, dict)
    print(f"- - is dictionary")
    assert "name" in ccg.keys()
    print(f"- - name {ccg['name']}")
    assert "excluded_drugs" in ccg.keys()
    print(f"- - has excluded_drugs list")
    for d in ccg['excluded_drugs']:
        print(f"- - - Checking drug {ccg['excluded_drugs'].index(d)}")
        assert isinstance(d, str)
        print(f"- - - - is string ({d})")
    assert "clinics" in ccg.keys()
    print(f"- - has clinic list")
    for c in ccg['clinics']:
        print(f"- - - Checking clinic {ccg['clinics'].index(c)}")
        assert isinstance(c, dict)
        print(f"- - - - is dictionary")
        assert "name" in c.keys()
        print(f"- - - - name {c['name']}")
        assert "code" in c.keys()
        print(f"- - - - code {c['code']}")

print("\nmap.json passed all checks")
