# def subtract(x1, x2):
#     """減法設計"""
#     result = x1 - x2
#     print(result)


# a = eval(input("a = ")) # input from user
# b = eval(input("b = ")) # input from user
# print("a - b = ",end="") # output str, no new line
# subtract(a, b)

# def interest(interest_type, subject = 'HEAVEN'): # 有給定參數預設值的parameter要放在後面
#     """"show interest and topic"""
#     print(f'我的興趣是 {interest_type}')
#     print(f'在{interest_type} 中,最喜歡的是{subject}')
#     print()

# interest('travel') # 只傳遞一個參數 另一個預設值
# interest(subject = 'HEAVEN', interest_type='travel') # 都有給定引數不需要照順序

## Function return & 回傳值
### return
# def showme(name, age, phone):
#     """"practice return and test data"""
#     if not isinstance(name, str):
#         print(f'error!Name must be str type')
#         return # 中斷函式
#     if not isinstance(age, int):
#         print(f'error!age must be int type')
#         return # 中斷函式
#     if not isinstance(phone, int):
#         print(f'error!phone must be int type')
#         return # 中斷函式
    
#     print(f'{name}, {age} years old,contact num is {phone}')

# showme('jason', '43', 886934655844)

###　寫一個函式　傳入一個list 去掉ODD return even num
# def showEven(*args): # *args不限定參數類型可以混搭
#     newl = []
#     print(args ,type(args)) # *args會將傳入的數字們組成一個tuple (21, 20, 45, 68, 35, 49, 75, 68) <class 'tuple'>
#     for val in args: # tuple 這也是為什麼可以iterate it
#         if not isinstance(val, int):
#             print('傳入的資料必須都是數字型態')
#             return
#         if val % 2 == 0:
#             newl+=[val]
#     print(newl)
#     return newl

# mylist=[21,20,45,68,35,(4,3,4),75,68]
# showEven(*mylist) # 用*來展開list 變成不定位置的數字

### 多筆資料回傳 =>仍是只有一個回傳值(tuple)
# def mitifun(x1, x2):
#     add = x1 + x2
#     sub = x1 - x2
#     mul = x1 * x2
#     div = x1 / x2
#     return add, sub, mul, div # 多筆資料的回傳(但原則上只有一筆回傳值=>Tuple(add, sub, mul, di)) 

# answer = mitifun(50,2)
# print(answer, type(answer)) #(52, 48, 100, 25.0) <class 'tuple'>

# val1, val2, val3, val4 = mitifun(50,2) #另做tuple解包
# print(val1, val2, val3, val4)



# newEven = [val for val in args if val % 2 == 0]

# mylist=[21,20,45,68,35,(4,3,4),75,68]
# showEven(*mylist) 

# def showEven(li): # *args不限定參數類型可以混搭
#     return [val for val in li if val % 2 == 0]

# li = [2,3,4,5,6,7,8]
# # a = showEven(li)
# # print(a)

# k = lambda li: [val for val in li if val % 2 == 0]
# # K is 匿名函式()
# print(k(li))

# def showEven(*args): # *args不限定參數類型可以混搭
#     newl = []
#     for val in args:
#         if val % 2 == 0:
#             newl+=[val]
#     return newl

# newEven = [val for val in args if val % 2 == 0]

# mylist=[21,20,45,68,35,(4,3,4),75,68]
# showEven(*mylist) 
# nli = [2,3,4,5,6,7,8]

# def showEven(): # *args不限定參數類型可以混搭
#     return [val for val in li if val % 2 == 0]

k = lambda *args: [val for val in args if val % 2 == 0]
print(k(*[2,4,5,6,7,8,9]))