class MyDict:

    def __init__(self, **kwargs):
        self._dict = dict(kwargs)

    def get(self, value):
        result = None
        for key in self.keys():
            if key == value:
                result = self._dict[key]
                break
        return result

    def items(self):
        keys_list, values_list = self.keys(), self.values()
        keys_values_list = []
        for key, value in enumerate(keys_list):
            keys_values_list.append((keys_list[key], values_list[key]))
        return keys_values_list

    def keys(self):
        return list(self._dict)

    def values(self):
        values_list = []
        for k in self.keys():
            values_list.append(self._dict[k])
        return values_list

    def __add__(self, other):
        return MyDict(**self._dict, **other)

    def __str__(self):
        return str(self._dict)