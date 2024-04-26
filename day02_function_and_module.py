"""
输入M和N计算C(M,N)

Version: 0.1
Author: Franklin
Date: 2024-04-23
"""

# def fac(num):
#     result = 1
#     for i in range(1, num + 1):
#         result *= i
#     return result
#
#
# m = int(input('m = '))
# n = int(input('n = '))
#
# if m < n:
#     tmp = m
#     m = n
#     n = tmp
#
# print(fac(m) // fac(n) // fac(m - n))

"""
可变参数
"""
# def add(*args):
#     total = 0
#     for val in args:
#         total += val
#     return total
#
#
# print(add(1, 2, 3, 4, 5, 6))

# from test_module import foo
# foo()

"""
实现计算求最大公约数和最小公倍数的函数。

Version: 0.1
Author: Franklin
Date: 2024-04-23
"""

#
# def gcd(m, n):
#     if m < n:
#         # tmp = m
#         # m = n
#         # n = tmp
#         m, n = n, m
#     r = m % n
#     while r:
#         m = n
#         n = r
#         r = m % n
#     print(f'最大公约数为{n}')
#     return n
#
# def lcm(m, n):
#
#     print(f'最小公倍数为' + str(m * n // gcd(m, n)))
#
# lcm(15, 35)


"""
实现判断一个数是不是回文数的函数。

Version: 0.1
Author: Franklin
Date: 2024-04-23
"""


# def is_palindrome(num):
#     tmp = num
#     result = 0
#     while tmp != 0:
#         result = result * 10 + tmp % 10
#         tmp //= 10
#         print(result,tmp)
#     if result == num:
#         return True
#     else:
#         return False
#
# # print(is_palindrome(141))
#
# def is_prime(num):
#     flag = True
#     for i in range(2, num):
#         if num % i == 0 and num != i:
#             flag = False
#             break
#     if flag:
#         return True
#     else:
#         return False
#
# print(is_prime(37))