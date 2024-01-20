from flask import Flask, render_template, request

app = Flask(__name__)

class PetrolStationQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, name, priority):
        self.queue.append((name, priority))
        self.queue.sort(key=lambda x: x[1], reverse=True)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

petrol_station_queue = PetrolStationQueue()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        priority = int(request.form['priority'])
        petrol_station_queue.enqueue(name, priority)

    return render_template('index.html', queue_content=petrol_station_queue.queue)

@app.route('/pop', methods=['GET'])
def pop_from_queue():
    served_customer = petrol_station_queue.dequeue()
    return render_template('index.html', queue_content=petrol_station_queue.queue, served_customer=served_customer)

if __name__ == '__main__':
    app.run(debug=True)
