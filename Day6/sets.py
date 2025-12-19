# # set1 = set()
# # set1 = {41, 52, 36, 74}
# # print(set1)

# # set1.add(76)
# # print(set1)
# # set1.add(41)
# # print(set1)

# # set1.remove(36)
# # print(set1)

# # set1.update({85, 23, 14, 52, 96})
# # print(set1)

# # set1.discard(74)
# # print(set1)

# # set1.pop()
# # print(set1)

# # set1.clear()
# # print(set1)

# set1 = {41, 52, 36, 74}
# set2 = {23, 85, 69, 41}

# # print(set1.union(set2))

# # print(set1.intersection(set2))
# # # set2.intersection_update(set1)
# # # print(set1)
# # # print(set2)

# # print(set2.difference(set1))
# # set2.difference_update(set1)
# # print(set1)
# # print(set2)


# # set1 = {41, 52, 36, 74}
# # set2 = {23, 85, 69, 41}

# # print(set1.symmetric_difference(set2))
# # set1.symmetric_difference_update(set2)
# # print(set1)
# # print(set2)

# # print(set1.issubset(set2))
# # print(set1.issuperset(set2))


# # students = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}
# # submitted = {15, 12, 22, 16}
# # print(students.difference(submitted))

# # Dictionary

# # lt = [10, 20, 30]

# # fruits = {
# #     'banana': 23,
# #     'apple': 12
# # }

# # sentence = "i like to eat potato, potato like  i eat sometime forever a little little"

# # word = sentence.split(' ')
# # print(word)

# # set1 = set(word)
# # print(set1)

# # res = {}

# # for i in set1:
# #     res[i] = word.count(i)

# # print(res)


# # set1 = {'i', '', 'a', 'potato,', 'forever', 'little',
# #         'potato', 'to', 'like', 'eat', 'sometime'}
# # for i in set1:
# #     print(i)


# # d = {}

# # d[1] = "one"
# # d['list1'] = [1, 2, 3]
# # d['list'] = [10, 20, 30]

# # print(d)

# d = {'i': 2, 'potato,': 1, 'eat': 2, '': 1, 'little': 2, 'potato': 1,
#      'sometime': 1, 'forever': 1, 'a': 1, 'like': 2, 'to': 1}
# print(d.keys())
# print(d.values())

# print(d.items())

# d.pop('forever')
# print(d)

# print(d.popitem())

# d1 = {
#     1: True,
#     0: False
# }
# d.update(d1)
# print(d)
