# string are immutable thats means its contents cannot be changes
# The following immutable types are builts in pythons

#int
#floats
# bool (true, false): #subclass
str #(string)
tuple
frozenset
bytes
# immutable  objects its should be obvious that an int like 5 cant changed
#5 is always 5 You can add another value to it.For example, we can add 1 to 5 to get a new number: 6
# But we cant change 5
#the same true of floats 3.14159 will always 3.14159
#Once again, we can perform arithmetric with a float, and get a new float value
# But we cant change the value of 3.14159

#BOOL  values are  also  immutables and so are string

result = True
another_result = result
print(id(result))
print(id(another_result))

result = False
print(id(result))

##
results = "Correct"
another_result = result
print(id(another_result))
#
results += "ish"
print(id(results))
print(id(another_result))