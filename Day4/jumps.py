# def min_jumps(arr):
#     if len(arr)==0:
#         return -1
#     jump = 0
#     count = 0
#     while jump <= len(arr)-1:
#         if arr[jump] == 0:
#             return -1
#         jump = jump + arr[jump]
#         count += 1

#     if len(arr)==1:
#         return 1

#     return count


# arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# print(min_jumps(arr))


# def majority_element(arr):
#     plate = []
#     half = len(arr)/2
#     for i in arr:
#         if i not in plate:
#             if arr.count(i) > half:
#                 return i
#         plate.append(i)
#     return -1

# arr = [1, 1, 2, 1, 3, 5, 1]


lt = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10, 22, 11]
window = 4
print(len(lt))
old_sum = 0
p = 0
for i in range(0, len(lt)-window-1):
    new_sum = sum(lt[i:i+window:1])
    if old_sum < new_sum:
        old_sum = new_sum
        p = i

print(old_sum)
print(lt[p:p+window:])


# list slicing
# lt[start:end:step]

# print(lt[4:8:1])
# print(lt[-1:-8:-3])   # 11  53 6
# print(lt[-2:-9:2])
# print(lt[::-1])  # reverse list
# print(lt[::])
# # start => 0
# # stop => n
# # step => 1
