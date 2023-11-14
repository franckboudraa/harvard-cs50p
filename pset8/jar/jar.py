class Jar:
    def __init__(self, capacity=12):
        self._size = 0
        self.capacity = capacity

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("You cannot have more cookies than permitted capacity")
        elif n < 0:
            raise ValueError("You cannot deposit a negative number of cookies")

        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("You cannot withdraw a negative number of cookies")
        elif self._size - n < 0:
            raise ValueError("You cannot withdraw more cookies that you have in jar")

        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("You must provide a positive capacity")

        self._capacity = capacity

    @property
    def size(self):
        return self._size

