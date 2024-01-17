car_queue = []

def enqueue_car(car):
    car_queue.append(car)
    print(f"The car queued is a {car}")

def dequeue_car():
    if len(car_queue) == 0:
        print('The queue is empty!')
    else:
        car_fueled = car_queue.pop(0)
        print(f'The car that has been fueled is: {car_fueled}')

def display():
    print(*car_queue, sep = ", ")
    
def front_car():
    front_car = car_queue[0]
    print(f'The car at the front of the line is: {front_car}')
    
    
option = None

print("1: Enter car to be fueled: ", end = '')
print("\n", end = '')
print("2: Remove car that has been fueled", end = '')
print("\n", end = '')
print("3: The cars in line are ", end = '')
print("\n", end = '')
print("4: Display car at the front of the line", end = '')
print("\n", end = '')
print("5: Exit", end = '')
print("\n", end = '')
condition = True
while condition:
     
    option = int(input("\nInput the number of activity:"))
   
    if option == 1:
        car = input("Enter the type of to be fueled: ")
        enqueue_car(car)  
    elif option == 2:
        dequeue_car()
    elif option == 3:
        print('\nThe cars in line to be fueled are: ')
        display()
    elif option == 4:
        front_car()
    elif option == 5:
        print("Exit", end = '')
        print("\n", end = '')
    else:
        print("Invalid choice", end = '')
        print("\n", end = '')
    condition = option!=5

