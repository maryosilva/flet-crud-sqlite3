import flet as ft
from services import get_all_users
from .user_delete import user_delete
from .user_update import user_update


def create_user_row(user, users_column):

    name_text = ft.Text(
        user.name,
        size=15,
        weight=ft.FontWeight.W_500,
        expand=3,
    )

    row = ft.Row()

    def on_deleted():
        users_column.controls.remove(row)
        users_column.update()

    def on_updated(new_name):
        name_text.value = new_name
        name_text.update()

    row.controls = [
        ft.Text(
            f"{user.id:02d}",
            size=14,
            weight=ft.FontWeight.W_600,
            expand=1,
        ),

        name_text,

        ft.Row(
            controls=[
                user_update(
                    user=user,
                    on_updated=on_updated,
                ),

                user_delete(
                    user=user,
                    on_deleted=on_deleted,
                ),
            ],
            spacing=5,
            expand=1,
        ),
    ]

    row.vertical_alignment = ft.CrossAxisAlignment.CENTER

    return row


def user_list():

    users = get_all_users()

    users_column = ft.Column(
        spacing=10,
        scroll=ft.ScrollMode.HIDDEN,
        expand=True,
    )

    for user in users:
        if user is not None:
            users_column.controls.append(
                create_user_row(
                    user,
                    users_column
                )
            )

    return users_column