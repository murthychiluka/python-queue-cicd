class QueueCreation:

    def __init__(self):
        self.queue = []

    # Add element
    def enqueue(self, element):
        self.queue.append(element)
        return self.queue

    # Remove element
    def dequeue(self):
        if not self.queue:
            return "Queue is empty"

        return self.queue.pop(0)

    # Display queue
    def display(self):
        return self.queue


# Application execution
if __name__ == "__main__":

    q = QueueCreation()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Queue:", q.display())

    print("Removed:", q.dequeue())

    print("Updated Queue:", q.display())