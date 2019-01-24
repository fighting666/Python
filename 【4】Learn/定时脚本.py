#-*- coding:utf-8 -*-
import threading
import time

# 真正要执行的函数


def t1():
    print('ok')

# 每隔10秒钟执行


def t2():
    while 1:
        t1()
        time.sleep(2)

if __name__ == '__main__':
    t = threading.Thread(target=t2)
    t.start()

    # 此处写你主线程要处理的事情.....

    t.join()
