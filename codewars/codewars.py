'''
A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, 
each raised to the power of the number of digits in a given base.
In this Kata, we will restrict ourselves to decimal (base 10).
For example, take 153 (3 digits), which is narcissistic:
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    and 1652 (4 digits), which isn't:
    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
The Challenge:
Your code must return true or false (not 'true' and 'false') 
depending upon whether the given number is a Narcissistic number in base 10.

This may be True and False in your language, e.g. PHP.

Error checking for text strings or other invalid inputs is not required,
 only valid positive non-zero integers will be passed into the function.
 '''
# 我的解法:
# def narcissistic( value ):
#     teli = list(map(int,str(value))) # => [5] | [1,5,3] | [1,6,5,2]
#     numlen = len(teli) # => length / mutiply
#     # print(num)
#     if numlen == 1: 
#       # value = value**numlen # 長度等於時 等於自己
#         print(f'true, {value} == {value**numlen}')
#         return True
#     else:
#         newli= list(map(lambda x: x**numlen, teli)) # [1, 125, 27] | [1, 1296, 625, 16]
#         total = sum(newli) # 加總list中所有int數字 print(sum(newli))
#         if total == value:
#             print(f'true, {newli} sum is {total} == {value}')
#             return True
#         else:
#             print(f'false, {newli} sum is {total} !== {value}')
#             return False
    

# narcissistic(5)
# narcissistic(153)
# narcissistic(1652)

## 參考解法
# def narcissistic(value):
#     return value == sum(int(x) ** len(str(value)) for x in str(value))

# narcissistic(5)
# narcissistic(153)
# narcissistic(1652)



'''
Move the first letter of each word to the end of it, 
then add "ay" to the end of the word. 
Leave punctuation marks untouched.
'''

def pig_it(text):
    #your code here
    #del 1 letter => the end of 1ay
    textlist = text.split(' ') # str.split('') | ['Hello', 'world']
    print(textlist)
    #firSte = text[0:1] + 'ay' # 提取第一個字 加上-ay
    def changeWord(tlixt):
            if str.isalpha(tlixt): # 使用 str.isalpha() => true or false
                firstr = tlixt[0:1]+"ay"
                remain= tlixt[1:len(tlixt)+1]+firstr  #elloHay 組字串
                print(remain) #elloHay
                return  remain
            else:
                 return tlixt
    an=list(map(changeWord,textlist))
    ' '.join(an)
    print(' '.join(an))
  
    # print(an)
    # return an

# pig_it('Hello world !')

#　參考解法：
def pis_at(text):
    return " ".join([x[1:]+x[0]+'ay' if x.isalpha() else x for x in text.split()])

## lambda 寫法
# def pig_it(text):
#     return ' '.join(list(map(lambda word: word if word in '!?' else word[1:]+word[0]+'ay', text.split(' '))))

# pis_at('Hello world !')