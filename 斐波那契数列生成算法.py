#定义一个生成器去按需生成数列的元素(调用通知的时候再去拿数据)
# def fib(n):
#     #定义2个初始值
#     a,b = 0,1
#     for i in range(n):
#         yield b
#         #下一次执行的代码---必须保证每次a,b都变化
#         a,b = b,a+b
#     pass
#
# if __name__ == '__main__':
#     for item in fib(5): #---生成5个数的斐波那契数列----每次调用都通知生成器去拿数据
#         print(item,end=' ')
#         pass

# def fib2():
#     a,b = 0,1
#     for i in range(5): #每次生成的数都放在了内存中
#         if i == 0 or i == 1:  #逻辑运算符 and or
#             print(b,end=' ')
#         else:
#             a,b = b,a+b
#             print(b,end=' ')
#         pass
#     pass
# fib2()
'''输出1000以内的斐波那契数列'''
# def fib3():
#     a,b = 0,1
#     while b < 1000: #斐波那契是从1开始的数列
#         print(b,end=' ')
#         #每次让b变化
#         a,b = b,a+b
#     pass
# fib3()


'''
递归方式实现 生成前5项
'''
# def fib(n):
#     if n == 0 :
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-2) + fib(n-1)
# f = fib(5)
# print(f,end=' ')


# def fib(n):
#     if n < 3:
#         return n
#     return fib(n-2) + fib(n-1)
# print(fib(6))

# def num(n):
#     count = 0
#     while (n > 0):
#         if ((n & 1) == 1):
#             count += 1
#         n = n >> 1
#     return count
# f = num(5)
# print(f)


