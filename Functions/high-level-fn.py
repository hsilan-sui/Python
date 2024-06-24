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

# # from functools import reduce
# # def narcissistic( value ):
# #     testli = list(map(int,list(str(value)))) #[2,1]
# #     mutiNum = len(testli) # 2
# #     add = 0
# #     if mutiNum == 1:
# #         add = value
# #         return True
# #     else:
# #         add = sum(*list(map(lambda x: x^mutiNum ,testli)))
# #         if add == value:
# #             return True
# #         else:
# #             return False
    

# # narcissistic(153)
# # narcissistic(1652)

# data1 = {'甲':(31,56,23),'乙':(31,56,23),'丙':(31,56,23)}

# # 
# def doso(*args):
#     return sum(args)

# print(doso(2,3,45))

# # 
# def dosoo(**argv):
#     return argv # dict

# print(dosoo(name='aa',age=16))


# def narcissistic(value):
#     testli = list(map(int,list(str(value)))) #[2,1]
#     num = len(testli) # 2
#     li = list(map(lambda x: x**num ,testli))
#     print(list(map(int,str(value))))
#     print(sum(li))
    # if mutiNum == 1:
    #     return True
    # else:
    #     li = list(map(lambda x: x^mutiNum ,testli))
    #     # add = sum(*li)
    #     print(value,li)
    #     # if add == value:
        #     print(add)
        #     return True
        # else:
        #     return False
    

# narcissistic(153)
# narcissistic(1652)

def narcissistic( value ):
    teli = list(map(int,str(value)))
    num = len(teli)
    if num == 1: 
      return True
    else:
        newli= list(map(lambda x: x**num, teli))
        if sum(newli) == value:
            print('true')
            return True
        else:
            print('false')
            return False
    

narcissistic(153)
narcissistic(1652)
# 非int就return