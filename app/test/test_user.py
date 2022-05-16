import sys
sys.path.append(".")

import pytest
from user import User


@pytest.fixture(scope="function")
def example_user_data():
    return [
        'darren', 1
    ]

def test_number_of_user(example_user_data):
    name, number = example_user_data
    user = User(name)
    assert user.get_number_of_user() == number


@pytest.mark.parametrize('name, expected',
        [
            ('Darren', 'Darren'),
            ('Ena', 'Ena'),
            ('Eric', 'Eric'),
            ('George', 'George')
        ]
    )
def test_user_name(name, expected):
    user = User(name)
    assert user.name == expected

