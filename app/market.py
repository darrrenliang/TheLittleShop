from user import User
from item import Item

class Market:
    def __init__(self, name:str):
        self.name = name
        self.user_table = {}
        self.item_table = {}

    def register(self, username:str):
        pass

    def createList(
        self, 
        title:str,
        price:int,
        cate:str,
        username:str,
        desc:str = None
    ):  
        pass
    
    def deleteList(self, username:str, listid:int):
        pass   


if __name__ == "__main__":
    pass