
list_names = ["Victor", 
"Peter", 
"Mary", 
"John", 
"Badara", 
"Peer"]

list_names.append(' David')
list_names.append('malcolm')
print('List_names:', 'David')
print(list_names)

#  Replace an Item 

# Replace an item at a particular index in a Python list
a_list = ["Victor", 
"Peter", 
"Mary", 
"John", 
"Badara", 
"Peer"]

# Mofidy first item  last name
list_names[-1] = "peer"
print(list_names)
# Returns: [Victor Peter, Mary, John, Badara, Malcolm]

# Modify last item
# Modify last item
list_names[-1] = "maxcolm"
print(list_names)

##
# Replace a particular item in a Python list
list_names = ["Victor", 
"Peter", 
"Mary", 
"John", 
"Badara", 
"Peer"]

for i in range(len(a_list)):
    if a_list[i] == 'peer':
        a_list[i] = 'marclom'

print(list_names)

# Replace All Instances of a Single Character using replace()

