import unittest
from my_queue import QueueCreation


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.q = QueueCreation()

    def test_enqueue(self):
        self.q.enqueue(10)
        self.q.enqueue(20)

        self.assertEqual(self.q.display(), [10, 20])

    def test_dequeue(self):
        self.q.enqueue(10)
        self.q.enqueue(20)

        result = self.q.dequeue()

        self.assertEqual(result, 10)
        self.assertEqual(self.q.display(), [20])

    def test_empty_queue(self):

        result = self.q.dequeue()

        self.assertEqual(result, "Queue is empty")


if __name__ == "__main__":
    unittest.main()