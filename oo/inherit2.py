class A:
    def p(self):
        print("A Called")

class B:
    def p(self):
        print("B Called")

class C(A, B):
    pass

class D(C):
    pass


cinstance = C()
cinstance.p()