from .BaseModel import BaseModel
from psycopg import connect
from psycopg.rows import dict_row



class BookModel(BaseModel):
    def addBook(self, bookData):
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

                insert into library.member 
                (id_person, join_date, expiration_date)
                select id_person, %(join_date)s, %(expiration_date)s from insert_address
                returning id
                """

    def getBookById(self, id):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """select * from library.book where id = %(id)s"""
                return cur.execute(sql, {"id": id}).fetchone()


    def addAuthor(self, authorData):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """
                insert into library.author
                (first_name, last_name, nationality)
                values
                (%(first_name)s, %(last_name)s, %(nationality)s) 
                returning id
                """
                return cur.execute(sql, authorData).fetchone()
    
    def getAuthorById(self, id):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """select * from library.author where id = %(id)s"""
                return cur.execute(sql, {"id": id}).fetchone()


    def getAllAuthors(self):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """select * from library.author"""
                return cur.execute(sql).fetchall()