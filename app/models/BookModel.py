from .BaseModel import BaseModel
from psycopg import connect
from psycopg.rows import dict_row



class BookModel(BaseModel):
    def addBook(self, bookData):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                insert_book = """
                    insert into library.book
                    (isbn, title, language, publication_date, physical_location, price)
                    values
                    (%(isbn)s, %(title)s, %(language)s, %(publication_date)s, %(physical_location)s, %(price)s)
                    returning id"""
                id_book = cur.execute(insert_book, bookData).fetchone()["id"]

                add_author = """
                    insert into library.book_author
                    (id_book, id_author)
                    values
                    (%(id_book)s, %(id_author)s)"""
                for id_author in bookData["authors"]: 
                    cur.execute(add_author, {"id_author": id_author, "id_book": id_book})

                add_genre = """
                    insert into library.book_genre
                    (id_book, id_genre)
                    values
                    (%(id_book)s, %(id_genre)s)"""
                for id_genre in bookData["genres"]:
                    cur.execute(add_genre, {"id_genre": id_genre, "id_book": id_book})

                return {"id": id_book}

    def getAllBooks(self):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """select * from library.book"""
                return cur.execute(sql).fetchall()

    def getBookById(self, id):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """select * from library.book where id = %(id)s"""
                return cur.execute(sql, {"id": id}).fetchone()


    def searchBook(self, formData):
        with connect(self.connStr, row_factory=dict_row) as conn:
            searchFilters = dict()  
            searchFilters["genre"] = "%" + formData["genre"] + "%"
            searchFilters["author_first_name"] = "%" + formData["author_first_name"] + "%"
            searchFilters["author_last_name"] = "%" + formData["author_last_name"] + "%"
            searchFilters["title"] = "%" + formData["title"] + "%"

            with conn.cursor() as cur:
                get_book_ids = """select distinct bk.id from library.genres_of_book gob 
                        inner join library.authors_of_book aob 
                        on gob.id_book = aob.id_book
                        inner join library.book bk 
                        on bk.id = aob.id_book
                        where gob.name ilike %(genre)s
                        and aob.first_name ilike %(author_first_name)s
                        and aob.last_name ilike %(author_last_name)s
                        and bk.title ilike %(title)s;"""

                book_ids = [[book["id"] for book in cur.execute(get_book_ids, searchFilters).fetchall()]]

                get_books = """select * from library.book 
                                where id = any(%s)"""
                return cur.execute(get_books, book_ids).fetchall()



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




    def addGenre(self, genreData):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """
                insert into library.genre
                (name)
                values
                (%(name)s)
                returning id
                """
                return cur.execute(sql, genreData).fetchone()
    
    def getGenreById(self, id):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """select * from library.genre where id = %(id)s"""
                return cur.execute(sql, {"id": id}).fetchone()


    def getAllGenres(self):
        with connect(self.connStr, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                sql = """select * from library.genre"""
                return cur.execute(sql).fetchall()