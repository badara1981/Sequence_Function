def full_name(*args): # "tuple"
    # 2 names, 3 etc.
    # Handle it "gracefully!!"
    # print(args)
    # return f"{args[0]} {args[1]} {args[2]} {args[3]}"
    # --> TUPLE / List (Tuples cannot be changed/mutated )
    return args

# looping crash
names = ('Felipe', 'Gonzalez') ## tuple

# 2 major ways of doing it
full_string = ""
for name in names:
    full_string += f"{name} " # name + " " $$$
    # print(name, end="") # A for effort!!!

print(full_string.strip())    

###



#(note the parantheses on the function call split.)

#split() creates a list where each element is from your original string, delimited by whitespace. You can now grab the second element using name.split()[1] or the last element using name.split()[-1]

#However, as others said, unless you're SURE you're just getting a string like "First_Name <space> Last_Name", there are a lot more issues involved. 


##  printing string in full
def full_name(*args):
    for name in args:
        print(name)
full_name("BADARA  JAMMEH")

def  full_name(**kwargs):
    if 'full_name' in kwargs:
        print(kwargs)
        if 'name' in kwargs:
            print('full_name {]'.format(kwargs['full_name']))
    else:
        print('his name is felipe Gonzalez')