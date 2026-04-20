import json

with open('example.json', 'r') as f:
    data_json = json.load(f)
print("JSON Data:\n", data_json)

with open('output.json', 'w') as f:
    json.dump(data_json, f, indent=4)
