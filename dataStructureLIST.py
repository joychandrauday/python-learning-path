# list #
first_list = [10, 20, 30, "apple", True]
# print(first_list[-1])

# changing items
first_list[-1] = 99
# print(first_list)        # [10, 20, 30, 'apple', 99]

# Slicing Items
# print(first_list[1:3])      # 1 to 2 Positioned Elements: [20, 30]

# Adding Items 
first_list.append(True)
# print(first_list)        # [10, 20, 30, 'apple', 99, True]
first_list.insert(6,"Sixth Position")
# print(first_list)        # [10, 20, 30, 'apple', 99, True, 'Sixth Position']

# Removing Items
first_list.remove("Sixth Position")
# print(first_list)        # [10, 20, 30, 'apple', 99, True]
first_list.pop(5)
# print(first_list)        # [10, 20, 30, 'apple', 99]
first_list.clear()
print(first_list)        # []: empty array

num_list = [1, 2, 7, 4, 3, 5, 6]

# length
# print(len(num_list))  # Output: 7

# sort the list (in-place)
num_list.sort()
# print(num_list)       # Output: [1, 2, 3, 4, 5, 6, 7]

# reverse the sorted list (in-place)
num_list.reverse()
# print(num_list)       # Output: [7, 6, 5, 4, 3, 2, 1]