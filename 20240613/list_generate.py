# [2,9,12,33] -> [4,9,24,33]

# 正常寫法:
# li=[2,9,12,33]
# newli=[]
# for num in li:
#     if num % 2 == 0:
#         (num:=num*2) 
#     newli.append(num)
# print(newli)

# list comprehensive寫法:
# print(newli:=[num * 2 if num % 2 ==  0 else num for num in [2,9,12,33]])

# 正常寫法:
# for num in li:
#     if num % 2 == 0:
#         newli.append(num*2)
#     else:
#         newli.append(num)
# print(newli)

# list comprehensive寫法:
# print(newli:=[num * 2 if num % 2 == 0 else num for num in [2,9,12,33]])

# [9, 58, 63, 100] -> > 60 -> [63,100]
# li=[9, 58, 63, 100] 
# newli=[]
# for num in li:
#     if num > 60:
#         newli.append(num)
# print(newli)

# print(newli:=[num for num in [9, 58, 63, 100] if num > 60])


# 再輸入一個人名 # 禁用in
# nlist=['arron','andy','apple','arron']

# (keyin:=input('請輸入一個人名:'))

# if bool(nlist.count(keyin)): # find()
#     print('有參加')
# else:
#     print('無參加')

## 回應: 有參加 無參加

# in 寫法(value in list)
# if keyin in nlist:
#     print('有參加')
# else:
#     print('無參加')

# print(bool({})) F
# print(bool(())) F

# for .. in 搭配 list.index(keyword) 可以得到index 
# nlistt=['arRron','andy','apple','JESS','CHESS']
# for n in nlistt:
#     if n == keyin:
#         indice = nlistt.index(n)
#         print(f'有,並且{n}在nlistt的第{indice}位置')
#         break
# else:
#     print(f'無此資料')
str='abcdefghijklmnopqrstuvwxyz'
for w in str:
    ind=str.index(w)
    print(f'{ind}, {w}')

nlistt=['arRron','andy','apple','JESS','CHESS']
for n in nlistt:
    indice = nlistt.index(n)
    print(f'{indice}, {n}')

# enumerate()
for i,val in enumerate(nlistt):
    print(val) # tuple(key, value)

# enumerate()
for val in enumerate(nlistt):
    print(val) # tuple(key, value)

# 九九乘法表
for k in range(1,10):
    for i in range(2,10):
        print(f'{i} X {k} = {i * k:2d}', end="\t")
    print()


# star 1-5層
# li=[]
# for i in range(1,6):
#     li+=['*']
#     print(''.join(li))

# lii=['1','2']
# print(''.join(lii))
# print()''.join(lii))

 