def subtract(x1, x2):
    """減法設計"""
    result = x1 - x2
    print(result)


# a = eval(input("a = ")) # input from user
# b = eval(input("b = ")) # input from user
# print("a - b = ",end="") # output str, no new line
# subtract(a, b)

def interest(interest_type, subject = 'HEAVEN'): # 有給定參數預設值的parameter要放在後面
    """"show interest and topic"""
    print(f'我的興趣是 {interest_type}')
    print(f'在{interest_type} 中,最喜歡的是{subject}')
    print()

interest('travel') # 只傳遞一個參數 另一個預設值
interest(subject = 'HEAVEN', interest_type='travel')