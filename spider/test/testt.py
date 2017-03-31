import threading,time,random
'''
count =0

class Counter(threading.Thread):
    def __init__(self,lock,threadName):
        super(Counter,self).__init__(name=threadName)
        self.lock = lock
        self.name = threadName
    def run(self):
        global count
        self.lock.acquire()
        for i in range(100000):
            count = count+1
        self.lock.release()
        print(self.name)
lock = threading.Lock()

for i in range(50):
    th = Counter(lock,"thread-"+str(i))
    th.start()
    th.join()

print (count)
'''

class Seeker(threading.Thread):
    def __init__(self,lock,threadName):
        super(Seeker,self).__init__()
        self.cond = lock
        self.name = threadName
    def run(self):
        time.sleep(1)
        self.cond.acquire()
        print(self.name+":我已经把眼睛蒙上了！")
        self.cond.notify()
        self.cond.wait()
        print(self.name+":我找到你了！")
        self.cond.notify()
        self.cond.wait()
        print(self.name+":i win")
        self.cond.release()

class Hider(threading.Thread):
    def __init__(self,lock,threadName):
        super(Hider,self).__init__()
        self.cond = lock
        self.name = threadName
    def run(self):
        self.cond.acquire()
        print(self.name+":我要开始藏了！")
        self.cond.wait()
        print(self.name+"：我已经藏好啦！")
        self.cond.notify()
        self.cond.wait()
        print(self.name+":被你找到了")
        self.cond.notify()
        self.cond.release()
cond = threading.Condition()
seeker = Seeker(cond,'seeker')
hider = Hider(cond,'hider')

hider.start()
seeker.start()


