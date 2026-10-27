import flet as ft
from services import delete_user


def user_delete(user, on_deleted):

    def confirm_delete(e):
        page = e.control.page

        try:
            delete_user(user.id)

            page.pop_dialog()

            # Remove a linha da interface
            on_deleted()

            page.show_dialog(
                ft.SnackBar(
                    content=ft.Text("Usuário excluído com sucesso!")
                )
            )

        except Exception as err:
            page.pop_dialog()

            page.show_dialog(
                ft.SnackBar(
                    content=ft.Text(str(err))
                )
            )

    def open_delete_dialog(e):
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Excluir usuário"),
            content=ft.Text(
                f"Deseja realmente excluir {user.name}?"
            ),
            actions=[
                ft.TextButton(
                    "Cancelar",
                    on_click=lambda e: e.control.page.pop_dialog(),
                ),
                ft.TextButton(
                    "Excluir",
                    on_click=confirm_delete,
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        e.control.page.show_dialog(dialog)

    return ft.IconButton(
        icon=ft.Icons.DELETE_OUTLINE,
        tooltip="Excluir usuário",
        on_click=open_delete_dialog,
    )