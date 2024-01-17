
car_array = [0 for _ in range(10)]
number_of_cars = 10
front_car = - 1
rear_car = - 1

def enqueue_car(car):
    global number_of_cars
    global rear_car
    global front_car
    if rear_car == number_of_cars - 1:
        print("The queue is full!", end = '')
        print("\n", end = '')
        return
    else:
        if front_car == - 1 and rear_car == -1:
            front_car = 0
            rear_car = 0
        else:
            rear_car += 1
        
        car_array[rear_car] = car
        print(f"The car queued is a {car}")

def dequeue_car():
    global number_of_cars
    global rear_car
    global front_car
    
    if front_car == - 1 or front_car > rear_car:
        print("The queue is empty! ", end = '')
        return
    else:
        car = car_array[front_car]
       
        print(f"The car fueled is a {car} ", end = '')
        print("\n", end = '')
        
        if rear_car == front_car:
            rear_car = -1
            front_car = -11
            
        else:
            front_car = front_car 
        
        front_car += 1

def display():
    global number_of_cars
    global rear_car
    global front_car
    
    if front_car == - 1:
       
        print("The queue is empty!", end = '')
        print("\n", end = '')
        return
    else:
        
        print("The cars in line are : ", end = '')
        i = front_car
        while i <= rear_car:
            print(car_array[i], end = '')
            print(", ", end = '')
            i += 1
        print("\n", end = '')

def display_front_car():
    global number_of_cars
    global rear_car
    global front_car
    
    if front_car == - 1:
       
        print("The queue is empty!", end = '')
        print("\n", end = '')
        return
    else:
       
        print(f"The car at the front is a {car_array[front_car]} ", end = '')
        print("\n", end = '')

option = None

print("1: Enter car to be fueled ", end = '')
print("\n", end = '')
print("2: Remove car that has been fueled ", end = '')
print("\n", end = '')
print("3: Display all cars in the line", end = ' ')
print("\n", end = '')
print("4: Display car at the front of the line", end = '')
print("\n", end = '')
print("5: Exit", end = '')
print("\n", end = '')

condition = True
while condition:
     
    option = int(input("\nInput the number of activity: "))
    
    if option == 1:
        car = input("Enter the type of car: ")
        enqueue_car(car)
    elif option == 2:
        dequeue_car()
    elif option == 3:
        display()
    elif option == 4:
        display_front_car()
    elif option == 5:
        print("Exit", end = '')
        print("\n", end = '')
    else:
        print("Invalid choice", end = '')
        print("\n", end = '')
    condition = option!=5

