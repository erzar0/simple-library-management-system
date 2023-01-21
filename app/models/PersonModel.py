from psycopg import connect

from .BaseModel import BaseModel
from datetime import date, timedelta
from psycopg.rows import dict_row


class PersonModel(BaseModel):

    def registerMember(self, personData):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                personData["join_date"] = date.today()
                personData["expiration_date"] = date.today() + timedelta(days=365)
                sql = """
                with insert_person as 
                    (insert into library.person 
                    (first_name, last_name, pesel, birth_date, email)
                    values
                    (%(first_name)s, %(last_name)s, %(pesel)s, %(birth_date)s, %(email)s)
                    returning id),

                insert_address as 
                    (insert into library.address
                    (id_person, city, postal_code, street, house_number, apartment_number)
                    select id, %(city)s, %(postal_code)s, %(street)s, %(house_number)s, %(apartment_number)s from insert_person
                    returning id_person)

                insert into library.member 
                (id_person, join_date, expiration_date)
                select id_person, %(join_date)s, %(expiration_date)s from insert_address
                returning id
                """
                return cur.execute(sql, personData).fetchone()

    def getAllMembers(self):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """select * from library.member_all_data"""
                return cur.execute(sql).fetchall()
    
    def getMemberById(self, id):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """select * from library.member_all_data where id = %(id)s"""
                return cur.execute(sql, {"id": id}).fetchone()

    def registerLibrarian(self, personData):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """
                with insert_person as 
                    (insert into library.person 
                    (first_name, last_name, pesel, birth_date, email)
                    values
                    (%(first_name)s, %(last_name)s, %(pesel)s, %(birth_date)s, %(email)s)
                    returning id),

                insert_address as 
                    (insert into library.address
                    (id_person, city, postal_code, street, house_number, apartment_number)
                    select id, %(city)s, %(postal_code)s, %(street)s, %(house_number)s, %(apartment_number)s from insert_person
                    returning id_person)

                insert into library.librarian
                (id_person, id_supervisor, salary, job_position)
                select id_person, %(id_supervisor)s, %(salary)s, %(job_position)s from insert_address
                returning id
                """
                return cur.execute(sql, personData).fetchone()

    def getAllLibrarians(self):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """select * from library.member_all_data"""
                return cur.execute(sql).fetchall()
    
    def getLibrarianById(self, id):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """select * from library.librarian_all_data where id = %(id)s"""
                return cur.execute(sql, {"id": id}).fetchone()




            
