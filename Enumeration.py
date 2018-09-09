# coding:utf-8
import time

# 枚举法的应用：a+b+c=1000,a^2+b^2=c^2,求整数a,b,c
start_time = time.time()
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
#                 print ("a, b, c:%d,%d,%d" % (a, b, c))
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print ("a, b, c:%d,%d,%d" % (a, b, c))

end_time = time.time()
print ("计算结束，用时%d秒。" % (end_time - start_time))

# 排列一个列表，sort()方法并不返回列表而是NONE
li = [0, 100, 66, 44, 78, 99, 22]
li.sort()
print li
# reverse()倒排序
li.reverse()
print li

