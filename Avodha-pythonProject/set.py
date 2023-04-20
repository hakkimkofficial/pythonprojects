# set1={'a','b','c','d'} #---- or set1=set(('a','b','c','d'))
# print('f' in set1)
# set1.add('e')
# print(set1)
# set1.update(['f','g','h'])
# print(set1)
# print(len(set1))
# set1.remove('h')
# print(set1)
# set1.discard('g')
# print(set1)
# set1.pop()
# print(set1)
#--------set union------
# set1={'a','b','c'}
# set2={1,2,3,4}
# # set3=set1.union(set2) or
# set3=set1| set2
# print(set3)
# set1.update(set2)
# print(set1)
#-----set intercept(difference)
set1={1,2,3,4 }
set2={2,3,4,5}

set3=set2-set1
print(set3)
set3=set1-set2
print(set3)





