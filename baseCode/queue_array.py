class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, number):
        if self.rear == self.size - 1:
            print("Queue full.")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = number

    def dequeue(self):
        if self.front == -1:
            print("Queue empty.")
            return None
        
        number = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front += 1
        return number

print_queue = Queue(5)

print_queue.enqueue("1")
print_queue.enqueue("2")
print_queue.enqueue("3")
print_queue.enqueue("4")
print_queue.enqueue("5")
print_queue.enqueue("6")

print('\nDequeuing:')
print(print_queue.dequeue())  
print(print_queue.dequeue())  
print(print_queue.dequeue())  
print(print_queue.dequeue())  
print(print_queue.dequeue())  
