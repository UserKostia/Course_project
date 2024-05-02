import flet as ft


def NavBar(page):

    NavBar = ft.AppBar(
            leading=ft.Icon(ft.icons.PEOPLE),
            leading_width=40,
            title=ft.Text("Medicine"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
                ft.IconButton(ft.icons.PEOPLE_OUTLINE, on_click=lambda _: page.go('/doc_rec')),
                ft.IconButton(ft.icons.PERSON_2_OUTLINED, on_click=lambda _: page.go('/patient')),
                ft.IconButton(ft.icons.SETTINGS, on_click=lambda _: page.go('/settings'))
            ]
    )

    return NavBar
