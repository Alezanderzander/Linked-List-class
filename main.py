from linked_list import *

list = linked_list()
list.add("a")
list.add("b")
list.add("d")

list.insert_after("c",1)
list.insert_after("e",2)
list.insert_after("f",3)
list.insert_after("g",4)
list.insert_after("h",5)
list.insert_after("x",8)

print("size:", list.size)

print([list.get(i) for i in range(-1,list.size)])