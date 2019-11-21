class ContextManagerShelve:

    def __init__(self, name):
        self._name = name

    def __enter__(self):
        self.file = open(self._name)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
