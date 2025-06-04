"""this_list = ["banana", "Orange", "Kiwi", "cherry"]
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
"""





#CHATGPT Practice
#.append()
empty_list = []
name_to_add = "Adair"
empty_list.append(name_to_add)
print(empty_list)


empty_list_2 = []
for _ in range(1, 6):
    empty_list_2.append(_)

print(empty_list_2)


one_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
empty_list_3 = []

for number in one_to_ten:
    if number % 2 == 0:
        empty_list_3.append(number)

print(empty_list_3)


#.clear()
elements_to_delete = [1, 2, 3, "Adair", True]
elements_to_delete.clear()
print(elements_to_delete)

empty_list_4 = []
#user_to_add = str(input("Add a name to add a user: "))
#empty_list_4.append(user_to_add)
print(empty_list_4)
empty_list_4.clear()
print(empty_list_4)


check_length = ["Adair", "Dhayana", "Monserrat"]
#add_name = str(input("Add a name if you want, be careful to not exceed the limit: "))
#check_length.append(add_name)
length = len(check_length)
print(length)

if length >= 4:
    check_length.clear()

print(check_length)


list_to_copy = [True, False, False, True]
copied_list = list_to_copy.copy()
copied_list.append(True)
print(list_to_copy)
print(copied_list)

#This is the same list because makes reference to the same spot in memory
list_to_copy_2 = list_to_copy


#.count()
list_to_count = [1, 3, 3, 5, 3, 7]
times = list_to_count.count(3)
print(times)

word = str(input("Give me a word to count how many vowels are in it: "))
vowels =
counting = word.count(vowels)
print(counting)