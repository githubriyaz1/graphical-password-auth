import json

class User:
    def __init__(self, id, username, click_points):
        self.id = id
        self.username = username
        self.click_points = click_points

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "click_points": json.loads(self.click_points)
        }

    @staticmethod
    def from_row(row):
        return User(
            id=row["id"],
            username=row["username"],
            click_points=row["click_points"]
        )
