myDictList = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
              {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
              {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

newList = list(sorted(myDictList, key=lambda item: int(item['model']), reverse=True))
print(newList)
