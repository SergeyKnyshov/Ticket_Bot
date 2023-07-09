import sqlite3
from user_profile import UserProfile

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def get_user(self, login):
        with self.connection:
            self.cursor.execute("SELECT * FROM users WHERE login = ?", (login,))
            row = self.cursor.fetchone()
            return row

    def save_user(self, user_profile):
        sett = False
        try:
            with self.connection:
                self.cursor.execute("INSERT INTO users (user_id, login, password) VALUES (?, ?, ?)",
                                    (user_profile.get_user_id(), user_profile.get_login(), user_profile.get_pass()))
                sett = True
        except sqlite3.Error:
            print("Ошибка в сохранении пользователя")
        return sett
