###　寫一個函式　傳入一個list 去掉ODD return even num
def showEven(*args): # *args不限定參數類型可以混搭
    newl = []
    print(args ,type(args)) # *args會將傳入的數字們組成一個tuple (21, 20, 45, 68, 35, 49, 75, 68) <class 'tuple'>
    for val in args: # tuple 這也是為什麼可以iterate it
        if not isinstance(val, int):
            print('傳入的資料必須都是數字型態')
            return
        if val % 2 == 0:
            newl+=[val]
    print(newl)
    return newl

mylist=[21,20,45,68,35,75,68]
showEven(*mylist) # 用*來展開list 變成不定位置的數字


## 縮寫: lambda 搭配 *args寫法 | function statement
newlist =lambda *args: [val for val in args if val % 2 == 0]
print('lambda寫法,fn statement',newlist(*mylist))

## 縮寫: lambda 搭配 *args寫法  | function expression
ne =(lambda *args: [val for val in args if val % 2 == 0])(*mylist)
print('lambda寫法,fn expression',ne)

## 寫一個lambda 可以做加法運算 請直接呼叫
print((lambda x,y: x + y)(888,999))

### js匿名函式
# ((a,b) => a+b)(888,999)
### 匿名函式 作為另一個函式的參數
# setTimeout(() => console.log('每三秒輸出一次'), 3000)

# def math(a,b,f):
#     return f(a,b)

## 匿名函式使用與map()
mylist=[5, 10, 15, 20, 25, 30]

squarlist = list(map(lambda x: x**2, mylist))

print(f'串列平方值= ', squarlist)

num = 322

test =list(map(int, list(str(num))))

print(test)