# Operators :
# 1. Arithmetics
# 2. Logical:  and or not
# 3. Bitwise : & | ! ^ >>  <<
# 4. Membership : in , not in
# 5. Assignment: = += -= *= ....
# 6. Comparisons: > < <= >=  == !=
# 7. Identity : is , is not

# t1 = (10, 20, 30)
# t2 = (10, 20, 30)
# print(id(t1))
# print(id(t2))
# print(t1 is t2)

# Conditional Statement:
# 1. if
# 2. if else
# 3. elif
# 4. nested if

# wt = int(input())
# if 0 < wt and wt < 2000:
#     print("20min")
# elif 2000 < wt and wt < 4000:
#     print("30min")
# elif 4000 < wt and wt < 7500:
#     print("45min")
# else:
#     print("OVERWEIGHT")


# a = 12
# b = 11
# c = 10

# if a+b >= c and b+c >= a and a+c >= b:
#     print("triangle formed")
# else:
#     print("triangle not formed")

# Looping
# 1. while
# 2. For

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# range(start,stop,step)
# range(10,25,3)  => 10, 13 16 19 22
# range(10,2,-2) => 10 9 8 7 6 5 4 3

# range(9):

# for i in range():


# Function :
# Types of Argument:
# 1. positional
# 2. keyword
# 3. default

# def fun1(first, last="sondawale"):
#     print("inside func1")
#     print(first, last)


# fun1("nikunj")


# def fun2(args):
#     if args < 1:
#         return
#     fun2(args)
#     print(args)
#     args -= 1


# fun2(10)


# m = 5
# n = 5
# lt = [1,2,3,4,5,6,7]
# lt.pop(index)

# def paths(i, j):
#     if i == m-1 and j == n-1:
#         return 1

#     if j == n-1:
#         z = i+1
#         return paths(z, j)

#     if i == m-1:
#         z = j+1
#         return paths(i, z)

#     return paths(i, j+1) + paths(i+1, j)


# print(paths(0, 0))

# def execution(cur, people):
#     if len(people) == 1:
#         print(people[0])
#         return

#     cur = (cur+2) % len(people)
#     people.pop(cur)
#     execution(cur, people)


# people = [1, 2, 3, 4, 5, 6, 7]
# execution(0, people)

# Collections

# 1. List
# 2. Tuples
# 3. Set
# 4. Dictionary

# s = "Nikunj"

# d_s= {'N':1}

# d = {'a': 'apple'}
# print(d['a'])
