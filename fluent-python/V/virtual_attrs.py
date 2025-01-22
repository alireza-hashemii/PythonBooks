import json 


with open('oscon.json', 'r') as json_file:
    feed = json.load(json_file)   

print(sorted(feed['Schedule'].keys()))

for key, value in sorted(feed['Schedule'].items()):
    print(f"{len(value)}", key)