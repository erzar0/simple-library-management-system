from .BaseModel import BaseModel
from psycopg import connect
from psycopg.rows import dict_row
from datetime import date, timedelta



class FunctionalityModel(BaseModel):
    def loanBook(self, loanData):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """
                insert into library.loan  
                (id_book, id_member, id_librarian, loan_date, due_date)
                values
                (%(id_book)s, %(id_member)s, %(id_librarian)s, %(loan_date)s, %(due_date)s)
                returning id
                """
                return cur.execute(sql, loanData).fetchone()

    def getLoanById(self, id):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """select * from library.loan where id = %(id)s"""
                return cur.execute(sql, {"id": id}).fetchone()
    
    def isBookLent(self, id):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """select * from library.lent_books where id = %(id)s"""
                return True if cur.execute(sql, {"id": id}).fetchone() else False

    def getAllLoans(self):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """select * from library.loan"""
                return cur.execute(sql).fetchall()




    def imposePayment(self, paymentData):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                paymentData["issue_date"] = date.today()
                sql = """
                insert into library.payment
                (id_member, id_librarian, type, to_pay, issue_date)
                values
                (%(id_member)s, %(id_librarian)s, %(type)s, %(to_pay)s, %(issue_date)s)
                returning id
                """
                return cur.execute(sql, paymentData).fetchone()

    def getPaymentById(self, id):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """select * from library.payment where id = %(id)s"""
                return cur.execute(sql, {"id": id}).fetchone()
    
    def getAllPayments(self):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """select * from library.payment"""
                return cur.execute(sql).fetchall()
        

    