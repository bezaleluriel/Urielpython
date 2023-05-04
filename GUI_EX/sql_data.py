import sqlite3
import csv

class UserExistsException(Exception):
    pass

class UserManager():
    def __init__(self):
        self.conn = sqlite3.connect('sql/sql_data.db')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def user_exists(self, user_name, password=None):
        query = f"select count(*) from users where username = '{user_name}'"
        if password != None:
            query += f" and password = '{password}'"
        users = self.cursor.execute(query)
        return users.fetchone()[0] > 0


    def add_user(self, user_name, password):
        if self.user_exists(user_name):
            raise UserExistsException('user already exists')
        else:
            query = f"INSERT into users(username, password) VALUES('{user_name}','{password}')"
            self.cursor.execute(query)
            self.conn.commit()




# um = UserManager()
# print(um.user_exists('admin', 'admin'))
# um.add_user('nadav', '123')