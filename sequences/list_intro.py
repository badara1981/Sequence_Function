# MUTABLE 
# List are mutable therefore they can be change the content of Lists
# STRING are IMMUTABLE they cant be change there contents

computer_parts = ["computers",
 "mouse", 
 "keyboards", 
 "monitors", 
 "mouse cat"
 ]

for part in computer_parts:
    print(part)
    print()
    print(computer_parts[2])
    print(computer_parts[0:3])
    print(computer_parts[-1])