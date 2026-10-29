class UserModel:
    def __init__(self, user_id=None, username="", email="", points=0):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.points = points

    def update_username(self, new_username: str):
        if new_username.strip():
            self.username = new_username.strip()
            return True
        return False

    def update_email(self, new_email: str):
        if "@" in new_email:
            self.email = new_email.strip()
            return True
        return False

    def add_points(self, amount: int):
        if amount > 0:
            self.points += amount

    def reset_data(self):
        self.username = ""
        self.email = ""
        self.points = 0