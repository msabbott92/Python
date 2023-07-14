from wall_app import app
from wall_app.controllers import wall_controller, post_controller
from wall_app.models.wall_model import User
from wall_app.models.post_model import Post


if __name__ == "__main__":
    app.run(debug=True)