class A:
    def method(self):
        print("Method from class A")


class B(A):
    def method(self):
        print("Method from class B")


class C(A):
    def method(self):
        print("Method from class C")


class D(B, C):
    def method(self):
        print("Method from class D")



print("MRO for class A:", A.__mro__)
print("MRO for class B:", B.__mro__)
print("MRO for class C:", C.__mro__)
print("MRO for class D:", D.__mro__)
