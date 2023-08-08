class FlatIterator:

    def __init__(self, list_of_list):
        lst = []
        for i in list_of_list:
            if isinstance(i, list): lst += i
            else: lst.append(i)
        for i in lst:
            if isinstance(i, list):
                return self.__init__(lst)
        self.list = lst

    def __iter__(self):
        self.index = -1
        return self
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.list): raise StopIteration
        return self.list[self.index]


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()