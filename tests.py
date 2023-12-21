class Queue:
    queue = []
    def dequeue(self)->int:
        first_item = self.queue[0]
        self.queue.remove(self.queue[0])
        return first_item
    
    def enqueue(self, val:int)->str:
        self.queue.append(val)
        return f"{val} was successfully enqueued.\n Available data in queue: {self.queue}"




queue = Queue()
print(queue.enqueue(1))
print(queue.enqueue(2))
print(queue.enqueue(3))
# assert queue.dequeue() == 1
print(queue.dequeue())
print(queue.dequeue())