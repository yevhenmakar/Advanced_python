class Stack:

    def __init__(self):
        self._items = []

    def get_stack(self):
        return self._items

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._items.pop()

    def size(self):
        return len(self._items)

    def is_empty(self):
        return True if not self.size() else False

    def peek(self):
        return self._items[len(self._items) - 1]

    def clear_stack(self):
        self._items = []


stack = Stack()

stack.push('aaa')
stack.push('bbb')
stack.push('ccc')
print(stack.get_stack())
print(stack.peek())

stack.pop()
print(stack.get_stack())

stack.clear_stack()
print(stack.get_stack())
