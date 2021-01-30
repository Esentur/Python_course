#отладка
# a=0
# while True:
#     a+=0.1
#     # print(a)
#     if (a>=1):
#         exit(0)
#     print('Hello')

#exercise
list=[3,5,-2,-8,0]
def findNegativeNum(arr):
    negs=[]
    for n in arr:
        if n<0:
            negs.append(n)
    return negs
print(findNegativeNum(list))
print('Basic part completed')
