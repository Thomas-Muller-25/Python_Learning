"""
华摄氏度转为摄氏度

version: 0.1
Author: Franklin
"""
f = float(input('请输入华摄氏度：'))
c = (f - 32) / 1.8
print('%.1f华摄氏度 = %.1f摄氏度' % (f, c))
print(f'{f:.1f}华摄氏度 = {c:.1f}摄氏度')


"""
输入圆的半径计算计算周长和面积

version: 0.1
Author: Franklin
"""
# from math import pi
# radius = float(input('请输入半径：'))
# perimeter = 2 * pi * radius
# area = pi * radius * radius
# print('perimeter: %.2f' % perimeter)
# print(f'area: {area:.2f}')


"""
输入年份判断是不是闰年

version: 0.1
Author: Franklin
"""

# year = int(input('请输入年份：'))
# if (year % 4 == 0 and year % 100 != 0 or
#         year % 400 == 0):
#     print(f'{year}是闰年')
# else:
#     print('%d不是闰年' % year)

"""
乘法口诀表9*9

Version: 0.1
Author: Franklin
"""

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d ' % (i, j, i * j), end="")
#     print()

"""
判断一个数是不是素数

Version: 0.1
Author: Franklin
"""
# from math import sqrt
#
# num = int(input('请输入一个正整数：'))
# end = int(sqrt(num))
# is_prime = True
# for i in range(2, end + 1):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d is a prime' % num)
# else:
#     print(f'{num} is not a prime')

"""
输入两个正整数，计算它们的最大公约数和最小公倍数。
提示：两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。

Version: 0.1
Author: Franklin
"""
# a = int(input('请输入第一个正整数：'))
# b = int(input('请输入第二个正整数：'))
# if a < b:
#     a, b = b, a
# for i in range(b, 0, -1):
#     if a % i == 0 and b % i == 0:
#         print("%d和%d的最大公约数为%d" % (a, b, i))
#         print(f'{a}和{b}的最小公倍数为{a * b // i}')
#         break


"""
打印如下所示的三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

"""
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print('*', end='')
#     print()
#
# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(' ', end='')
#     for k in range(6-i, 6):
#         print('*', end='')
#     print()
#
# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(' ', end='')
#     for k in range(1, 2 * i):
#         print('*', end='')
#     print()
"""
寻找所有水仙花数

说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，
例如：$1^3 + 5^3+ 3^3=153$。

Version: 0.1
Author: Franklin

"""

# for i in range(100, 1000):
#     low = i % 10  # 个位
#     mid = i % 100 // 10  # 十位
#     high = i // 100  # 百位
#     if low**3 + mid**3 + high**3 == i:
#         print(i)

"""
正整数反转，例如：将12345变成54321

Version: 0.1
Author: Franklin
"""

# x = int(input('请输入一个正整数'))
# while x != 0:
#     tmp = x % 10
#     x //= 10
#     print(tmp, end='')

# num = int(input('请输入一个正整数'))
# reversed_num = 0
# while num != 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)

"""
百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，
用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？

Version: 0.1
Author: Franklin
Date: 2024-04-23
"""

# for i in range(0, 21):
#     for j in range(0, 34):
#         k = 100 - i - j
#         if i*5 + j*3 + k/3 == 100:
#             print(f'公鸡：{i}，母鸡：{j}，小鸡：{k}')


"""
CRAPS赌博游戏。

说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。

Version: 0.1
Author: Franklin
Date: 2024-04-23
"""

# from random import randint
#
# not_win_flag = True
# count = 0
# first = randint(1, 6) + randint(1, 6)
# count += 1
# if first == 7 or first == 11:
#     print('玩家胜，第%d次摇出的点数为%d' % (count, first))
#     not_win_flag = False
# elif first == 2 or first == 3 or first == 12:
#     print('庄家胜，第%d次摇出的点数为%d' % (count, first))
#     not_win_flag = False
#
# while not_win_flag:
#     tmp = randint(1, 6) + randint(1, 6)
#     count += 1
#     if tmp == 7:
#         print('庄家胜，第%d次摇出的点数为%d' % (count, tmp))
#         not_win_flag = False
#     elif tmp == first:
#         print('玩家胜，第%d次摇出的点数为%d' % (count, tmp))
#         not_win_flag = False
#     else:
#         continue

"""
生成斐波那契数列的前20个数。

说明：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）在《计算之书》中提出一个在理想假设条件下兔子成长率的问题而引入的数列，
所以这个数列也被戏称为"兔子数列"。
斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，
形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。

Version: 0.1
Author: Franklin
Date: 2024-04-23
"""
#
# x = 1
# y = 1
# print(x, end=', ')
# print(y, end=', ')
# for i in range(2, 20):
#     num = x + y
#     y = x
#     x = num
#     if i != 19:
#         print(num, end=', ')
#     else:
#         print(num)

"""
找出10000以内的完美数。

说明：完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。

Version: 0.1
Author: Franklin
Date: 2024-04-23
"""

# for i in range(1, 10001):
#     sum = 0
#     for j in range(1, i):
#         if i % j == 0:
#             sum += j
#     if sum == i:
#         print(i)

"""
输出100以内所有的素数。

说明：素数指的是只能被1和自身整除的正整数（不包括1）

Version: 0.1
Author: Franklin
Date: 2024-04-23
"""

# for i in range(2, 100):
#     flag = True
#     for j in range(2, i):
#         if i % j == 0 and i != j:
#             flag = False
#             break
#     if flag:
#         print(i)


