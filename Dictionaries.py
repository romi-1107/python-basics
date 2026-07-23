empty_dict = {}
dict_example = {'key1' : 'value1','key2': 'value2'}

example_list = ['value1','value2']

print(dict_example['key1'])
print(dict_example['key2'])

data_types = {


"int"     : "A whole number like 1,2,or 3.",
"float"   : "A number that can have decimal points, like 2.5 or 0.1.",
"str"     : "Words or letters , like 'Hello' or 'Apple'.",
"bool"    : "True / False. Similar to Yes/No parameters in Revit.",
"list"    : "A group of things you can change, like [1,2,'apple'].",
"tuple"   : "A collection of things you can't change, like (1,2,'apple').",
"dict"    : "Paris of things, like {'name': 'Jhon', 'age':10}.",
"set"     : "A group of unique things, like{1,2,3} Duplicates ignored.",
"NonType" : "Means nothing or empty, like an empty box.",
}

print(data_types['dict'])
print(data_types['set'])
print(data_types.get('NoneType'))
print(data_types.setdefault('Missing','MyValue'))

data_types['int'] = 'Just a number'
print(data_types)

print('list' in data_types)
print('test' not in data_types)

print(len(data_types))

print(data_types.keys())
print(data_types.values())
print(data_types.items())
data_types.update(dict_example)
print(data_types)
print(data_types.pop('bool'))


