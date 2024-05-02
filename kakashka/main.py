import flet as ft
from views.routes import router
from user_controls.app_bar import NavBar
# import entrance.main_window as mw


def main(page: ft.Page):

    page.theme_mode = "light"
    page.appbar = NavBar(page)
    page.on_route_change = router.route_change
    router.page = page
    page.add(
        router.body
    )
    page.go('/')


ft.app(target=main, assets_dir="assets")
