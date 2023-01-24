from flask import Flask, request, flash, render_template, redirect, url_for
from datetime import date, timedelta
import json

from src.forms.RegisterMemberForm import RegisterMemberForm
from src.forms.RegisterLibrarianForm import RegisterLibrarianForm
from src.forms.AddBookForm import AddBookForm
from src.forms.AddAuthorForm import AddAuthorForm
from src.forms.AddBookGenreForm import AddBookGenreForm
from src.forms.SearchBookForm import SearchBookForm 
from src.forms.LoanBookForm import LoanBookForm 
from src.forms.ImposePaymentForm import ImposePaymentForm
from src.forms.ReturnBookForm import ReturnBookForm


from src.models.PersonModel import PersonModel
from src.models.BookModel import BookModel 
from src.models.FunctionalityModel import FunctionalityModel



app = Flask(__name__, template_folder="src/templates")
app.secret_key = "parmegiano"
app.static_folder = "src/static"

Person = PersonModel()
Book = BookModel()
Functionality = FunctionalityModel() 

@app.route("/")
def index():
    return render_template("base.html")

#Member
@app.route("/member/register", methods=["GET", "POST"])
def registerMember():
    form = RegisterMemberForm() 
    if request.method == "POST": 
        if form.validate():
                try:
                    res = Person.registerMember(form.data)
                    return redirect(url_for("showMember", id=res["id"]))

                except BaseException as e:
                    flash("Wystąpił błąd bazy danych!")
                    print(e)
        else:
            flash("Wprowadzono nieprawidłowe dane!")
    return render_template("RegisterMember.html", form = form)

@app.route("/member/<id>", methods=["GET"])
def showMember(id):
    id = request.view_args["id"]
    record = Person.getMemberById(id)
    return render_template("ShowDbEntry.html", record = record)

@app.route("/member/all", methods=["GET"])
def showAllMembers():
    records = Person.getAllMembers()
    return render_template("ShowDbEntries.html", records=records)




@app.route("/librarian/register", methods=["GET", "POST"])
def registerLibrarian():
    form = RegisterLibrarianForm() 
    if request.method == "POST": 
        if form.validate():
                try:
                    res = Person.registerLibrarian(form.data)
                    return redirect(url_for("showLibrarian", id=res["id"]))
                except BaseException as e:
                    flash("Wystąpił błąd bazy danych!")
                    print(e)
        else:
            flash("Wprowadzono nieprawidłowe dane!")

    return render_template("RegisterLibrarian.html", form = form)

@app.route("/librarian/<id>", methods=["GET"])
def showLibrarian(id):
    id = request.view_args["id"]
    record = Person.getLibrarianById(id)
    return render_template("ShowDbEntry.html", record = record )

@app.route("/librarian/all", methods=["GET"])
def showAllLibrarians():
    records = Person.getAllLibrarians()
    return render_template("ShowDbEntries.html", records=records)




@app.route("/book", methods=["GET", "POST"])
def addBook():
    authors = [(author["id"], author["first_name"] 
                            + " " + author["last_name"] 
                            + " - " + author["nationality"]) for author in Book.getAllAuthors()]
    genres = [(genre["id"], genre["name"] ) for genre in Book.getAllGenres()]
    form = AddBookForm() 
    form.authors.choices = authors
    form.genres.choices = genres
    if request.method == "POST": 
        print(form.data)
        if form.validate():
                try:
                    res = Book.addBook(form.data)
                    return redirect(url_for("showBook", id=res["id"]))
                except BaseException as e:
                    flash("Wystąpił błąd bazy danych!")
                    print("blad:", e.with_traceback())
        else:
            flash("Wprowadzono nieprawidłowe dane!")

    return render_template("AddBook.html", form = form)

@app.route("/book/<id>", methods=["GET"])
def showBook(id):
    id = request.view_args["id"]
    record = Book.getBookById(id)
    return render_template("ShowDbEntry.html", record = record )

@app.route("/book/all", methods=["GET"])
def showAllBooks():
    records = Book.getAllBooks()
    return render_template("ShowDbEntries.html", records=records)

@app.route("/book/search", methods=["GET", "POST"])
def searchBook():
    form = SearchBookForm() 
    if request.method == "POST": 
        if form.validate():
                try:
                    books = Book.searchBook(form.data)
                    return render_template("SearchBook.html", form = form, books=books)
                except BaseException as e:
                    flash("Wystąpił błąd bazy danych!")
                    print(e)
        else:
            flash("Wprowadzono nieprawidłowe dane!")

    return render_template("SearchBook.html", form = form)




@app.route("/book/author", methods=["GET", "POST"])
def addAuthor():
    form = AddAuthorForm() 
    if request.method == "POST": 
        if form.validate():
                try:
                    res = Book.addAuthor(form.data)
                    return redirect(url_for("showAuthor", id=res["id"]))
                except BaseException as e:
                    flash("Wystąpił błąd bazy danych!")
                    print(e)
        else:
            flash("Wprowadzono nieprawidłowe dane!")

    return render_template("AddAuthor.html", form = form)

@app.route("/book/author/<id>", methods=["GET"])
def showAuthor(id):
    id = request.view_args["id"]
    record = Book.getAuthorById(id)
    return render_template("ShowDbEntry.html", record = record )

@app.route("/book/author/all", methods=["GET"])
def showAllAuthors():
    records = Book.getAllAuthors()
    return render_template("ShowDbEntries.html", records=records)





@app.route("/book/genre", methods=["GET", "POST"])
def addBookGenre():
    form = AddBookGenreForm() 
    if request.method == "POST": 
        if form.validate():
                try:
                    res = Book.addGenre(form.data)
                    return redirect(url_for("showBookGenre", id=res["id"]))
                except BaseException as e:
                    flash("Wystąpił błąd bazy danych!")
                    print(e)
        else:
            flash("Wprowadzono nieprawidłowe dane!")
    return render_template("AddBookGenre.html", form = form)

@app.route("/book/genre/<id>", methods=["GET"])
def showBookGenre(id):
    id = request.view_args["id"]
    record = Book.getGenreById(id)
    return render_template("ShowDbEntry.html", record = record )

@app.route("/book/genre/all", methods=["GET"])
def showAllGenres():
    records = Book.getAllGenres()
    return render_template("ShowDbEntries.html", records=records)


@app.route("/loan/", methods=["GET", "POST"])
def loanBook():
    form = LoanBookForm()
    if request.method == "POST": 
        if form.validate():
            print(form.data)
            if not Functionality.isBookLent(form.data["id_book"]):
                try:
                    loanData = {k: v for k,v in form.data.items()}
                    loanData["loan_date"] = date.today()
                    loanData["due_date"] = date.today() + timedelta(days=30)
                    res = Functionality.loanBook(loanData)
                    return redirect(url_for("showLoan", id=res["id"]))
                except BaseException as e:
                    flash("Wystąpił błąd bazy danych!")
                    print(e)
            else:
                flash("Książka jest już wypożyczona!")
        else:
            flash("Wprowadzono nieprawidłowe dane!")
    return render_template("LoanBook.html", form = form)

@app.route("/loan/<id>", methods=["GET"])
def showLoan(id):
    id = request.view_args["id"]
    record = Functionality.getLoanById(id)
    return render_template("ShowDbEntry.html", record = record )

@app.route("/loan/all", methods=["GET"])
def showAllLoans():
    records = Functionality.getAllLoans()
    return render_template("ShowDbEntries.html", records=records)

@app.route("/loan/return", methods=["GET", "POST"])
def returnBook():
    form = ReturnBookForm()
    if request.method == "POST": 
        if form.validate():
                try:
                    res = Functionality.returnBook(form.data)
                    print(res)
                    return redirect(url_for("showLoan", id=res["id"]))
                except BaseException as e:
                    flash("Wystąpił błąd bazy danych!")
                    print(e)
        else:
            flash("Wprowadzono nieprawidłowe dane!")
    return render_template("ReturnBook.html", form = form)




@app.route("/payment/", methods=["GET", "POST"])
def imposePayment():
    form = ImposePaymentForm()
    if request.method == "POST": 
        if form.validate():
                try:
                    res = Functionality.imposePayment(form.data)
                    print(res)
                    return redirect(url_for("showPayment", id=res["id"]))
                except BaseException as e:
                    flash("Wystąpił błąd bazy danych!")
                    print(e)
        else:
            flash("Wprowadzono nieprawidłowe dane!")
    return render_template("ImposePayment.html", form = form)

@app.route("/payment/<id>", methods=["GET"])
def showPayment(id):
    id = request.view_args["id"]
    record = Functionality.getPaymentById(id)
    return render_template("ShowDbEntry.html", record = record )

@app.route("/payment/all", methods=["GET"])
def showAllPayments():
    records = Functionality.getAllPayments()
    print(records)
    return render_template("ShowDbEntries.html", records=records)



if __name__ == "__main__":
    app.run(debug=True)