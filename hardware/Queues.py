import Queue

class ReadyQueue(object):
    def __init__(self):
        self.queue = Queue.Queue()

    def insert(self, pid):
        self.queue.put(pid)

    def take(self):
        return self.queue.get()
