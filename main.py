import json

import flet as ft
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "db.json")

def load_tasks() -> list[dict]:
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    return []


def save_tasks(tasks: list[dict]):
    with open(DB_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


def main(page: ft.Page):
    page.title = "Flet CRUD Tasks"
    page.bgcolor = "#FBF8FF"
    page.width = 776

    page.fonts = { "Geist": "https://github.com/vercel/geist-font/raw/main/fonts/geist-sans/Geist-Regular.ttf" }

    tasks_data: list[dict] = load_tasks()
    task_column = ft.Column(scroll=ft.ScrollMode.AUTO, height=400, expand=True)



    def render_task_item(task_dict: dict) -> ft.Row | None:

        if not task_dict['description']:
            return

        task_text = ft.Text(
            value=task_dict['description'],
            size=14,
            weight=ft.FontWeight.W_400,
            color="#1A1B22",
            style=ft.TextStyle(
                    decoration=ft.TextDecoration.LINE_THROUGH
                    if task_dict["isCompleted"] else
                    ft.TextDecoration.NONE, decoration_color="#767676",
                )
        )

        def task_changed_status(e: ft.Event[ft.Checkbox]):

            task_dict['isCompleted'] = e.control.value
            save_tasks(tasks_data)

            task_text.style = ft.TextStyle(
                decoration=ft.TextDecoration.LINE_THROUGH
                if task_dict['isCompleted']
                else ft.TextDecoration.NONE,
                decoration_color="#767676"
            )

            if task_dict['isCompleted']:
                edit_task_action.visible = False
            else:
                edit_task_action.visible = True

            page.update()

        def delete_this_task():
            task_column.controls.remove(task_row)
            tasks_data.remove(task_dict)

            if 'count_tasks' in globals() or 'count_tasks' in locals():
                count_tasks.value = f"{len(task_column.controls)} tarefas"

            save_tasks(tasks_data)
            page.update()



        def edit_task():

            task_row.visible = False

            def cancel_edit():
                task_column.controls.remove(task_edit_item)
                task_row.visible = True
                page.update()

            def update_task():
                if task_field.value.strip():
                    task_text.value = task_field.value.strip()
                    task_dict['description'] = task_text.value
                    save_tasks(tasks_data)

                task_column.controls.remove(task_edit_item)

                task_row.visible = True
                task_edit_item.visible = False

                page.update()

            task_field = ft.TextField(
                content_padding=14,
                width=342,
                height=40,
                value=task_text.value,
                color="#1A1B22",
                border={
                    ft.ControlState.DEFAULT: ft.UnderlineInputBorder(
                        side=ft.BorderSide(width=1, color="#5D5E66")
                    ),
                    ft.ControlState.FOCUSED: ft.UnderlineInputBorder(
                        side=ft.BorderSide(color="#1A1B22")
                    ),

                }
            )

            task_edit_item = ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    task_field,
                    ft.Row(
                        controls=[
                             ft.IconButton(
                                icon=ft.Icons.CHECK_OUTLINED,
                                icon_size=20,
                                icon_color="#5D5E66",
                                on_click=update_task
                            ),
                            ft.IconButton(
                                icon=ft.Icons.CLOSE_OUTLINED,
                                icon_size=20,
                                icon_color="#5D5E66",
                                on_click=cancel_edit
                            )
                        ]
                    )
                ]
            )


            task_index = task_column.controls.index(task_row)
            task_column.controls.insert(task_index + 1, task_edit_item)
            page.update()


        task_row = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    controls=[
                        ft.Checkbox(
                            border_side=ft.BorderSide(
                               color="#767676",
                           ),
                           check_color="#000000",
                           fill_color={
                               ft.ControlState.SELECTED: "#FFFFFF",
                           },
                           on_change=task_changed_status,
                           value=task_dict['isCompleted']
                        ),
                        task_text,
                    ]
                ),
                ft.Row(
                    controls=[
                        edit_task_action := ft.IconButton(
                               icon=ft.Icons.EDIT_OUTLINED,
                               icon_size=20,
                               icon_color="#5D5E66",
                               on_click=edit_task,
                               visible=not task_dict['isCompleted']
                        ),
                        delete_task_action := ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINED,
                            icon_size=20,
                            icon_color="#5D5E66",
                            on_click=delete_this_task
                        )
                    ]
                )
            ]
        )

        if 'count_tasks' in globals() or 'count_tasks' in locals():
            count_tasks.value = f"{len(task_column.controls)} tarefas"

        page.update()


        return task_row


    def add_task_click():

        if description.value.strip():

            new_task = {
                "id": len(tasks_data) + 1,
                "description": description.value.strip(),
                "isCompleted": False
            }

            tasks_data.append(new_task)
            save_tasks(tasks_data)

            task_item = render_task_item(new_task)

            if task_item is not None:
                task_column.controls.append(task_item)

            description.value = ""
            page.update()


    form = ft.Column(
        width=576,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        spacing=32,
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(
                            value="Nova Tarefa",
                            color="#1A1B22",
                            size=24,
                            font_family="Geist",
                            weight=ft.FontWeight.W_600
                        ),

                        ft.Text(
                            value="Organize suas tarefas de forma simples.",
                            color="#5D5E66",
                            size=14,
                            font_family="Geist",
                            weight=ft.FontWeight.W_500
                        ),
                    ],
                    spacing=6
            )),

            ft.Container(
                 bgcolor="#FFFFFF",
                 padding=20,
                 width=544,
                 content=ft.Column(
                     alignment=ft.MainAxisAlignment.START,
                     controls=[
                         ft.Text(
                             value="TÍTULO DA TAREFA",
                             color="#5D5E66",
                             size=12,
                             font_family="Geist",
                             weight=ft.FontWeight.W_500
                         ),

                         ft.Row(
                             controls=[
                                 ft.Container(
                                     bgcolor="#FBF8FF",
                                     border_radius=4,
                                     content = (
                                         description := ft.TextField(
                                             content_padding=14,
                                             width=342,
                                             height=40,
                                             hint_text="Digite uma nova tarefa...",
                                             color="#1A1B22",
                                             border={
                                                 ft.ControlState.DEFAULT: ft.OutlineInputBorder(
                                                     border_radius=4,
                                                     side=ft.BorderSide(width=1, color=ft.Colors.TRANSPARENT)
                                                 ),
                                                 ft.ControlState.FOCUSED: ft.OutlineInputBorder(
                                                     side=ft.BorderSide(color="#1A1B22")
                                                 )
                                             }
                                         )
                                     ),
                                     shadow=ft.BoxShadow(spread_radius=1, color=ft.Colors.BLACK_12, offset=ft.Offset(0, 0))
                                 ),

                                  ft.Button(
                                     content="Adicionar tarefa",
                                     width=150,
                                     height=40,
                                     color="#FFFFFF",
                                     style=ft.ButtonStyle(
                                         padding=16,
                                         shape=ft.RoundedRectangleBorder(radius=4)

                                     ),
                                     icon=ft.Icons.ADD,
                                     on_click=add_task_click
                                 )
                             ],
                             spacing=10
                         )
                     ],
                     spacing=12
                 )
             ),

             ft.Container(
                 content= ft.Column(
                     controls=[
                         ft.Row(
                             vertical_alignment=ft.CrossAxisAlignment.CENTER,
                             height=28,
                             controls=[
                                 ft.Text(
                                     value="Minhas tarefas",
                                     color="#1A1B22",
                                     size=20,
                                     weight=ft.FontWeight.W_500,
                                     font_family="Geist",
                                 ),
                                ft.Container(
                                    bgcolor="#EEEDF7",
                                    padding=ft.Padding.symmetric(vertical=2, horizontal=8),
                                    border_radius=12,
                                     content= (
                                         count_tasks := ft.Text(
                                             value="0 tarefas",
                                             size=12,
                                             color="#5D5E66",
                                             font_family="Geist",
                                             weight=ft.FontWeight.W_500,
                                             text_align=ft.TextAlign.CENTER,
                                         )
                                     )
                                 )
                             ]
                         )
                     ]
                 )
             ),

             ft.Container(
                 content=task_column
             )
        ],

    )

    for item in tasks_data:
        task_item = render_task_item(item)

        if task_item is not None:
            task_column.controls.append(task_item)


    main = ft.Container(
        content=form,
        alignment=ft.Alignment.CENTER,
        margin=ft.Margin.only(top=72),

    )

    page.add(ft.SafeArea(content=main))


if __name__ == "__main__":
    ft.run(main)
