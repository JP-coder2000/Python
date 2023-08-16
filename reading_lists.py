# append() method adds an item to the end of the list.
# insert() method adds an item to a specific index.
# remove() method removes an item from a list based on the value.
# pop() method removes the item at a particular index.

dna = [ 'AUG', 'AUC', 'UCG' ]

dna.append('UAA')     # [ 'AUG', 'AUC', 'UCG', 'UAA' ]
dna.insert(2, 'GAU')  # [ 'AUG', 'AUC', 'GAU', 'UCG', 'UAA' ]
dna.remove('AUC')     # [ 'AUG', 'GAU', 'UCG', 'UAA' ]
dna.pop(0)            # [ 'GAU', 'UCG', 'UAA' ]



#List Method	Description
#.append()	Add an item to the end of the list
#.clear()	Remove all items from the list
#.copy() 	Return a shallow copy of the list
#.count()	Return the number of times the value appears in the list
#.extend()	Appends another list to the current list by extending it
#.index()	Returns the index of a value inside the list
#.insert()	Insert an item at a specified position in the list
#.pop()	    Remove an item from a specified position in the list
#.remove()	Remove an item from the list based on the value of the item
#.reverse()	Reverses the list in place
#.sort()	    Sorts the list in place

books = ["Zero to one","The lean Startup", "The mom test", "Made to Stick", "Life in code"]
books.append("Zero to sold")
books.remove("The lean Startup")
books.pop(0)
print(books)
