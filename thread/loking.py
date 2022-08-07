import threading
import time

exitFlag = 0
threadLock = threading.Lock()
threads = []


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        threadLock.acquire()
        print_time(threadName=self.name, delay=self.counter, counter=3)
        print("Exiting " + self.name)


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime((time.time()))))
        counter -= 1
        if exitFlag:
            threadName.exit()


thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(1, "Thread-2", 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

thread1.join()
thread2.join()

for t in threads:
    t.join()
print("Exiting Main Thread")
