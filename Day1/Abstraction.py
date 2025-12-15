# Abstraction : hiding the implementation,

# Abstract class :  a class which contains one or more abstract methods
# Abstract method : a method that is declared, but contains no implementation
from abc import ABC, abstractmethod           # Abstract Base Class

class Sample(ABC):
    @abstractmethod
    def func1(self):
        pass

    @abstractmethod
    def func2(self):
        pass


class Sample2(Sample):
    def func1(self):
        print("In fun1 of Sample2")

    def func2(self):
        pass


s = Sample2()
s.func1()
