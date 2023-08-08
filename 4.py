import types

def unpack_list(list_of_list):
    lst = []
    for i in list_of_list:
        if isinstance(i, list): lst += i
        else: lst.append(i)
    for i in lst:
        if isinstance(i, list): return flat_generator(lst)
    return lst

def flat_generator(list_of_list):
    lst = unpack_list(list_of_list)
    for i in lst:
        yield i

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
