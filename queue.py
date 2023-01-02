class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        return self._data.pop(0)

    def peek(self):
        return self._data[0]

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0
