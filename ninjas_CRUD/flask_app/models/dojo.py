from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja, dojo

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        if results:
            dojos = []
            for dojo in results:
                dojos.append(cls(dojo))
            return dojos
        else:
            return []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_ninjas').query_db(query, data)
    
        
    @classmethod
    def get_one_dojo(cls,dojo_id):
        query = """
        SELECT * FROM dojos WHERE id = %(id)s;
        """
        data ={ 'id':dojo_id}
        results = connectToMySQL('dojos_ninjas').query_db(query,data)
        new_dojo_object = cls(results[0])
        return new_dojo_object
    
    @classmethod
    def get_dojo_with_ninjas(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_ninjas').query_db(query, data )
        print(results)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninja.Ninja( ninja_data))
        return dojo