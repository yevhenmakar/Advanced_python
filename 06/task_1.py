class MyList:

    def __init__(self, *args):
        self._list = list(args)

    def pop(self):
        del self[len(self._list) - 1]
        return self[len(self._list) - 1]

    def append(self, item):
        save_list = self._list
        self._list = [0] * (len(save_list) + 1)
        for i in range(len(save_list)):
            self._list[i] = save_list[i]
        self._list[-1] = item

    def insert(self, index, item):
        list_before_index = self._list[:index]
        list_after_index = self._list[index:]
        self._list = []
        for i in list_before_index:
            self.append(i)
        self.append(item)
        for i in list_after_index:
            self.append(i)

    def remove(self, item):
        for key, value in enumerate(self._list):
            if value == item:
                del self._list[key]
                break

    def clear(self):
        self._list = list()

    def __add__(self, other_list):
        result_list = []
        for i in self._list:
            result_list.append(i)
        for i in other_list:
            result_list.append(i)
        return MyList(result_list)

    def __str__(self):
        return str(self._list)






