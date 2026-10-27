import flet as ft
from services import create_user


def user_form(on_user_created):

    input_name = ft.TextField(
        hint_text="Nome do usuário",
        height=48,
        expand=True,
        text_size=14,
        border_radius=10,
    )

    def on_click_user(e):
        try:
            user = create_user(input_name.value)

            input_name.value = ""
            input_name.update()

            # Adiciona somente o usuário criado
            on_user_created(user)

            e.control.page.show_dialog(
                ft.SnackBar(
                    content=ft.Text(
                        "Usuário registrado com sucesso!"
                    )
                )
            )

        except ValueError as err:
            e.control.page.show_dialog(
                ft.SnackBar(
                    content=ft.Text(str(err))
                )
            )

    button_register = ft.Button(
        content="Registrar",
        on_click=on_click_user,
        height=48,
    )

    return ft.Column(
        controls=[
            ft.Text(
                "Novo usuário",
                size=18,
                weight=ft.FontWeight.W_600,
            ),

            ft.Row(
                controls=[
                    input_name,
                    button_register,
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ],
    )