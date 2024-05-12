# # 三种字符串表示方式
# str1 = 'hello world'
# str2 = "hello world"
# str3 = """
# hello
# world
# """
# print(str3)
#
# #\反斜杠为转义字符
#
# #
# s1 = '123456789'
# print(s1)
# print('ll' in s1)
# print('nice' not in s1)
#
# # slice
# # odd
# print(s1[0::2])
# # even
# print(s1[1::2])
# # reverse
# print(s1[::-1])
# # From 1 to 5
# print(s1[0:5])

# # 内置函数对字符串进行操作
# str1 = 'hello world'
# # 内置函数len()计算长度
# print(len(str1))
#
# # capitalize() 获得字符串首字母大写的拷贝
# print(str1.capitalize())
#
# # title() 获得字符串每个单词首字母大写的拷贝
# print(str1.title())
#
# # upper() 获得字符串变大写后的拷贝
# print(str1.upper())
#
# # find() 从字符串中查找字串的位置
# print(str1.find('llo')) # 找得到返回子串开头所对应的下标
# print(str1.find('fxxk')) # 找不到返回-1
#
# # index()和find()类似，但找不到子串会引发异常
# print(str1.index('llo'))
# # print(str1.index('fxxk')) # ValueError: substring not found
#
# # startswith() 检查字符串是否以指定字符串开头
# print(str1.startswith('hel'))
# print(str1.startswith('money'))
#
# # endswith() 检查字符串是否以指定字符串结尾
# print(str1.endswith('ld'))
#
# # center() 将字符串以指定的宽度居中并在两侧填充指定的字符
# print(str1.center(50, '$'))
# print(str1.center(100, '¥'))
import random
import sys


#
# f = [x for x in range(10)]
# print(f)
#
# f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f)

# f = [x ** 2 for x in range(1, 1000)]
# print(sys.getsizeof(f))
# # print(f)

#
# f = (x ** 2 for x in range(1, 1000))
# print(sys.getsizeof(f))
# for n in f:
#     print(n)

#
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a
#
# f= fib(6)
# for i in f:
#     print(i, end=' ')

# tuple不可以改， list可以改
# list = [1, 'a', 123, True]
# print(list)
#
# tuple = (1, 'a', 123, True)
# print(tuple)
#
# list[0] = 123
# print(list)


# set1 = {1, 2, 3, 3, 2, 1}
# set1.update([11, 12])
# print(set1)
# set1.discard(5)
# set1.remove(5)
# print(set1)

#
# scores = { int: 95, '白元芳': 78, '狄仁杰': 82}
# print(scores[int])
# scores.update({"christal": 123})
# scores.update(冷面=67, 方启鹤=85,)
# print(scores)
# for key in scores:
#     print(f'{key}:',scores[key])

# 在屏幕上显示跑马灯文字。
# import os
# import time
#
# content = "I want to be an Artificial intelligence Exp"
# while True:
#     os.system('clear')
#     print(content)
#     time.sleep(0.2)
#     content = content[1:] + content[0]


# 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
# import random
# def generate_code(code_len=4):
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         pos = random.randint(0, last_pos)
#         code += all_chars[pos]
#     return code
#
#
# print(generate_code())

# 设计一个函数返回给定文件名的后缀名。
def get_suffix(file_name, has_dot=False):
   pos = 0
   for i in range(len(file_name)):
       if file_name[i] == '.':
           pos = i
   # '.' 不是第一个或者最后一个字符
   if 0 < pos < len(file_name) - 1:
       index = pos if has_dot else  pos + 1
       return file_name[index:]
   else:
       return ''

# def get_suffix(file_name, has_dot = False):
#     pos = file_name.rfind('.')
#     if 0 < pos < len(file_name) - 1:
#         index = pos if has_dot else pos + 1
#         return file_name[index:]
#     else:
#         return ''


# print(get_suffix('test_module.py', True))

# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
def max2(x):
    if len(x) < 2:
        return 'Error, too short'
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 =x[index]
    return m1, m2


x = [random.randint(0, 10) for _ in range(10)]
print(x)
print(max2(x))


# 练习5：计算指定的年月日是这一年的第几天。

days = [31, 28, 31, 30, 31, ]
