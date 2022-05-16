import sys
sys.path.append(".")

import pytest
from item import Item

@pytest.fixture(scope="function")
def example_item_index_data():
    return [ 10001, 10001 ]

def test_index_of_item(example_item_index_data):
    index, expected = example_item_index_data
    Item.set_start_index(index)
    assert Item.get_current_index() == expected


@pytest.fixture(scope="class")
def example_item_data():
    return {
        'title':'macbook air m1', 
        'price': 24600,
        'user' : 'Darren1', 
        'cate' : 'laptop', 
        'desc' :'apple laptop'
    }


class TestItemCase(object):
    
    def test_item_tiile(self, example_item_data):
        assert example_item_data['title'] == 'macbook air m1'
        
    def test_item_price(self, example_item_data):
        assert example_item_data['price'] == 24600

    def test_item_user(self, example_item_data):
        assert example_item_data['user'] == 'Darren1'

    def test_item_cate(self, example_item_data):
        assert example_item_data['cate'] == 'laptop'
        
    def test_item_desc(self, example_item_data):
        assert example_item_data['desc'] == 'apple laptop'
        

