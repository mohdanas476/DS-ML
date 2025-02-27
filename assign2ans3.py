## MODIFIES THE LIST USING APPEND
def append_item(lst,item):
    lst.append(item) # Add item to the list
mylist = [1,2,3]
print('Before ',mylist)

append_item(mylist, 4) # Append 4 to the list
print('After',mylist)
