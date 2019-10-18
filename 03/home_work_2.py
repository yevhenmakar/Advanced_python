class Queue:

    def __init__(self):
        self._items = []

    def get_queue(self):
        return self._items

    def push(self, item):
        self._items.insert(0, item)

    def pop(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def peek(self):
        return self._items[-1]

    def clear_stack(self):
        self._items = []


queue = Queue()

queue.push('aaa')
queue.push('bbb')
queue.push('ccc')
print(queue.get_queue())
print(queue.peek())

queue.pop()
print(queue.get_queue())
print(queue.peek())

queue.clear_stack()
print(queue.get_queue())