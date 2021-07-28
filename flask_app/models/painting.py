from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models.user import User

class Painting:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.quantity = data['quantity']
        self.count = data['count']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None
        self.buyer_id = None
        self.buyer = None

    @staticmethod
    def validate_painting(data):
        is_valid = True

        if len(data['title']) < 1 or len(data['title']) > 255:
            flash("Title should be between 1 to 255 characters")
            is_valid = False
        if len(data['description']) < 1 or len(data['description']) > 1000:
            flash("Description should be between 1 to 1000 characters")
            is_valid = False
        if len(data['price']) < 1:
            flash("Price should be greater than 0")
            is_valid = False
        if len(data['quantity']) < 1:
            flash("Quantity should be greater than 0")
            is_valid = False

        return is_valid

    @classmethod
    def get_all_paintings_with_user(cls):
        query = "SELECT * FROM paintings JOIN users ON paintings.user_id = users.id"

        results = connectToMySQL('python_exam2').query_db(query)

        all_paintings = []

        for item in results:
            painting = Painting(item)
            user_data = {
                'id': item['users.id'],
                'first_name': item['first_name'],
                'last_name': item['last_name'],
                'email': item['email'],
                'password': item['password'],
                'created_at': item['users.created_at'],
                'updated_at': item['users.updated_at']
            }
            painting.user = User(user_data)
            all_paintings.append(painting)
        
        return all_paintings

    @classmethod
    def get_all_paintings_with_user_by_painting_id(cls, data):
        query = "SELECT * FROM paintings JOIN users ON paintings.user_id = users.id WHERE paintings.id = %(id)s;"

        result = connectToMySQL('python_exam2').query_db(query, data)

        painting = Painting(result[0])

        user_data = {
            'id': result[0]['users.id'],
            'first_name': result[0]['first_name'],
            'last_name': result[0]['last_name'],
            'email': result[0]['email'],
            'password': result[0]['password'],
            'created_at': result[0]['users.created_at'],
            'updated_at': result[0]['users.updated_at'],
        }
        painting.user = User(user_data)
        
        return painting

    @classmethod
    def get_painting_by_id(cls, data):
        query = "SELECT * FROM paintings WHERE id = %(id)s;"

        result = connectToMySQL('python_exam2').query_db(query, data)

        painting = Painting(result[0])

        return painting

    @classmethod
    def insert_painting(cls, data):
        query = "INSERT INTO paintings (title, description, price, quantity, count, user_id) VALUES (%(title)s, %(description)s, %(price)s, %(quantity)s, %(count)s, %(user_id)s);"

        result = connectToMySQL('python_exam2').query_db(query, data)

        new_painting_id = result

        return new_painting_id

    @classmethod
    def update_painting(cls,data):
        query = "UPDATE paintings SET title = %(title)s, description = %(description)s, price = %(price)s, quantity = %(quantity)s WHERE id = %(id)s;"

        connectToMySQL('python_exam2').query_db(query, data)

    @classmethod
    def delete_painting(cls, data):
        query = "DELETE FROM paintings WHERE id = %(id)s;"

        connectToMySQL('python_exam2').query_db(query, data)

    @classmethod
    def buy_painting(cls, data):
        query = "UPDATE paintings SET count = count+1 WHERE id = %(id)s;"

        connectToMySQL('python_exam2').query_db(query, data)

        query2 = "INSERT INTO purchases (user_id, painting_id) VALUES (%(user_id)s, %(id)s);"

        result = connectToMySQL('python_exam2').query_db(query2, data)

        new_purchases_id = result

        return new_purchases_id

    @classmethod
    def get_paintings_purchases_by_user_id(cls, data):
        query = "SELECT * FROM paintings JOIN users ON paintings.user_id = users.id JOIN purchases ON paintings.id = purchases.painting_id WHERE purchases.user_id = %(id)s;"

        results = connectToMySQL('python_exam2').query_db(query, data)

        print("HEREEEEEEEEEEE")
        print(results)

        all_purchases = []

        for item in results:
            painting_data = {
                'id': item['id'],
                'title': item['title'],
                'description': item['description'],
                'price': item['price'],
                'quantity': item['quantity'],
                'count': item['count'],
                'created_at': item['created_at'],
                'updated_at': item['updated_at'],
                'user_id': item['user_id']
            }
            painting = Painting(painting_data)

            creator_data = {
                'id': item['users.id'],
                'first_name': item['first_name'],
                'last_name': item['last_name'],
                'email': item['email'],
                'password': item['password'],
                'created_at': item['users.created_at'],
                'updated_at': item['users.updated_at']
            }
            painting.user = User(creator_data)

            all_purchases.append(painting)
        
        return all_purchases