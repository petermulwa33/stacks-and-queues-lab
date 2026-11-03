
import random


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        Add a new customer to the back of the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the customer at the front.
        Return None if the queue is empty.
        """
        if self.is_empty():
            return None

        return self.items.pop(0)

    def peek(self):
        """
        Return the first customer without removing them.
        """
        if self.is_empty():
            return None

        return self.items[0]

    def is_empty(self):
        """
        Check whether the queue contains any customers.
        """
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly select a customer and dequeue everyone
        up to and including the selected winner.

        Returns the winning customer's name.
        Returns None if the queue is empty.
        """

        if self.is_empty():
            return None

        # Randomly select an index in the queue.
        winner_index = random.randrange(len(self.items))

        # Identify the customer at that position.
        winner = self.items[winner_index]

        # Remove everyone from the front through the winner.
        for _ in range(winner_index + 1):
            self.dequeue()

        return winner
