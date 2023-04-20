class A:
    def get1(self):
        print('iam a class')
class B:
    def get2(self):
        print('iam b class')
class C(A,B):
    def put(self):
        print('yes iam inherited A&B')
obj=C()
obj.get1()
obj.get2()
obj.put()


