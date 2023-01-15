from flask import Flask, request, flash, render_template

from models.Person import Person

from forms.addPerson import AddPersonForm

app = Flask(__name__, template_folder="templates")

app.secret_key = "devvvvv"

@app.route("/")
def index():
    return "hello"

@app.route("/person", methods=["GET", "POST"])
def person():
    form = AddPersonForm() 
    if request.method == "POST":
        if form.validate() == False:
            flash("All fields are required")
            return render_template("addPersonForm.html", form = form)
    elif request.method == "GET": 
        return render_template("addPersonForm.html", form = form)


if __name__ == "__main__":
    app.run(debug=True)