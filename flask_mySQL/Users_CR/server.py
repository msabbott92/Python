from flask_app import app
from flask_app.controllers import users


from flask_app.models import user
app = Flask(__name__)



if __name__ == "__main__":
    app.run(debug=True)