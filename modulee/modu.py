# import bs4
# import mathh
#  # 引用模組
# '''
# 模組的命名(=變數規則)要注意:
# 1.不能是數字
# 2.可以底線開頭 
# 3.不能數字開頭
# 4. - $不能被命名S=
# '''
# print(mathh.add(10,20))

# htmlFile = requests.get('https://www.tenlong.com.tw/')
# objSoup = bs4.BeautifulSoup(htmlFile.text, 'lxml')
# print(type(objSoup)) # 有獲得資料類型

# htmlFile =open('myhtml.html', encoding="utf-8")
# objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
# print(type(objSoup))

# import random
# a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# answer = ''.join(random.sample(a, 4))
# print(answer)

# count = 0

# while True:
#     guess = input('請輸入一個四位數字：')
#     count += 1

#     try:
#         int(guess)
#     except ValueError: 
#         print('the input must be numbers')
#         continue

#     if len(guess) != 4:
#         print('the input is only for 4 digital numbers')
#         continue

#     if len(set(guess)) != 4:
#         print('the input must be non-repeat 4 digital numbers')
#         continue

#     # num&addr -> A ; num & !addr ->B
#     get_a=0
#     if guess[0] == answer[0]:
#         get_a += 1
#     if guess[1] == answer[1]:
#         get_a += 1
#     if guess[2] == answer[2]:
#         get_a += 1
#     if guess[3] == answer[3]:
#         get_a += 1

#     get_b=0 
#     if guess[0] in answer and guess[0] != answer[0]:
#         get_b += 1
#     if guess[1] in answer and guess[1] != answer[1]:
#         get_b += 1
#     if guess[2] in answer and guess[2] != answer[2]:
#         get_b += 1
#     if guess[3] in answer and guess[3] != answer[3]:
#         get_b += 1
#     print(f'有{get_a}A, {get_b}B')

#     if guess == answer:
#         print('***bingo***! this is the right answer')
#         break

    
#print(set(answer)) #{'8', '2', '9', '5'}
# print(answer.count(user[0]))

# (num:=int(input('請輸入數字:')))
# #1 5 2 4
# def dosome(x,y):
#     return x*y
# => snowball
