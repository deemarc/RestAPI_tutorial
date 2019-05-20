import sqlite3

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,)) # the value need to be ion the form of tuple
        row = result.fetchone()
        if row:
            # user = cls(row[0],row[1],row[2])
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cobs, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
    
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,)) # the value need to be ion the form of tuple
        row = result.fetchone()
        if row:
            # user = cls(row[0],row[1],row[2])
            user = cls(*row)
        else:
            user = None

        connection.close()  
        return user