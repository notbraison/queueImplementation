class PetrolStationQueue:
    def __init__(self, num_pumps):
        self.pumps = {i + 1: [] for i in range(num_pumps)}

    def enqueue(self, number_plate):
        shortest_queue = min(self.pumps, key=lambda pump: len(self.pumps[pump]))
        self.pumps[shortest_queue].append(number_plate)
        print(f"{number_plate} joined the queue at pump {shortest_queue}.")

    def dequeue(self, pump):
        if not self.pumps[pump]:
            print(f"Queue at Pump {pump} is empty.")
            return None

        car = self.pumps[pump].pop(0)
        print(f"Pump {pump} is done fueling {car}.")
        return car

    def peek(self, pump):
        if not self.pumps[pump]:
            print(f"Queue at Pump {pump} is empty.")
            return None

        car = self.pumps[pump][0]
        print(f"The first car at pump {pump} is {car}.")
        return car

    def is_empty(self, pump):
        if pump not in self.pumps:
            print(f"Pump {pump} does not exist.")
            return None

        return len(self.pumps[pump]) == 0

    def display_queues(self):
        for pump in self.pumps:
            self.display_queue(pump)

    def display_queue(self, pump):
        if pump not in self.pumps:
            print(f"Pump {pump} does not exist.")
            return

        if self.is_empty(pump):
            print(f"Queue at Pump {pump} is empty.")
        else:
            print(f"Current Queue at Pump {pump}:", self.pumps[pump])


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
        for pump_id in range(1, num_pumps + 1):
            petrol_station_queue.dequeue(pump_id)
    elif choice == '5':
        break
    else:
        print("Invalid option.")
