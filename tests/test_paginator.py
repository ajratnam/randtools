import pytest

from randtools import Paginator


class data:
    normal_data = {
        'data': {
            'objects': ['1', '2', '3', '4', '5', '6', '7'],
            'starting_index': 0,
            'on_end_error': False,
            'convert_to_list': False
        },
        'expected': {
            'starting_index': 0,
            'next_index': 1,
            'starting_value': '1',
            'next_value': '2',
            'prev_index': 0,
            'prev_value': '1',
            'extreme_next_index': 6,
            'extreme_next_value': '7',
            'extreme_prev_index': 0,
            'extreme_prev_value': '1'
        }
    }

    convert_to_list_data = {
        'data': {
            'objects': range(10),
            'starting_index': 0,
            'on_end_error': False,
            'convert_to_list': True
        },
        'expected': {
            'starting_index': 0,
            'next_index': 1,
            'starting_value': 0,
            'next_value': 1,
            'prev_index': 0,
            'prev_value': 0,
            'extreme_next_index': 9,
            'extreme_next_value': 9,
            'extreme_prev_index': 0,
            'extreme_prev_value': 0
        }
    }

    custom_starting_index_data = {
        'data': {
            'objects': range(10),
            'starting_index': 2,
            'on_end_error': False,
            'convert_to_list': True
        },
        'expected': {
            'starting_index': 2,
            'next_index': 3,
            'starting_value': 2,
            'next_value': 3,
            'prev_index': 1,
            'prev_value': 1,
            'extreme_next_index': 9,
            'extreme_next_value': 9,
            'extreme_prev_index': 0,
            'extreme_prev_value': 0
        }
    }

    on_end_error_is_true_data = {
        'data': {
            'objects': range(10),
            'starting_index': 0,
            'on_end_error': True,
            'convert_to_list': True
        },
        'expected': {
            'starting_index': 0,
            'next_index': 1,
            'starting_value': 0,
            'next_value': 1,
            'prev_index': IndexError,
            'prev_value': IndexError,
            'extreme_next_index': IndexError,
            'extreme_next_value': IndexError,
            'extreme_prev_index': IndexError,
            'extreme_prev_value': IndexError
        }
    }

    on_end_error_is_none_data = {
        'data': {
            'objects': range(10),
            'starting_index': 0,
            'on_end_error': None,
            'convert_to_list': True
        },
        'expected': {
            'starting_index': 0,
            'next_index': 1,
            'starting_value': 0,
            'next_value': 1,
            'prev_index': 9,
            'prev_value': 9,
            'extreme_next_index': 0,
            'extreme_next_value': 0,
            'extreme_prev_index': 0,
            'extreme_prev_value': 0
        }
    }

    starting_index_is_more_than_limit_data = {
        'data': {
            'objects': range(10),
            'starting_index': 11,
            'on_end_error': False,
            'convert_to_list': True
        },
        'expected': {
            'starting_index': 9,
            'next_index': 9,
            'starting_value': 9,
            'next_value': 9,
            'prev_index': 8,
            'prev_value': 8,
            'extreme_next_index': 9,
            'extreme_next_value': 9,
            'extreme_prev_index': 0,
            'extreme_prev_value': 0
        }
    }

    starting_index_is_more_than_limit_and_on_error_is_true_data = {
        'data': {
            'objects': range(10),
            'starting_index': 11,
            'on_end_error': True,
            'convert_to_list': True
        },
        'expected': {
            'starting_index': IndexError,
            'starting_value': IndexError
        }
    }

    starting_index_is_more_than_limit_and_on_error_is_none_data = {
        'data': {
            'objects': range(10),
            'starting_index': 11,
            'on_end_error': None,
            'convert_to_list': True
        },
        'expected': {
            'starting_index': 1,
            'next_index': 2,
            'starting_value': 1,
            'next_value': 2,
            'prev_index': 0,
            'prev_value': 0,
            'extreme_next_index': 1,
            'extreme_next_value': 1,
            'extreme_prev_index': 1,
            'extreme_prev_value': 1
        }
    }

    starting_index_is_less_than_limit_data = {
        'data': {
            'objects': range(10),
            'starting_index': -1,
            'on_end_error': False,
            'convert_to_list': True
        },
        'expected': {
            'starting_index': 0,
            'next_index': 1,
            'starting_value': 0,
            'next_value': 1,
            'prev_index': 0,
            'prev_value': 0,
            'extreme_next_index': 9,
            'extreme_next_value': 9,
            'extreme_prev_index': 0,
            'extreme_prev_value': 0
        }
    }

    starting_index_is_less_than_limit_and_on_error_is_true_data = {
        'data': {
            'objects': range(10),
            'starting_index': -1,
            'on_end_error': True,
            'convert_to_list': True
        },
        'expected': {
            'starting_index': IndexError,
            'starting_value': IndexError
        }
    }

    starting_index_is_less_than_limit_and_on_error_is_none_data = {
        'data': {
            'objects': range(10),
            'starting_index': -1,
            'on_end_error': None,
            'convert_to_list': True
        },
        'expected': {
            'starting_index': 9,
            'next_index': 0,
            'starting_value': 9,
            'next_value': 0,
            'prev_index': 8,
            'prev_value': 8,
            'extreme_next_index': 9,
            'extreme_next_value': 9,
            'extreme_prev_index': 9,
            'extreme_prev_value': 9
        }
    }

    is_at_end = {
        'data': {
            'objects': range(10),
            'starting_index': 9,
            'on_end_error': False,
            'convert_to_list': True
        },
        'expected': {
            'starting_index': 9,
            'next_index': 9,
            'starting_value': 9,
            'next_value': 9,
            'prev_index': 8,
            'prev_value': 8,
            'extreme_next_index': 9,
            'extreme_next_value': 9,
            'extreme_prev_index': 0,
            'extreme_prev_value': 0
        }
    }

    is_at_end_and_on_error_is_true = {
        'data': {
            'objects': range(10),
            'starting_index': 9,
            'on_end_error': True,
            'convert_to_list': True
        },
        'expected': {
            'starting_index': 9,
            'next_index': IndexError,
            'starting_value': 9,
            'next_value': IndexError,
            'prev_index': 8,
            'prev_value': 8,
            'extreme_next_index': IndexError,
            'extreme_next_value': IndexError,
            'extreme_prev_index': IndexError,
            'extreme_prev_value': IndexError
        }
    }

    is_at_end_and_on_error_is_none = {
        'data': {
            'objects': range(10),
            'starting_index': 9,
            'on_end_error': None,
            'convert_to_list': True
        },
        'expected': {
            'starting_index': 9,
            'next_index': 0,
            'starting_value': 9,
            'next_value': 0,
            'prev_index': 8,
            'prev_value': 8,
            'extreme_next_index': 9,
            'extreme_next_value': 9,
            'extreme_prev_index': 9,
            'extreme_prev_value': 9
        }
    }


all_data = {
    'normal': [value for value in vars(data).values() if
               isinstance(value, dict) and value.get('data', {}).get('on_end_error') is False],
    'on_end_error_is_true': [value for value in vars(data).values() if
                             isinstance(value, dict) and value.get('data', {}).get('on_end_error') is True],
    'on_end_error_is_none': [value for value in vars(data).values() if
                             isinstance(value, dict) and value.get('data', {}).get('on_end_error', False) is None],
    'starts_proper': [value for value in vars(data).values() if
                      isinstance(value, dict) and isinstance(value.get('expected', {}).get('starting_index', None),
                                                             int)]
}

check = lambda test_data: pytest.mark.parametrize("sequence", test_data)

all_test_data = check(sum(all_data.values(), []))
normal_test_data = check(all_data['normal'])
end_true_data = check(all_data['on_end_error_is_true'])
end_none_data = check(all_data['on_end_error_is_none'])
starts_proper = check(all_data['starts_proper'])


def get_data_and_expected(sequence, *keys) -> tuple:
    return sequence['data'], *[sequence['expected'][attr] for attr in keys]


@all_test_data
def test_initial_index_and_value(sequence):
    test_data, expected_index, expected_value = get_data_and_expected(sequence, 'starting_index', 'starting_value')
    try:
        pages = Paginator(**test_data)
        assert pages.index == expected_index
        assert pages.value == expected_value
    except Exception as err:
        assert isinstance(err, expected_index)


@starts_proper
def test_next_index_and_value(sequence):
    test_data, expected_index, expected_value = get_data_and_expected(sequence, 'next_index', 'next_value')
    pages = Paginator(**test_data)
    try:
        pages.next()
        assert pages.index == expected_index
        assert pages.value == expected_value
    except Exception as err:
        assert isinstance(err, expected_index)


@starts_proper
def test_prev_index_and_value(sequence):
    test_data, expected_index, expected_value = get_data_and_expected(sequence, 'prev_index', 'prev_value')
    pages = Paginator(**test_data)
    try:
        pages.prev()
        assert pages.index == expected_index
        assert pages.value == expected_value
    except Exception as err:
        assert isinstance(err, expected_index)


@starts_proper
def test_extreme_next_index_value(sequence):
    test_data, expected_index, expected_value = get_data_and_expected(sequence, 'extreme_next_index', 'extreme_next_value')
    pages = Paginator(**test_data)
    try:
        pages.next(10)
        assert pages.index == expected_index
        assert pages.value == expected_value
    except Exception as err:
        assert isinstance(err, expected_index)


@starts_proper
def test_extreme_prev_index_value(sequence):
    test_data, expected_index, expected_value = get_data_and_expected(sequence, 'extreme_prev_index', 'extreme_prev_value')
    pages = Paginator(**test_data)
    try:
        pages.prev(10)
        assert pages.index == expected_index
        assert pages.value == expected_value
    except Exception as err:
        assert isinstance(err, expected_index)
