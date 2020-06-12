import time

from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)

# Using filter method
#def filterDuplicates(name):
#    if(name in names_1):
#        return True
#    else:
#        return False

#for each in map(filterDuplicates, names_2):
#    duplicates.append(each)

namesBinarySearchTree = BSTNode(names_1[0])

i = 1

while i < len(names_1):
    namesBinarySearchTree.insert(names_1[i])
    i += 1

for each in names_2:
    if namesBinarySearchTree.contains(each):
        duplicates.append(each)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
