from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo




@app.route("/dojos")
def dashboard():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("dojos.html", dojos=dojos )


@app.route('/dojo/add', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route("/dojos/<int:id>")
def show_dojo(id):
    data={
        "id":id
    }
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("dojos_id.html", dojo = dojo)



