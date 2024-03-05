import time
from threading import *
class A(Thread):
    def run(self):
        for i in range(0, 5):
            print("ThreadA" + str(i + 1))
            time.sleep(1)


class B(Thread):
    def run(self):
        for i in range(0, 5):
            print("ThreadB" + str(i + 1))
            time.sleep(1)


obA = A()
obB = B()

obA.start()
time.sleep(0.5)
obB.start()

obA.join()
obB.join()
print("Main Thread")
