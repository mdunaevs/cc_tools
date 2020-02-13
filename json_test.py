import json

json_file_name = "family_data.json"

with open(json_file_name, "r") as reader:
    family_json_data = json.load(reader)

print(family_json_data)
