# # List
# # Sets'63', 10,
# # Tuples
# # Dictionaries
# # Strings

# # Lists : Collections of items that are ordered and mutable. Allows duplicate members.
# my_list = []
# # print(my_list[0])  # This will raise an IndexError since the list is empty

# my_list = []
# # for i in range(5):
# #     my_list.append(input("Enter item: "))  # Appending user inputs to the list

# # print(my_list)  # Displays the list with user inputs

# my_list = ['100 200 300 400 500', '55', '52', '55', '63']

# my_list.insert(-1, 500)  # Inserting 500 at the second last position
# my_list.insert(2, 600)
# # print(my_list)

# list1 = [10, 20, 30, 40, 50]

# my_list.extend(list1)  # Extending the list with another list
# print(my_list)

# list2 = ['a', 'b', 'c']

# my_list = my_list + list2    # Concatenation
# print(my_list)
# # int[] arr = new int[5];
# # [0 0 0 0 0]


# list = ['55', 600, '52', '55', 500, '63', 10, 20, 30, 40, 50, 'a', 'b', 'c']
# print(len(list))   # Length of the list

# list.remove('55')  # Removes the first occurrence of '55'
# print(list)

# z = list.pop(5)  # Removes and returns the last item or specidied index
# print(list)
# print("Popped item:", z)

# del list[5]   # Deletes the item at index 5
# print(list)

# list.clear()  # Clears the entire list
# print(list)

# list = [55, 600, 52, 55, 500,  20, 30, 40, 50]
# a = list.index(55)  # Returns the index of the first occurrence of '55'
# print(a)

# print(list.count(500))  # Counts how many times '55' appears in the list

# list.reverse()  # Reverses the list
# print(list)

# list.sort()  # Sorts the list in ascending order
# print(list)

# list.sort(reverse=True)  # Sorts the list in descending order
# print(list)

# list1 = list.copy()  # Creates a shallow copy of the list
# print(list1)


list = [55, 600, 52, 55, 500,  20, 30, 40, 50]

print(max(list))  # Returns the maximum value in the list
print(min(list))  # Returns the minimum value in the list

print(sum(list))  # Returns the sum of all elements in the list

print(sorted(list))  # Returns a new sorted list without modifying the original list
print(list)  # Original list remains unchanged
