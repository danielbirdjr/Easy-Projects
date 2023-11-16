# DIFFERENCE BETWEEN
# LIST - [ ], mutable - can change
# TUPLE - ( ), inmutable - can't change
# SET - set keyword & ([ ]); no duplicate items
# DICTIONARY - { }, made up of key-value pairs; think word & definition

list1 = ["Computer", "Printer", "TV", "Camera", 89, 30.8]
list1[0] = "PC"
print(list1)

tuple1 = ("Computer", "Printer", "TV", "Camera", 89, 30.8)
# can't change any of the values
print(tuple1)

set1 = set(["Computer", "Computer", "Printer", "TV", "Camera", 89, 30.8])
print(set1)

dict1 = {
  1: "Monday", 
  2: "Tuesday"
}
print(dict1)