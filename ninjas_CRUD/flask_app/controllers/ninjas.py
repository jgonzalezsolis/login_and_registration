from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/ninjas")
def form_ninjas():
    ninjas = Ninja.get_all()
    dojos = Dojo.get_all()
    print(ninjas)
    return render_template("ninjas.html", all_ninjas=ninjas, all_dojos=dojos )


@app.route('/ninja/add', methods=["POST"])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id" : request.form["dojo_id"]
    }
    Ninja.save(data)
    return redirect('/dojos')

@app.route('/ninja/update/<int:dojo_id>',methods=['POST'])
def update(dojo_id):
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "id": request.form["id"]
    }
    Ninja.update(data)
    return redirect(f"/dojos/{dojo_id}")


@app.route('/update/ninja/<int:ninja_id>/<int:dojo_id>')
def update_ninja(ninja_id,dojo_id):
    ninja = Ninja.get_one_ninja(ninja_id)
    dojo = Dojo.get_one_dojo(dojo_id)
    return render_template("edit_ninja.html", ninja=ninja, dojo=dojo )

@app.route('/ninja/delete/<int:ninja_id>/<int:dojo_id>')
def delete(ninja_id, dojo_id): 
    Ninja.delete(ninja_id)
    return redirect(f"/dojos/{dojo_id}")

