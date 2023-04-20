# x=lambda a:a+2
# print(x(5))
#
# def fun(a):
#     print(a+2)
# fun(5)
#
# x=lambda a,b,c:a*b+5+c
# print(x(2,6,8))
#----function program-----
# def multiply(n):
#     return lambda a:a*n
# num1=multiply(6)
# print(num1(11))
#
# num2=multiply(7)
# print(num2(11))
#----------filter() map() reduce() using lambda
list1=[1,2,3,4,5,6,7,8,9]
list2=filter(lambda n:n%2==0 ,list1)
list3=map(lambda n:n*2,list1)
from functools import reduce
x=reduce(lambda q,p:q+p,list1)


print(list1)
print(list(list2))
print(list(list3))
print(x)






