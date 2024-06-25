# 程式異常 exception
# def division(x,y):
#     try:
#         return x / y
#     except ZeroDivisionError:
#         print("除數不可為零")
#     except TypeError:
#         print("除數只能是int 型態")
#     return 'done'

# print(division(5,0))
# print(division('a',0))
# print(int(division(10,5)))

school=[43,52,26,33,91,5,11]
stu=[78,63,45,88,37,92]
stulow=min(stu)
print(stulow)

def cacu(*args):
    aver = sum(args) / len(args)
    # print(f'average{round(aver,2)}')
    print(f'這個班級的最低分是{stulow}分')
    print(f'全校總平均是{int(aver)}分')
    return int(aver)
   

# 班上學生最低分 跟學校平均
cacu(*school)
