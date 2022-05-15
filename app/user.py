class User:
    number_of_user = 0

    def __init__(self, name):
        self.name = name
        User.add_user()
    
    @classmethod
    def get_number_of_user(cls):
        return cls.number_of_user

    @classmethod
    def add_user(cls):
        cls.number_of_user += 1

    def show(self):
        print(f"I am {self.name}.")
    

if __name__ == '__main__':
    u1 = User('Darren')
    u2 = User('Ena')
    u2.show()
    
    print(User.get_number_of_user())