import database as db
import user_profile as up




class UserService:



    def get_user_by_login(self, login):
        return db.Database('database.db').get_user(login)

    def add_new_user(user):
        return db.Database('database.db').save_user(user)
