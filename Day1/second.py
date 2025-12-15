# class Sample:
#     a = 100
#     sourse = ""
#     dest = ""
#     fair = 0

#     def __init__(self, s, d, f):
#         self.sourse = s
#         self.dest = d
#         self.fair = f

#     def func1(self, first):
#         print(self.sourse, self.dest, self.fair)
#         print(first)


# s1 = Sample("A", "B", 30)
# s2 = Sample("A", "C", 50)
# s1.func1("Nikunj")
# s2.func1("Popo")


# OOPs
# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism

# Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Hybrid Inheritance

# class Sample:    # Base Class
#     a = 100
#     b = 0

#     def __init__(self, b):
#         self.b = b

#     def func1(self):
#         print(self.a + self.b)


# class Sample2 (Sample):   # Derived Class
#     z = 500
#     x = 0

#     def __init__(self, x):
#         self.x = x

#     def func2(self):
#         print("In Sample2")

# class Sample3 (Sample):
#     p = 700
#     q = 0

#     def __init__(self, q):
#         self.q = q

#     def func3(self):
#         print("In Sample3")


# s1 = Sample(200)
# s2 = Sample2(300)
# s1.func1()
# s2.func2()
# s2.func1()
# s3 = Sample3(400)

# class Sample:
#     z = 0
#     a = 100

#     def __init__(self, z):
#         self.z = z

#     def func1(self):
#         print(self.a+self.z)


# class Sample2 (Sample):
#     def __init__(self, z, a):
#         super().__init__(z)
#         self.a = a

#     def func2(self):
#         print("In Sample2")


# s2 = Sample2(20, 10)
# print(s2.func1())


# Encapsulation 

# public 
# private __  : It's accessible only within the class, but by using getter and setter 
#               methods we can utilze the private members outside the class.
# protected  _ : It's accessible within the class, outside class and inside the same package,
#                but it's recommended to use it within the class and subclass only.