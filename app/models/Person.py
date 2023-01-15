from .BaseModel import BaseModel

class Person(BaseModel):

    def __init__(self):
        super().__init__("person")

    
    def add(self):
        print('bbbb')