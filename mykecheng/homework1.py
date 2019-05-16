#coding utf-8

import random

# 数字1，以00001的格式输出
a = 1
print('%05d' % a )


# hello_new _word 以'_'切割，在屏幕上输出
s = 'hello_new_word'
s_split = s.split('_')
for item in s_split:
    print(item)


#打印9*9乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('%d * %d = %2d ' % (j, i, i*j),end='')
    print()


#输出1000以内的完全数
for i in range(1, 1001):
    sum = 0
    list = []
    for j in range(1,i):
        if i % j == 0:
            list.append(j)
            sum = sum+j
    if sum == i:
        print(i)

# #猜数字
# key = random.randint(1, 100)
# a = 1
# b = 100
# # print(key)
# while 1:
#     guess = int(input("请输入一个%d" % a+'-%d' % b +"的数字"))
#     if guess == key:
#         print("猜对了，喝酒哦")
#         break
#     elif (guess < key):
#         a = guess
#         print("猜小了哦，请输入一个%d" % guess+"-%d" % b+"的数字")
#     elif (guess > key):
#         b = guess
#         print("猜大了，请输入一个%d" % a + "-%d" % guess + '的数字')


