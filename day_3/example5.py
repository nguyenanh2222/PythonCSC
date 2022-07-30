import json
f = open('people.json', 'w')
data = json.loads('people.json')
print(data)
company = {'name': 'TTTH', 'address': 'NVC'}
list = []
list.append(company)
new = {'company': company}
data.update(new)
f.close()
f = open('files_json/people.json', 'w', encoding='utf-8')
json.dump(data, f, indent=4)
f.close()