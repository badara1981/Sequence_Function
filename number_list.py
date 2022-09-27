list_even_number = [ 4, 6, 8, 10, 12, 14  ],
list_odd_number = [ 3, 5, 7, 9, 11, 13, 17 ],

print(min(list_even_number))
print(max(list_even_number))

print(min(list_odd_number))
print(max(list_odd_number))
print()
print(len(list_even_number))
print(len(list_odd_number))

##  DICTIONARY IN PYTHON
vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

my_car = vehicles['fiesta']
print(my_car)

commuter = vehicles['virago']
print(commuter)

learner = vehicles.get("ER5")
print(learner)