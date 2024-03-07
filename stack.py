class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self.is_empty():
            return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0

    def get_items(self):
        return self._items
