from flask import Flask, request, flash, render_template, redirect, url_for
from datetime import date, timedelta
import json

from app.forms.RegisterMemberForm import RegisterMemberForm
from app.forms.RegisterLibrarianForm import RegisterLibrarianForm
from app.forms.AddBookForm import AddBookForm
from app.forms.AddAuthorForm import AddAuthorForm


from app.models.PersonModel import PersonModel
from app.models.BookModel import BookModel 
def dumpJson(dict):
    return json.dumps(dict, indent=2, default=str, ensure_ascii=False)



app = Flask(__name__, template_folder="app/templates")
app.secret_key = "devvvvv"
app.static_folder = "app/static"

Person = PersonModel()
Book = BookModel()

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
                    print(res)
                    return redirect(url_for("showMember", id=res["id"]))

                except Exception as e:
                    flash("Wystąpił błąd bazy danych!")
                    print(e)
        else:
            flash("Wprowadzono nieprawidłowe dane!")
    return render_template("RegisterMember.html", form = form)

@app.route("/member/<id>", methods=["GET"])
def showMember(id):
    id = request.view_args["id"]
    record = Person.getMemberById(id)
    return render_template("ShowDbEntry.html", record = dumpJson(record))

@app.route("/member/all", methods=["GET"])
def showAllMembers():
    records = Person.getAllMembers()
    records = [dumpJson(record) for record in records]
    return render_template("ShowDbEntries.html", records=records)



@app.route("/librarian/register", methods=["GET", "POST"])
def registerLibrarian():
    form = RegisterLibrarianForm() 
    if request.method == "POST": 
        if form.validate():
                try:
                    res = Person.registerLibrarian(form.data)
                    return redirect(url_for("showLibrarian", id=res["id"]))
                except Exception as e:
                    flash("Wystąpił błąd bazy danych!")
                    print(e)
        else:
            flash("Wprowadzono nieprawidłowe dane!")

    return render_template("RegisterLibrarian.html", form = form)

@app.route("/librarian/<id>", methods=["GET"])
def showLibrarian(id):
    id = request.view_args["id"]
    record = Person.getLibrarianById(id)
    return render_template("ShowDbEntry.html", record = dumpJson(record) )

@app.route("/librarian/all", methods=["GET"])
def showAllLibrarians():
    records = Person.getAllLibrarians()
    records = [dumpJson(record) for record in records]
    return render_template("ShowDbEntries.html", records=records)



@app.route("/book/add", methods=["GET", "POST"])
def addBook():
    form = AddBookForm() 
    if request.method == "POST": 
        if form.validate():
                try:
                    res = Book.addBook()
                    # return redirect(url_for("showLibrarian", id=res["id"]))
                except Exception as e:
                    flash("Wystąpił błąd bazy danych!")
                    print(e)
        else:
            flash("Wprowadzono nieprawidłowe dane!")

    return render_template("AddBook.html", form = form)

@app.route("/book/author/add", methods=["GET", "POST"])
def addAuthor():
    form = AddAuthorForm() 
    if request.method == "POST": 
        if form.validate():
                try:
                    res = Book.addAuthor(form.data)
                    return redirect(url_for("showAuthor", id=res["id"]))
                except Exception as e:
                    flash("Wystąpił błąd bazy danych!")
                    print(e)
        else:
            flash("Wprowadzono nieprawidłowe dane!")

    return render_template("AddAuthor.html", form = form)

@app.route("/book/author/<id>", methods=["GET"])
def showAuthor(id):
    id = request.view_args["id"]
    record = Book.getAuthorById(id)
    return render_template("ShowDbEntry.html", record = dumpJson(record) )


if __name__ == "__main__":
    app.run(debug=True)