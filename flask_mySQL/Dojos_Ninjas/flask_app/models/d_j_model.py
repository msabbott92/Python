from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    DB = "dojos"
    def __init__( self , data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for d in results:
            dojos.append(cls(d))
        return dojos
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return result
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])