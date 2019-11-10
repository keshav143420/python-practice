class User:

    def __init__(self, name):
        self.name = name
        print('User object created ')

    def say_hello(self):
        print(f'Hello {self.name}')
