from flask_app import app
from flask_app.controllers import ninjas, dojos
from flask_app.models import dojo, ninja


if __name__=="__main__":
    app.run(debug=True, host="localhost", port=8000)

