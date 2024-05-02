import flet as ft
import reg_author
from flet import MainAxisAlignment


def main(page: ft.Page):
    page.title = "Registration"
    page.theme_mode = "light"
    page.window_maximized = True
    page.window_resizable = True
    page.window_min_height = 750
    page.window_min_width = 900
    page.vertical_alignment = MainAxisAlignment.CENTER

    find_doctor_text = ft.Text('Переглянути лікарів', size=80, color='Blue')
    find_doctor_text_field = ft.TextField(label='Введіть ПІБ лікаря або спеціальність', width=650)
    search_doctor_btn = ft.ElevatedButton(text="Пошук", width=300, height=70)

    text_background = ft.Row(
        [
            ft.Column(
                [
                    find_doctor_text,
                    find_doctor_text_field,
                    search_doctor_btn
                ], alignment=MainAxisAlignment.CENTER
            )
        ]
    )

    page.add(text_background)

    def exit_app(e):
        page = e.page
        page.window_destroy()

    def goto_reg_author(e):
        page = e.page
        page.window_destroy()
        ft.app(target=reg_author.main)
        page.update()

    create_akk = ft.Text("`\n\n\n\n\n\n Бажаєте увійти?", size=20)
    enter_btn = ft.CupertinoButton(text='Увійти', on_click=goto_reg_author, width=150)
    reg_line = ft.Row(
        [
            ft.Column(
                [
                    create_akk,
                    enter_btn
                ], alignment=ft.MainAxisAlignment.CENTER
            )
        ], alignment=ft.MainAxisAlignment.CENTER, width=1330
    )

    page.add(reg_line)
    page.update()


ft.app(target=main)
