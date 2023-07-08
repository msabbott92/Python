from flask_app import app
from flask_app.controllers import cookie_controller
from flask_app.models.cookie_model import Cookie


if __name__ == "__main__":
    app.run(debug=True)