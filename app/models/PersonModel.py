from .BaseModel import BaseModel
from sqlalchemy import text 

class PersonModel(BaseModel):

    def __init__(self):
        super().__init__("person")

    
    def add(self, person):
        with self.engine.connect() as conn:
            try:
                conn.execute(text(
                """insert into library.person 
                    (first_name, last_name ,pesel, birth_date, email) 
                    values (:first_name, :last_name, :pesel, :birth_date, :email)"""), person)
                return True 
            except Exception as e:
                print(e)
                return False
        