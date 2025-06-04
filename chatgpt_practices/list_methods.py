this_list = ["banana", "Orange", "Kiwi", "cherry"]
this_list.sort(key=str.upper)

print(this_list)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist.reverse()

print(thislist)

thisnewlist = thislist.copy()
thisnewlist.reverse()

print(thisnewlist)

list(thislist)
print(thislist)

newerlist = thislist[:]
print(newerlist)

sumlist = thislist + newerlist
print(sumlist)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1.extend(list2)
print(list1)

for item in list1:
    list2.append(item)

print(list2)






#CHATGPT Practice
