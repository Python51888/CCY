'''
Python 主要通过两种方式来创建线程：
1.使用 threading 模块的 Thread 类的构造器创建线程。
2.继承 threading 模块的 Thread 类创建线程类。
'''

#1.调用 Thread 类的构造器创建线程
import threading
# #定义一个普通的action函数,该函数准备作为线程执行体
# def action(max):
#     for i in range(max):
#         #调用threading模块current_thread()函数获取当前线程
#         #线程对象的getName()方法获取当前线程的名字
#         print(threading.current_thread().getName() + '---' + str(i))
# #下面是主程序(也就是主线程的执行体)
# for i in range(100):
#     #调用threading模块current_thread()函数获取当前线程
#     print(threading.current_thread().getName() + '---'+ str(i))
#     if i == 20:
#         #创建并启动第一个线程
#         t1 = threading.Thread(target=action,args=(100,))
#         t1.start()
#         #创建并启动第二个线程
#         t2 = threading.Thread(target=action,args=(100,))
#         t2.start()
# print('主线程执行完成!!!') #主线程结束，子线程任然要执行完
'''
以上是多线程的并发执行，轮询进行的(同一时刻只能有一个线程再执行,其他的线程处于阻塞状态,下一次继续上一次的执行)     
在进行多线程编程时，不要忘记 Python 程序运行时默认的主线程，主程序部分（没有放在任何函数中的代码）就是主线程的线程执行体

此时程序中共包含三个线程，这三个线程的执行没有先后顺序，它们以并发方式执行：Thread-1 执行一段时间，然后可能 Thread-2 或 MainThread 获得 CPU 执行一段时间，
接下来又换其他线程执行，这就是典型的线程并发执行，CPU 以快速轮换的方式在多个线程之间切换，从而给用户一种错觉，即多个线程似乎同时在执行。

通过上面介绍不难看出多线程的意义，如果不使用多线程，主程序直接调用两次 action() 函数，那么程序必须等第一次调用的 action() 函数执行完成，才会执行第二次调用的 action() 函数；必须等第二次调用的 action() 函数执行完成，才会继续向下执行主程序。
而使用多线程之后，程序可以让两个 action() 函数、主程序以并发方式执行，给用户一种错觉，两个 action() 函数和主程序似乎同时在执行。

threading.current_thread()：它是 threading 模块的函数，该函数总是返回当前正在执行的线程对象。
getName()：它是 Thread 类的实例方法，该方法返回调用它的线程名字。
'''



'''
通过继承 Thread 类来创建并启动线程的步骤如下： 
1.定义 Thread 类的子类，并重写该类的 run() 方法。run() 方法的方法体就代表了线程需要完成的任务，因此把 run() 方法称为线程执行体。
2.创建 Thread 子类的实例，即创建线程对象。
3.调用线程对象的 start() 方法来启动线程。
'''
#2.继承 Thread 类创建线程类
#通过继承threading.Thread类来创建线程类
class SubThread(threading.Thread):
    def __int__(self):
        threading.Thread.__init__(self)
        self.i = 0 #实例默认属性值
    #重写run()方法作为线程执行体
    def run(self):
        while self.i < 100:
            # 调用threading模块current_thread()函数获取当前线程
            # 线程对象的getName()方法获取当前线程的名字
            print(threading.current_thread().getName() + '--' + str(self.i))
            self.i += 1
    pass
#下面是主程序(主线程的执行体)
for i in range(100):
    # 调用threading模块current_thread()函数获取当前线程
    print(threading.current_thread().getName() + "--" + str(i))
    if i == 20:
        #创建并启动第一个线程对象
        t1 = SubThread()
        t1.start()
        #创建并启动第二个线程对象
        t2 = SubThread()
        t2.start()
print('主线程执行完成!!!')
'''程序中的 SubThread 类继承了 threading.Thread 类，并实现了 run() 方法。run() 方法中的代码执行流就是该线程所需要完成的任务。'''

'''
通常来说，推荐使用第一种方式来创建线程，因为这种方式不仅编程简单，而且线程直接包装 target 函数，具有更清晰的逻辑结构。
'''

# 通过继承threading.Thread类来创建线程类
class FkThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.i = 0
    # 重写run()方法作为线程执行体
    def run(self):
        while self.i < 100:
            # 调用threading模块current_thread()函数获取当前线程
            # 线程对象的getName()方法获取当前线程的名字
            print(threading.current_thread().getName() +  " " + str(self.i))
            self.i += 1
# 下面是主程序（也就是主线程的执行体）
for i in range(100):
    # 调用threading模块current_thread()函数获取当前线程
    print(threading.current_thread().getName() +  " " + str(i))
    if i == 20:
        # 创建并启动第一个线程
        ft1 = FkThread()
        ft1.start()
        # 创建并启动第二个线程
        ft2 = FkThread()
        ft2.start()
print('主线程执行完成!')



