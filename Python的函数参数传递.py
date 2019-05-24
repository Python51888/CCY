'''
Python 的参数值是如何传入函数的呢？这是由 Python 函数的参数传递机制来控制的。
Python 中函数的参数传递机制都是“值传递”。所谓值传递，就是将实际参数值的副本（复制品）传入函数，而参数本身不会受到任何影响
'''
# a = 1
# def fun(a): #参数a相当于局部变量，只在方法区内有效
#     a = 2
#     return a
#     pass
# print(fun(a)) #2
# print(a) #1

a = []
def fun(a):
    a.append(1)
    pass
fun(a)
print(a) #[1]

