class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def peek(self):
        if not self.is_empty():
            return self._data[-1]

    def is_empty(self):
        return self._data == []

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)


if __name__ == "__main__":
    s = Stack()
    s.push(2)
    s.push(1)
    s.push(0)
    assert s.is_empty() == False
    assert len(s) == 3
