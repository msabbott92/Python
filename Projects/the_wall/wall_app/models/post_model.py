from wall_app.config.mysqlconnection import connectToMySQL
from flask import flash
from wall_app.models.wall_model import User

class Post:
    db = "wall_posts"
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = data["user"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts (content, created_at, updated_at, users_id) VALUES (%(content)s, NOW(), NOW(), %(users_id)s);"
        print(query)
        results = connectToMySQL('the_wall_schema').query_db(query,data)
        return results
    
    @classmethod
    def get_all_posts(cls):
        query = "SELECT * FROM posts JOIN users on posts.users_id = users.id"
        results = connectToMySQL('the_wall_schema').query_db(query)
        all_wall_posts = []
        
        for user in results:
            wall_user = ({
            "id": user["users_id"],
            "first_name": user["first_name"],
            "last_name": user["last_name"],
            "created_at": user["users.created_at"],
            "email": user["email"],
            })
            wall_post = ({
                "id": user["id"],
                "content": user["content"],
                "created_at": user["created_at"],
                "user": wall_user
            })
        all_wall_posts.append(wall_post)    

        return all_wall_posts
        
    
    @classmethod
    def validate_post(cls, data):
        is_valid = False
        if len(data["content"]) == 0:
            flash("Please do not leave content blank")
            is_valid = False
        return is_valid