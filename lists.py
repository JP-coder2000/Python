list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ["hola", "como", "estás"]

# concatenate lists
list1.append(22222)
list1.extend(list2)

# built in functions
list1.append('A new item')
print(list1)
list1.remove(2)
print(list1)
# pop removes the last item of the list and return with it
result = list1.pop()
print(result)
list1.reverse()
print(list1)

list_numers = [3, 45, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
               432, 424, 234, 234, 234, 2342, 34234, 234234, 2342, 34234, 2342]
list_numers.sort()
print(list_numers)

# list comprehension
# allows us to creat a new list based on existing values of another list
# syntax: [expression for item in list]
# example:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = []


for i in numbers:
    if i % 2 == 0:
        # de esta manera agregamos un nuevo elemento a la lista
        new_list.append(i)


# another way to do it
new_list2 = [i for i in numbers if i % 2 == 0]

names = ["juan", "pedro", "maria", "jose",
         "luis", "jorge", "julio", "javier", "josefin"]

filteres_names = []

for name in names:
    if name.startswith("j"):
        filteres_names.append(name)

filteres_names2 = [name for name in names if name.startswith("j")]
