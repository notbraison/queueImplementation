class PetrolStationQueue:
    def __init__(self, num_pumps, max_queue_size=10):
        self.num_pumps = num_pumps
        self.max_queue_size = max_queue_size
        self.pumps = {i + 1: {'queue': [], 'front': -1, 'rear': -1} for i in range(num_pumps)}

    def is_full(self, pump):
        return (self.pumps[pump]['rear'] + 1) % self.max_queue_size == self.pumps[pump]['front']

    def is_empty(self, pump):
        return self.pumps[pump]['front'] == -1

    def get_shortest_queue_pump(self):
        shortest_pump = min(self.pumps, key=lambda pump: len(self.pumps[pump]['queue']))
        return shortest_pump

    def enqueue(self, number_plate):
        pump = self.get_shortest_queue_pump()
        if self.is_full(pump):
            print(f"Queue at Pump {pump} is full. Cannot enqueue {number_plate}.")
        else:
            if self.is_empty(pump):
                self.pumps[pump]['front'] = 0
            self.pumps[pump]['rear'] = (self.pumps[pump]['rear'] + 1) % self.max_queue_size
            self.pumps[pump]['queue'].append(number_plate)
            print(f" {number_plate} joined the queue at pump {pump}.")

    def dequeue(self, pump):
        if self.is_empty(pump):
            print(f"Queue at Pump {pump} is empty.")
            return None
        else:
            car = self.pumps[pump]['queue'][self.pumps[pump]['front']]
            if self.pumps[pump]['front'] == self.pumps[pump]['rear']:
                self.pumps[pump]['front'] = -1
                self.pumps[pump]['rear'] = -1
            else:
                self.pumps[pump]['front'] = (self.pumps[pump]['front'] + 1) % self.max_queue_size
            print(f"Pump {pump} is done fueling {car}.")
            return car

    def peek(self, pump):
        if self.is_empty(pump):
            print(f"Queue at Pump {pump} is empty.")
            return None
        else:
            car = self.pumps[pump]['queue'][self.pumps[pump]['front']]
            print(f"The first car at pump {pump} is {car}.")
            return car

    def display_queues(self):
        for pump in self.pumps:
            self.display_queue(pump)

    def display_queue(self, pump):
        if self.is_empty(pump):
            print(f"Queue at Pump {pump} is empty.")
        else:
            queue = self.pumps[pump]['queue']
            front, rear = self.pumps[pump]['front'], self.pumps[pump]['rear']
            if front <= rear:
                print(f"Current Queue at Pump {pump}:", queue[front: rear + 1])
            else:
                print(f"Current Queue at Pump {pump}:", queue[front:] + queue[:rear + 1])


num_pumps = 3
petrol_station_queue = PetrolStationQueue(num_pumps)

while True:
    print("\nOptions:")
    print("1. Enter car to be fueled")
    print("2. See the queues")
    print("3. Show the first car in each pump")
    print("4. Dequeue the first car in each pump")
    print("5. Exit")

    choice = input("\nChoose an option: ")

    if choice == '1':
        number_plate = input("Enter the number plate: ")
        petrol_station_queue.enqueue(number_plate)
    elif choice == '2':
        petrol_station_queue.display_queues()
    elif choice == '3':
        for pump_id in range(1, num_pumps + 1):
            petrol_station_queue.peek(pump_id)
    elif choice == '4':
        pump_to_dequeue = int(input("Enter the pump number to dequeue from: "))
        petrol_station_queue.dequeue(pump_to_dequeue)
    elif choice == '5':
        break
    else:
        print("Invalid option.")
