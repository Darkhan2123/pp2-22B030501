import json

with open("json-sample.json", "r") as read_file:
    data = json.load(read_file)

#print(data)

print("Interface Status")
print("=" * 80)
print("DN                                                 Description           Speed    MTU  ")
print("-" * 50 + " " + "-" * 20 + "  " + "-" * 6 + "  " + "-" * 6)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")
    print("{:<50}{:<23}{:<8}{}".format(dn, descr, speed, mtu))