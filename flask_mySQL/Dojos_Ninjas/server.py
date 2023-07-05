from flask_app import app
from flask_app.controllers import d_j_controller
from flask_app.models.d_j_model import Dojo, Ninja

if __name__ == "__main__":
    app.run(debug=True)
