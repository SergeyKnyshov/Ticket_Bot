
class UserProfile:

    def __init__(self, user_id,login,password):
        self.user_id = user_id
        self.login = login
        self.password = password

    def get_user_id(self):
        return self.user_id

    def get_login(self):
        return self.login

    def get_pass(self):
        return self.password



