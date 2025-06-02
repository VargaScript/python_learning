unordered_list = [12, 2, 32, 19, 57, 22, 14]
ordered_list = sorted(unordered_list)

mixed_unordered_list = ["Adair", "adair", "Dhayana"]
mixed_ordered_list = sorted(mixed_unordered_list, reverse=True)

print(ordered_list)
print(mixed_ordered_list)


sorted_list_method = mixed_unordered_list.sort(reverse=True)

print(mixed_unordered_list)


time_list = [12, 2, 32, 19, 57, 22, 14]

minimum_value = min(time_list)
maximum_value = max(time_list)
print(minimum_value, maximum_value)