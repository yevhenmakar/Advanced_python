class ContextManagerForFile:

    def __init__(self, filename, method):
        self._file = open(filename, method)

    def __enter__(self):
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()
