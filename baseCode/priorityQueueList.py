#priority queue using a list
class PriorityQueue:
    def __init__(self):
        self.queue = []#the list

    def enqueue(self, value, priority):
        # Add an element to the priority queue based on its priority
        self.queue.append((value, priority))

    def dequeue(self):
        if not self.is_empty():
            # Find the element with the highest priority
            highest_priority = 0
            for i in range(len(self.queue)):
                if self.queue[i][1] > self.queue[highest_priority][1]:
                    highest_priority = i
            # Remove and return the element with the highest priority
            return self.queue.pop(highest_priority)[0]
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            # Return the element with the highest priority (without removing it)
            highest_priority = 0
            for i in range(len(self.queue)):
                if self.queue[i][1] > self.queue[highest_priority][1]:
                    highest_priority = i
            return self.queue[highest_priority][0]
        else:
            return "Queue is empty"

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

pq = PriorityQueue()

# Enqueue elements with their priorities
pq.enqueue('3 litres', 3)
pq.enqueue('1 litre', 1)
pq.enqueue('2 litres', 2)

print("Peek:", pq.peek())  # Peek at the highest priority element
print("Dequeue:", pq.dequeue())  # Dequeue the highest priority element
print("Peek:", pq.peek())  # Peek after dequeue operation
