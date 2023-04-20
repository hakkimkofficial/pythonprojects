class A:
    def __init__(self,name,hodname):
        self.name=name
        self.hodname=hodname
    def getData(self):
        self.name=input('enetr your name')
class B(A):

    def putData(self):
        self.hodname=input('enter hod name')
    def display(self):
        print('student name is',self.name)
        print('hod name is',self.hodname)

class C(B):
    def fun3(self):
        print('this is C class')

class D(C):
    def fun4(self):
        print('this is D class')
obj=D('','')
obj.getData()
obj.putData()
obj.display()
obj.fun3()
obj.fun4()

