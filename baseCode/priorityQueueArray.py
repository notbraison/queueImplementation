import sys
#priority queue using an array

class item :#items' structure 
	value = 0
	priority = 0
class queue :# Store the element of a priority queue
	pr = [None] * (100000)# Pointer to the last index
	size = -1#size of the PQ
	
	
	@staticmethod
	def enqueue( value, priority) :# Function to insert a new elementinto priority queue
			
		queue.size += 1# Increase the size of PQ
		
		# Insert the element
		queue.pr[queue.size] = item()
		queue.pr[queue.size].value = value
		queue.pr[queue.size].priority = priority
		
	
	@staticmethod
	def peek() :# Function to check the top element
		highestPriority = -sys.maxsize
		ind = -1
		
		# Check for the element with highest priority
		i = 0
		while (i <= queue.size) :
		
			# If priority is same choose the element with the highest value
			if (highestPriority == queue.pr[i].priority and ind > -1 and queue.pr[ind].value < queue.pr[i].value) :
				highestPriority = queue.pr[i].priority
				ind = i
			elif(highestPriority < queue.pr[i].priority) :
				highestPriority = queue.pr[i].priority
				ind = i
			i += 1
			
		# Return position of the element
		return ind
	

	@staticmethod
	def dequeue() :	# Function to remove the element with the highest priority
	
		# Find the position of the element with highest priority
		ind = queue.peek()
		
		# Shift the element one index before from the position of the element with highest priority is found
		i = ind
		while (i < queue.size) :
			queue.pr[i] = queue.pr[i + 1]
			i += 1
			
		# Decrease the size of the priority queue by one
		queue.size -= 1
	@staticmethod
 
	def main( args) :
	
		# Function Call to insert elements as per the priority
		queue.enqueue(10, 2)
		queue.enqueue(14, 4)
		queue.enqueue(16, 4)
		queue.enqueue(12, 3)
		queue.enqueue(121, 7)
		
		# Stores the top element at the moment
		ind = queue.peek()
		print(queue.pr[ind].value)
		
		# Dequeue the top element
		queue.dequeue()
		
		# Check the top element
		ind = queue.peek()
		print(queue.pr[ind].value)
		
		# Dequeue the top element
		queue.dequeue()
		
		# Check the top element
		ind = queue.peek()
		print(queue.pr[ind].value)
        
	
if __name__=="__main__":
	queue.main([])

"""
item: Represents each element in the priority queue. It has attributes value and priority.
queue: Manages the priority queue operations using static methods like 
enqueue, dequeue, peek, and a main method to demonstrate how to use the priority queue functionalities.
The main method demonstrates the usage of the implemented priority queue 
by enqueuing elements with their respective priorities, then peeking at the highest priority element, 
dequeuing it, and peeking again to display the new highest priority element.

To execute this code, you can run it as a Python script.
Upon execution, it enqueues elements with priorities,
prints the top element, dequeues elements,
and prints the new top element after each dequeue operation.
"""