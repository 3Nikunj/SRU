from encapsulation import Sample

class Another:
    def method(self):
        s = Sample(100000)
        print(s._a)


an = Another()
an.method()


