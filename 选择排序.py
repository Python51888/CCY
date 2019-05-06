#定义排序的方法
def xuanSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(len(arr)-1): #总的次数是len(arr)-1--最后一个数不用排
        minIndex = i #确定最小值索引
        for j in range(i+1,len(arr)): #每次都从剩下序列的第二个位置开始比较
            if arr[j] < arr[minIndex]:#假如有比最小值索引处的值小的数,就把这个数的索引作为最小值的索引
                minIndex = j
        if i != minIndex:
            #交换两个数的位置
            arr[i],arr[minIndex] = arr[minIndex],arr[i]
    return arr
    pass

if __name__ == '__main__':
    a = input('请输入待排序数列')
    s = a.split()  # 以空格分割
    arr = []
    for item in s:
        arr.append(int(item))

    # 开始调用方法
    list = xuanSort(arr)
    print('数据排序如下:')
    for item in list:
        print(item, end=' ')
    pass
