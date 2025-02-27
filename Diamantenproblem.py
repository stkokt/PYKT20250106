class A:
    pass
    # def m(self):
    #     print("Methode von A")

class B(A):
    pass
    # def m(self):
    #     print("Methode von B")

class C(A):
    pass
    # def m(self):
    #     print("Methode von C")

class D(C,B):
    pass

d=D()

d.m()

print(D.mro())