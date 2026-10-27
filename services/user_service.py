from database import get_db_connection
from models import User


def create_user(name: str) -> User | None:
    name = name.strip()

    if len(name) < 4:
        raise ValueError("Name length min 4 characters!")

    with get_db_connection() as conn:
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO usuarios (name) VALUES (?);",
                (name,)
            )

            user_id = cursor.lastrowid

            conn.commit()

            cursor.execute(
                "SELECT * FROM usuarios WHERE id = ?;",
                (user_id,)
            )

            row = cursor.fetchone()

            print(f"User register success - name: {name}")

            return User.from_row(row)

        except Exception as e:
            conn.rollback()
            raise e


def get_all_users() -> list[User | None]:
    with get_db_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios;")
        rows = cursor.fetchall()

        return [
            User.from_row(row)
            for row in rows
            if row is not None
        ]


def get_user_by_id(id: int) -> User | None:
    with get_db_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM usuarios WHERE id = ?;",
            (id,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return User.from_row(row)


def delete_user(id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()

        try:
            cursor.execute(
                "DELETE FROM usuarios WHERE id = ?;",
                (id,)
            )

            conn.commit()

            print("Deleted user success!")

        except Exception as e:
            conn.rollback()
            raise e


def update_user(id, name):
    name = name.strip()

    if len(name) < 4:
        raise ValueError(
            "Name length min 4 characters!"
        )

    with get_db_connection() as conn:
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                UPDATE usuarios
                SET name = ?
                WHERE id = ?;
                """,
                (name, id)
            )

            conn.commit()
            print("User update success!")

        except Exception as e:
            conn.rollback()
            raise e