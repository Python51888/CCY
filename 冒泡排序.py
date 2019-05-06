#定义排序的方法
def maoSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    #每次冒出一个数--共排的次数是总数-1
    for i in range(n-1): #循环的次数是(总数-1)次
        #内部比较交换的次数---是len(arr)-1-i
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
    pass
if __name__ == '__main__':
    a = input('请输入待排序数列')
    s = a.split() #以空格分割
    arr = []
    for item in s:
        arr.append(int(item))

    #开始调用方法
    list = maoSort(arr)
    print('数据排序如下:')
    for item in list:
        print(item,end = ' ')


