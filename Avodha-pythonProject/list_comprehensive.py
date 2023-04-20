#ordinary program to square of 10 nos----
# def square():
#     for i in range(10):
#         print(i*i)
#square()
#-----comprehencive program to square of 10 nos
# li=[i*i for i in range(10)]
# print(li)

#ordinary program--------
# letters=[]
# for i in "avodha":
#     letters.append(i)
# print(letters)
#-----list comprehencive---
# letters=[i for i in "avodha"]
# print(letters)


# even nos program------
# even=[]
# for i in range(10):
#     if i%2==0:
#         even.append(i)
# print(even)

#list comprehencive program-----
# even=[i for i in range(10) if i%2==0]
# print(even)

#list comprehencive program tofind even numbers ofpower of 2
list=[1,4,5,8]
even=[i**2 for i in list if i%2==0]
print(even)
