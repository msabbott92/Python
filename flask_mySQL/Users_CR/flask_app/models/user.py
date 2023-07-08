from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB = "users"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"

        results = connectToMySQL('users_schema').query_db(query)

        users = []

        for u in results:
            users.append(cls(u))
        return users
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        result = connectToMySQL('users_schema').query_db(query, data)
        return result
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('users_schema').query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 3:
            flash("First name is reqired")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name is required")
            is_valid = False
        if len(user['email']) < 3:
            flash("Email is reqired")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid

#FOR FUTURE REFERENCE
        # # SENSEI way using a for loop (Good for if there are many fields)
        # # Loop over the dictionary with the user data
        # for field in user:
        #     # Test if any of the entered values are empty strings
        #     if len(user[field]) <= 0:
        #         is_valid = False
        #         message = f"{field} is required.".capitalize()

        #         # Take the _ out of the field names
        #         make_pretty = message.maketrans("_", " ")
        #         flash(message.translate(make_pretty))
