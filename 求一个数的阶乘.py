#递归函数
# def f(num):
#     if num <= 1:
#         return 1
#     return f(num-1)*num
#     pass
# if __name__ == '__main__':
#     print(f(5))


'''
n!=1×2×3×...×n         n!=1×2×3×...×(n-1)n
n的阶乘是求n与(n-1)阶乘的乘积

前提是: n>=1
'''
#非递归实现
#假如求10的阶乘   1*2*3*4*5*6*7*8*9*10
def func(num):
    res = 1
    for item in range(1,num+1):
        res *= item
    # print(item,end=' ') #10
    print(res,end=' ')
    pass
if __name__ == '__main__':
    func(10)
    pass


