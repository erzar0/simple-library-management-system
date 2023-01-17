from flask import Flask, request, flash, render_template
import datetime

from models.PersonModel import PersonModel

from forms.RegisterMemberForm import RegisterMemberForm

app = Flask(__name__, template_folder="templates")
app.secret_key = "devvvvv"

Person = PersonModel()

@app.route("/")
def index():
    return render_template("base.html")

#Member
@app.route("/member/register", methods=["GET", "POST"])
def registerMember():
    form = RegisterMemberForm() 
    print(form.data)
    if request.method == "POST" and form.validate():
        person = dict()  
        person["first_name"] = form.first_name.data
        person["last_name"] = form.last_name.data
        person["pesel"] = form.pesel.data
        person["email"] = form.email.data
        person["birth_date"] = form.birth_date.data

        doesPersonExists = Person.findStrict({"pesel": 76081666598})
        if(doesPersonExists):
            return render_template("RegisterMember.html", form = form)

        render_template("base.html")
    else:
        flash("All fields are required")
        return render_template("RegisterMember.html", form = form)
        
    return render_template("RegisterMember.html", form = form)



if __name__ == "__main__":
    app.run(debug=True)