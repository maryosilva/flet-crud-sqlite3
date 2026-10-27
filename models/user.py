class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    @classmethod
    def from_row(cls, row):

        if not row:
            return None
        return cls(id=row["id"], name=row["name"])

    def to_dict(self):
        return {"id": self.id, "name": self.name}

    def __repr__(self):
        return f"<User {self.name}>"