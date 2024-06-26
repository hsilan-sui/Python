# 適合用在效能量測

# def c(func):
#     def b():
#         print('在函式執行前，做一些操作')
#         func()
#         print("在函式執行後，做一些操作")
#     return b

# @c
# def a():
#     print("I'm a")

# a()

# def b(func):
#     def wrapper(name, age):
#         print('請問你叫什麼名字?幾歲?')
#         func(name, age)
#         print('好的已收到資料')
#     return wrapper

# @b
# def a(name, age):
#     print(f'名字叫{name},年齡是{age}歲')

# a('sui',2)

# def b(func):
#     def wrapper(name, age):
#         print('請問你叫什麼名字?')
#         # Here you can prompt for user input if you want
#         # For simplicity, I'll assume you directly pass name and age
#         func(name, age)
#         print('好的已收到資料')
# #     return wrapper
# import random
# print(vars(random))
# AOP & DECORATOR 注入模組-hook api | AOP 縱向物件導向 
import random 
def my_decorator(executedFn):
    def wrapFn(x,y):
        a = executedFn(x, y)
        
        with open('random.txt', 'w', encoding="utf-8") as file:
            file.write(str(a))
        return a
    return wrapFn


for ky,val in vars(random).items():
    if ky == 'randint':
        print(ky, val) # randint <bound method Random.randint of <random.Random object at 0x000001A0216FA8B0>>
        vars(random)[ky] = my_decorator(val)
   

executed_randint = random.randint(1,7)

print(executed_randint)