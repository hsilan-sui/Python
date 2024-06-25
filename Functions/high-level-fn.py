# filter()
## 有一個LIST 只想要純數字的list trim掉文字
# a = [3, 'gg',99,'dd',87,'x']

# def purNum(x):
#     if isinstance(x, int): # 只有
#         return x 
       
# pureNum = list(filter(purNum, a))
# print(pureNum)

# a = [3, 'gg',99,'dd',87,'x']
# pureNum = list(filter(lambda x: [val for val in a if isinstance(val,int)], a))
# print(pureNum)

# [3,4,5]


# map()

grade=[21,55,35,85,69,96,87]

# def addNum(x):
#     if x < 60:
#        return x + 10
#     else:
#         return x
    
# upNum=list(map(addNum, grade))
# upNum=list(map(lambda x: x + 10 if x < 60 else x, grade))
# print(upNum)


from functools import reduce
# reduce()

# num= [1,2,3]

# addup=reduce(lambda x,y: x + y, num, 0)
# print(addup)


# def narcissistic( value ):
#     if not isinstance(value, int):
#         return
#     testli = list(map(int,list(str(value)))) #[2,1]
#     mutiNum = len(testli) # 2
#     if len(testli) > 1:
#         add = reduce(lambda x,y: x + y, list(map(lambda x: x^mutiNum,testli)),0)
#         print(add)   
#     # if add == value:
#     #     return True
#     # else:
#     #     return False
# print(narcissistic(153))

# a = [23,47,15,98,15,62]

# # def compare(x,y):
# #     if x < y:
# #         return x
# #     else:
# #         return y
 
    
# # # c = reduce(compare, a)
# # d = reduce(lambda x,y: x if x < y else y, a)


# # print(d)

# data={'aa': 13, 'bb': 45, 'cc': 22}
# # j = tuple(data.values())
# # print(j)

# def dosome(x,y):
#     if data[x] > data[y]:
#         return y
#     else:
#         return x
# # s=reduce( lambda x,y: x if x < y else y, data.values())
# s=reduce(dosome, data.keys())
# print(s)

