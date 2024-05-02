import flet as ft
import sqlite3


def main(page: ft.Page):
    page.title = "Registration"
    page.theme_mode = 'dark'
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_maximized = True
    page.window_resizable = False

    def register(e):
        db = sqlite3.connect('Registration.db')
        cur = db.cursor()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                login VARCHAR(30),
                pass VARCHAR(30)
            )'''
        )
        cur.execute(f"INSERT INTO users VALUES (NULL, '{user_login.value}', '{user_pass.value}')")
        db.commit()
        db.close()

        user_login.value = ''
        user_pass.value = ''
        btn_regist.text = 'Added'
        page.update()

    def auth_user(e):
        db = sqlite3.connect('Registration.db')
        cur = db.cursor()

        cur.execute(f"SELECT * FROM users WHERE login = '{user_login.value}' AND pass = '{user_pass.value}'")

        if cur.fetchone() != None:
            user_login.value = ''
            user_pass.value = ''
            btn_regist.text = 'Authorized'

            if len(page.navigation_bar.destinations) == 2:
                page.clean()
                page.snack_bar.open = False
                ft.app(target=main.main(page))
                page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text('Error data!'))
            page.snack_bar.open = True

        db.commit()
        db.close()
        page.update()

    def validat(e):
        if all([user_login.value, user_pass.value]):
            btn_regist.disabled = False
            btn_auth.disabled = False
        else:
            btn_regist.disabled = True
            btn_auth.disabled = True
        page.update()

    user_login = ft.TextField(label='Login...', width=350, on_change=validat)
    user_pass = ft.TextField(label='Password...', password=True, width=350, on_change=validat)
    btn_regist = ft.OutlinedButton(text='Sign Up', width=350, on_click=register, disabled=True)
    btn_auth = ft.OutlinedButton(text='Sign In', width=350, on_click=auth_user, disabled=True)

    panel_register = ft.Row(
        [
            ft.Column
            (
                [
                    ft.Text('\n\n\n               Sign Up', size=30),
                    user_login,
                    user_pass,
                    btn_regist
                ]
            )
        ], alignment=ft.MainAxisAlignment.CENTER,
    )

    panel_auth = ft.Row(
        [
            ft.Column
            (
                [
                    ft.Text('\n\n\n               Sing In', size=30),
                    user_login,
                    user_pass,
                    btn_auth
                ]
            )
        ], alignment=ft.MainAxisAlignment.CENTER
    )

    def navigate(e):
        page.clean()
        index = page.navigation_bar.selected_index

        if index == 0:
            page.add(panel_register)
        elif index == 1:
            page.add(panel_auth)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.VERIFIED_USER, label="Registration"),
            ft.NavigationDestination(icon=ft.icons.VERIFIED_USER_OUTLINED, label="Authorization")
        ], on_change=navigate
    )
    ft.NavigationBar(ft.icons.VERIFIED_USER, label_behavior="Registration")
    ft.NavigationBar(ft.icons.VERIFIED_USER_OUTLINED, label_behavior="Authorization")

    page.add(panel_register)


ft.app(target=main)
