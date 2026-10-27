import flet as ft
from services import update_user


def user_update(user, on_updated):

    current_name = user.name

    input_name = ft.TextField(
        value=current_name,
        hint_text="Nome do usuário",
        text_size=14,
        autofocus=True,
    )

    def save_user(e):
        nonlocal current_name

        name = input_name.value.strip()

        try:
            update_user(user.id, name)

            current_name = name

            # Atualiza somente o nome na interface
            on_updated(name)

            e.control.page.pop_dialog()

            e.control.page.show_dialog(
                ft.SnackBar(
                    content=ft.Text(
                        "Usuário atualizado com sucesso!"
                    )
                )
            )

        except ValueError as err:
            e.control.page.show_dialog(
                ft.SnackBar(
                    content=ft.Text(str(err))
                )
            )

    def open_update_dialog(e):
        input_name.value = current_name

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Editar usuário"),
            content=ft.Container(
                content=input_name,
                width=350,
            ),
            actions=[
                ft.TextButton(
                    "Cancelar",
                    on_click=lambda e: e.control.page.pop_dialog(),
                ),
                ft.Button(
                    content="Salvar",
                    on_click=save_user,
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        e.control.page.show_dialog(dialog)

    return ft.IconButton(
        icon=ft.Icons.EDIT_OUTLINED,
        tooltip="Editar usuário",
        on_click=open_update_dialog,
    )