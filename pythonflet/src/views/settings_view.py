import flet as ft

from pythonflet.src.components.navigation_bar.nav_bar import show_menu_bar
from State import global_state


def settings_view(_):
    page = global_state.get_state_by_key('page')

    def toggle_dark_mode(_):
        if page.theme_mode == "light":
            page.theme_mode = "dark"
            page.update()
        else: 
            page.theme_mode = "light"
            page.update()

    def exit_app(_):
        page.window_destroy()

    def block_app(_):
        page.go("/")
    
    content = ft.Column(
        [
            show_menu_bar(page),
            ft.Row(
            [
                ft.Text("My Settings", size=30),
                ft.IconButton(icon=ft.icons.SETTINGS_ROUNDED, icon_size=30),
            ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    ft.TextButton("Light/Dark Mode", icon=ft.icons.WB_SUNNY_OUTLINED, on_click=toggle_dark_mode)
                ],
            ),
            ft.Row(
                [
                    ft.TextButton("Exit Application", icon=ft.icons.CLOSE, on_click=exit_app, icon_color="red")
                ],
            ),
            ft.Row(
                [
                    ft.TextButton("Заблокувати", icon=ft.icons.BLOCK, on_click=block_app, icon_color="red")
                ],
            ),
        ],
    )

    return content
