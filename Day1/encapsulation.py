class Sample:
    __z = 0
    _a = 100

    def __init__(self, z):
        self.__z = z

    def __func1(self):
        print(self._a+self.__z)

    # Setter method
    def func2(self, p):
        self._a = p
        self.__func1()

    # Getter method
    def func3(self):
        return self._a


class Sample2 (Sample):
    def __init__(self, a):
        self.p = a

    # def func2(self):
    #     print("In Sample2")


s1 = Sample(300)
s2 = Sample2(500)
# print(s2.__a)
# print(s1.__a)
s1.func2(55)
s2.func2(99)
