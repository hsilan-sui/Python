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

def b(func):
    def wrapper(name, age):
        print('請問你叫什麼名字?幾歲?')
        func(name, age)
        print('好的已收到資料')
    return wrapper

@b
def a(name, age):
    print(f'名字叫{name},年齡是{age}歲')

a('sui',2)

# def b(func):
#     def wrapper(name, age):
#         print('請問你叫什麼名字?')
#         # Here you can prompt for user input if you want
#         # For simplicity, I'll assume you directly pass name and age
#         func(name, age)
#         print('好的已收到資料')
#     return wrapper