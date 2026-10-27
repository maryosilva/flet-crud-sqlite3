import flet as ft
from components import user_list, user_form
from components.user_list import create_user_row


def main(page: ft.Page):
    page.title = "Crud users FLET"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    component_list_users = user_list()

    def on_user_created(user):
        component_list_users.controls.append(
            create_user_row(
                user,
                component_list_users
            )
        )

        # Aqui pode, porque a aplicação já foi renderizada
        component_list_users.update()

    component_form_user = user_form(
        on_user_created
    )

    main_column = ft.Column(
        controls=[
            component_form_user,
            component_list_users
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=40
    )

    main_content = ft.Container(
        content=main_column,
        alignment=ft.Alignment.CENTER,
        expand=True,
        width=568,
    )

    page.add(
        ft.SafeArea(
            content=main_content,
            expand=True,
            align=ft.Alignment.CENTER
        )
    )


if __name__ == "__main__":
    ft.run(main)