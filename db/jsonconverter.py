import json


def convert_json():
  with open('file (2).json', 'r', encoding='UTF-8') as file:
    data = json.load(file)
    output_list = []
    for receipt in data:
      items = receipt['ticket']['document']['receipt']['items']
      date = receipt['query']['date'][:10]
      for item in items:
        list1 = []
        list1.append(date)
        list1.append(item['name'])
        list1.append(item['sum'])
        output_list.append(list1)
  return output_list