import csv

class UserExistsException(Exception):
    pass

class UserManager():
    def __init__(self):
        self.db = "users.csv"
        self.f = open(self.db, "r+")
        self.fieldnames = self.f.readline().replace('\n', '').split(',')
        # because we search and want to return to start each time
        self.f.seek(0)

    # destructor
    def __del__(self):
        self.f.close()

    def user_exists(self, user_name, password=None):
        users = csv.DictReader(self.f, fieldnames=self.fieldnames)

        for user in users:
              if user['username'] == user_name:
                  if password == user['password']:
                    return True
        return False

    def add_user(self, user_name, password):
        if self.user_exists(user_name):
            raise UserExistsException('user already exists')
        else:
            self.f.seek(0)
            next_user_id = int(self.f.readlines()[-1].split(',')[0]) + 1
            self.f.write(f'\n{next_user_id},{user_name},{password}')




# user1 = UserManager()
# print(user1.user_exists('uriel'))
# print(user1.add_user('jhon', '1234'))