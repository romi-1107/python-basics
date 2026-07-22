empty_list = []
my_list    = ['Wall','Floor','Roof','Ceiling','Wall','Floor','Roof','Ceiling']

# print(my_list)
# print(my_list[0])
# print(my_list[2])
# print(my_list[1])
# print(my_list[3])
# print(my_list[:2])
# print(my_list[2:])
# print(my_list[1:2])
# print(my_list[2:5])
# print(my_list[2:5:2])

my_list = ['Wall','Floor','Roof','Ceiling']
my_list[2] = 'NewItem'
my_list[-1] = 'LastItem'
my_list[1:3] = ['a','b']
print(my_list)

my_list= ['Categories','Wall','Floor','Roof','Ceiling']
my_list2 = ['Door','Window']
numbers = [10,20,30,40,50]
header = my_list[0]
data   = my_list[1:]
# print(header)
print(data)
# print('Wall' in my_list)
# print('Door'in my_list)
# print('Door'not in my_list)
# print(len(my_list))
# print(sorted(my_list))
# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))
my_list.append('Door')
my_list.append('Window')
my_list.extend(my_list2)
my_list += my_list2
# print(my_list)
my_list.sort()
# print(my_list)
my_list.count('Door')
# print(my_list.index('Wall'))
# print(my_list)
my_list.insert(2,'Sofa')
my_list.remove('Floor')
# print(my_list)
item = my_list.pop(2)
# print(my_list)
# print(item)
my_list.reverse()
# print(my_list)
my_list.clear()
my_list = []

my_list = ['Wall', 'Floor','Roof','Ceiling']
x = my_list
y = my_list.copy()

my_list.append('NewItem')
print(x)
print(y)


points = [[0,0,0],
          [2,2,0],
    [4,4,0],
[6,6,0]]

pt2 = points[1]
print(points[1][2])
print(pt2[0],pt2[1],pt2[2])

my_list = ['Wall','Floor','Roof','Ceiling']

for i in my_list:
    print(i)
    print(i)
    print(i)


empty_tuple = ()
list_data = [0,1,2,3,4,5,0,1,2,3,4,5]
data = (0,1,2,3,4,5,0,1,2,3,4,5)
data_pts = ((0,0,0),(1,2,3),(2,4,6))

print(data[0])
print(data[2])
print(data[4])
print(data_pts[1])

data  = (0,1,2,3,4,5,0,1,2,3,4,5)

print(data[:2])
print(data[2:])
print(data[1:3])

data = (0,1,2,3,4,5,0,1,2,3,4,5)
print(len(data))
print(min(data))
print(max(data))
print(sum(data))
print(sorted(data))
print(tuple(sorted(data)))

data = (0,1,2,3,4,5,0,1,2,3,4,5)
print(data.count(3))
print(data.index(3))

empty_set = set()
empty_set = {}
set_items = {10,20,30,10,20,'AB','BA','AB',True,True,False}
print(set_items)

list_data  = [1,2,3,4,1,2,3,4]
set_data = set(list_data)
unique_list_data = list(set_data)

print(list_data)
print(set_data)
print(unique_list_data)


items = {10,20,30,'AB','BA','AB',True,True,False}

copy_set = items.copy()
removed = items.pop()
items.clear()

items.discard(3)
items.add(10)

a = {1,2,3,4}
b = {3,4,5,6}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.issubset(b))
print(a.issuperset(b))

print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(sorted(a))




















































































































































































































































































































































































































































































































