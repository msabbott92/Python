from wall_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "users"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('the_wall_schema').query_db(query)
        users = []
        for u in results:
            users.append(cls(u))
        return users
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        result = connectToMySQL('the_wall_schema').query_db(query, data)
        return result
    
    @staticmethod
    def validate_user(user): 
        is_valid = True
        if len(user['first_name']) < 2:
            flash("First name is reqired", "register")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name is required", "register")
            is_valid = False
        if len(user['email']) < 2:
            flash("Email is required", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!", "register")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Passwords don't match","register")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_by_email(cls,data):
        print(data, "method")
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        result = connectToMySQL("the_wall_schema").query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('the_wall_schema').query_db(query,data)
        return cls(result[0])