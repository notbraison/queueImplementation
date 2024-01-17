// Sample queue data (you would use this data in your Python backend)
let queue = [];

function addToQueue() {
    const name = document.getElementById("name").value;
    const priority = document.getElementById("priority").value;

    // Add item to the queue
    queue.push({ name, priority });

    // Update the queue table
    updateQueueTable();

    // Clear the form
    document.getElementById("name").value = "";
    document.getElementById("priority").value = "";
}

function popFromQueue() {
    // Pop the first item from the queue
    queue.shift();

    // Update the queue table
    updateQueueTable();
}

function updateQueueTable() {
    const queueBody = document.getElementById("queueBody");

    // Clear the existing table content
    queueBody.innerHTML = "";

    // Populate the table with the current queue data
    queue.forEach(item => {
        const row = document.createElement("tr");
        row.innerHTML = `<td>${item.name}</td><td>${item.priority}</td><td></td>`;
        queueBody.appendChild(row);
    });
}
