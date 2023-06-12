import csv
import json

with open('CNKGraph.Writings.json', encoding='utf-8-sig') as f:
    o = json.load(f)

items = o['Items']

def process_item(item):
    id_ = item['Id']
    title = item['Title']['Content']
    group_index = item.get('GroupIndex')
    type_ = item['Type']
    dynasty = item['Dynasty']
    author = item['Author']
    content = ''.join(x['Content'] for x in item['Clauses'])

    return id_, title, group_index, type_, dynasty, author, content

with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', lineterminator='\n', strict=True)
    writer.writerow(['id', 'title', 'group_index', 'type', 'dynasty', 'author', 'content'])
    for item in items:
        id_, title, group_index, type_, dynasty, author, content = process_item(item)
        writer.writerow([id_, title, group_index, type_, dynasty, author, content])
