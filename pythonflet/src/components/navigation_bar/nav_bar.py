import flet as ft
from pythonflet.src.State import global_state
from flet import Row, Container


def show_menu_bar(page: global_state.get_state_by_key('page')):
    nav_bar_pannel = Row(
        [
            Container(
                ft.Icon(ft.icons.PEOPLE),

                padding=ft.padding.only(left=10),
                bgcolor=ft.colors.SURFACE_VARIANT,
                alignment=ft.alignment.center_left,
                width=60,
                height=50,
            ),
            Container(
                ft.Text("Medicine", size=25, font_family="TimesNewRoman", weight=ft.FontWeight.W_700),
                alignment=ft.alignment.center_left,
                bgcolor=ft.colors.SURFACE_VARIANT,
                width=960,
                height=50,
            ),
            Container(
                ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/main'), tooltip="Лікарі", ),
                bgcolor=ft.colors.SURFACE_VARIANT,
                width=60,
                height=50,
            ),
            Container(
                content=ft.IconButton(ft.icons.PEOPLE_OUTLINE, on_click=lambda _: page.go('/doc_rec'),
                                      tooltip="Записи до лікарів"),
                bgcolor=ft.colors.SURFACE_VARIANT,
                width=60,
                height=50
            ),
            Container(
                content=ft.IconButton(ft.icons.PERSON_2_OUTLINED, on_click=lambda _: page.go('/patient'),
                                      tooltip="Пацієнти"),
                bgcolor=ft.colors.SURFACE_VARIANT,
                width=60,
                height=50
            ),
            Container(
                content=ft.IconButton(ft.icons.SETTINGS, on_click=lambda _: page.go('/settings'),
                                      tooltip="Налаштування"),
                bgcolor=ft.colors.SURFACE_VARIANT,
                width=60,
                height=50
            ),
        ],
        spacing=0
    )

    return nav_bar_pannel


page = global_state.get_state_by_key('page')
