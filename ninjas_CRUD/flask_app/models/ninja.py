from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo
class Ninja:
    db_name = "dojos_ninjas"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojo= [] 


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        if results:
            ninjas = []
            for ninja in results:
                ninjas.append(cls(ninja))
            return ninjas
        else:
            return []

    @classmethod
    def save(cls, data):
        query =  "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s, %(dojo_id)s );"
        return connectToMySQL('dojos_ninjas').query_db(query, data)
    
    
    @classmethod
    def get_one_ninja(cls,ninja_id):
        query = """
        SELECT * FROM ninjas WHERE id = %(id)s;
        """
        data ={ 'id':ninja_id}
        results = connectToMySQL('dojos_ninjas').query_db(query,data)
        new_ninja_object = cls(results[0])
        return new_ninja_object
    
    @classmethod
    def update(cls,data):
        query = """UPDATE ninjas 
                SET first_name=%(first_name)s,last_name=%(last_name)s,age=%(age)s WHERE id = %(id)s;"""
        return connectToMySQL('dojos_ninjas').query_db(query,data)

    @classmethod
    def delete(cls,ninja_id):
        query  = "DELETE FROM ninjas WHERE id = %(id)s;"
        data = {"id": ninja_id}
        return connectToMySQL('dojos_ninjas').query_db(query, data)


