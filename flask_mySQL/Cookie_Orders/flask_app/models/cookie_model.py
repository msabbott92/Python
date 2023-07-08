from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Cookie:
    def __init__(self, data):
            self.id = data['id']
            self.name = data['name']
            self.cookie_type = data['cookie_type']
            self.num_boxes = data['num_boxes']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookie_orders"
        results = connectToMySQL('cookies_schema').query_db(query)
        cookies = []
        for c in results:
            cookies.append(cls(c))
        return cookies
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO cookie_orders (name, cookie_type, num_boxes, created_at, updated_at) VALUES (%(name)s, %(cookie_type)s, %(num_boxes)s, NOW(), NOW());"
        result = connectToMySQL('cookies_schema').query_db(query, data)
        return result
    
    @classmethod
    def update(cls,data):
        query = "UPDATE cookie_orders SET name=%(name)s,cookie_type=%(cookie_type)s,num_boxes=%(num_boxes)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('cookies_schema').query_db(query,data)
    
    @staticmethod
    def validate_cookie(cookie):
        is_valid = True
        if len(cookie['name']) < 2:
            flash("Name is reqired")
            is_valid = False
        if len(cookie['cookie_type']) < 2:
            flash("Cookie type is required")
            is_valid = False
        if len(cookie[('num_boxes')]) == 0:
            flash("Enter valid amount of boxes")
            is_valid = False
        elif int(cookie['num_boxes']) <= 0:
            flash("Must be valid positive number")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM cookie_orders WHERE id = %(id)s;"
        result = connectToMySQL('cookies_schema').query_db(query,data)
        return cls(result[0])

