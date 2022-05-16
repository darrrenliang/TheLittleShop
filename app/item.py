from datetime import datetime

class Item:
    index_of_item = 0

    def __init__(
        self, 
        title:str, 
        price:int, 
        cate:str, 
        user:str, 
        desc:str = None
    ):

        self.index = self.get_current_index()
        self.title = title
        self.price = price
        self.time  = datetime.now()
        self.user  = user
        self.cate  = cate
        self.desc  = desc
        
        self.add_new_item()

    def __repr__(self):

        msgFormat = "%s|%s|%s|%s|%s|%s" % ( 
            self.title,
            self.desc,
            self.price,
            self.time.strftime('%Y-%m-%d %H:%M:%S'),
            self.cate,
            self.user
        )
        
        return msgFormat

    @classmethod
    def add_new_item(cls):
        cls.index_of_item += 1
    
    @classmethod
    def get_current_index(cls):
        return cls.index_of_item

    @classmethod
    def set_start_index(cls, number: int):
        if not isinstance(number, int):
            return
        
        cls.index_of_item = number


if __name__ == '__main__':
    Item.set_start_index(10001)

    i1 = Item('macbook air m1', 24600,'Darren1', 'laptop', 'apple laptop')
    i2 = Item('macbook pro m1', 34500,'Darren1', 'laptop', 'apple laptop')
    
    print(i2)
    print(Item.index_of_item)