# import bisect
# lt = [8, 23, 26, 34, 56, 57, 76, 87, 97, 524, 556, 872, 3423, 7658, 344357]
# print(len(lt))
# ele = 23
# left = 0
# right = len(lt)-1

# while left <= right:
#     mid = (left+right)//2
#     if ele == lt[mid]:
#         print(lt[mid])
#         break
#     if ele > lt[mid]:
#         left = mid+1
#     if ele < lt[mid]:
#         right = mid-1
