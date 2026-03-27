import flet as ft

import folder_watch

def main(page: ft.Page):
    async def handle_pick_files(e: ft.Event[ft.Button]):
        watch_switch.disabled=True
        watch_switch.value = False
        directory_path.value = ""
        files = await ft.FilePicker().pick_files(allow_multiple=False)
        selected_files.value = (
            ", ".join(map(lambda f: f.path, files)) if files else "Cancelled!"
        )


    async def handle_get_directory_path(e: ft.Event[ft.Button]):
        watch_switch.disabled=False
        selected_files.value = ""
        directory_path.value = await ft.FilePicker().get_directory_path()


    def handle_button_click(e: ft.Event[ft.Button]):
        folder_watch.folder_watch(directory_path.value or selected_files.value,watch_switch.value,black_bg=black_switch.value)

    page.add(
        ft.Row(
            controls=[
                ft.Button(
                    content="Pick files",
                    icon=ft.Icons.UPLOAD_FILE,
                    on_click=handle_pick_files,
                ),
                selected_files := ft.Text(),
            ]
        ),
        ft.Row(
            controls=[
                ft.Button(
                    content="Open directory",
                    icon=ft.Icons.FOLDER_OPEN,
                    on_click=handle_get_directory_path,
                    disabled=page.web,  # disable this button in web mode
                ),
                directory_path := ft.Text(),
            ]
        ),
        ft.Row(
            controls=[
                black_switch:=ft.Switch(label = "Black Background", value = False),
            ]
        ),
        ft.Row(
            controls=[
                watch_switch := ft.Switch(label="Folder Watch", value=False,disabled=True),
                start_btn := ft.Button(content="Start", on_click=handle_button_click),
            ]
        )
    )


if __name__ == "__main__":
    ft.run(main)