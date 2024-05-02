import datetime
import flet as ft
from typing import Union
from kakashka.views.Router import Router

from flet import (
    Row,
    Page,
    Text,
    Image,
    Column,
    colors,
    padding,
    Container,
    TextField,
    FontWeight,
    DatePicker,
    CircleAvatar,
    ElevatedButton)


def patiens_view(page: Page, router: Union[Router, str, None] = None):
    page.title = "Пацієнти"
    page.window_maximizable = True
    page.window_resizable = True

    avatar = CircleAvatar(
        foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
        content=Text("FF"),
    )

    title = Text("ПАЦІЄНТИ", font_family="Merriweather", size=40, weight=FontWeight.W_600)
    title.text_align = ft.TextAlign.CENTER
    header = ft.Row(
        [
            Container(
                content=title,
                # expand=True,
                bgcolor=colors.BLUE_GREY_50,
                height=65,
                padding=padding.only(left=20),
                border=ft.border.all(1, ft.colors.GREY),
                width=1200
            ),
            Container(
                content=avatar,
                padding=padding.only(right=10, top=10),
                height=65,
                width=65
            ),
        ],
        width=1210
    )

    def change_date():
        print(f"Date picker changed, value is {date_picker.value}")

    def date_picker_dismissed():
        print(f"Date picker dismissed, value is {date_picker.value}")

    find_pationt_field = TextField(label="Пошук по списку: введіть ПІБ пацієнта",
                                   width=700,
                                   height=45)

    scroll_left_date_btn = ElevatedButton(text="<", height=35)

    date_picker = DatePicker(on_change=change_date,
                             on_dismiss=date_picker_dismissed,
                             first_date=datetime.datetime(2023, 10, 1),
                             last_date=datetime.datetime(2024, 10, 1), )

    scroll_right_date_btn = ElevatedButton(text=">", height=35)
    # page.overlay.append(date_picker)

    def pick_date(self):
        self.open = True
        # self.update()

    date_button = ElevatedButton(
        "Дата",
        width=130,
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: pick_date(),
    )

    add_patient_btn = ElevatedButton("Записати пацієнта")
    navigation = Row(
        [
            Container(content=find_pationt_field),
            Container(content=scroll_left_date_btn),
            Container(content=date_button),
            Container(content=scroll_right_date_btn),
            Container(content=add_patient_btn)
        ],
    )

    name = Text("name", size=18, font_family="TimesNewRoman")
    surname = Text("surname", size=18, font_family="TimesNewRoman")
    maddlename = Text("maddlename", size=18, font_family="TimesNewRoman")

    complaint = Text("complaint", size=16, font_family="TimesNewRoman")
    registration_date = Text("Дата та час", size=16, font_family="TimesNewRoman")
    patient_content = Row(
        [
            Container(
                Image(
                    src="./img/me.png",
                    width=150,
                    height=150,
                ),
                height=150,
                padding=ft.padding.only(left=10, top=10, bottom=10, right=20),
                bgcolor=colors.GREY_200,
                alignment=ft.alignment.center,
                margin=ft.margin.only(left=30)
            ),
            Container(
                Column([
                    Container(
                        name,
                        margin=ft.margin.only(top=20),
                    ),
                    Container(
                        surname,
                    ),
                    Container(
                        maddlename,
                    )
                ]),
                width=370,
                bgcolor=colors.GREY_200,
                height=150,
            ),
            Container(
                Column([complaint]),
                bgcolor=colors.GREY_200,
                height=150,
                width=380,
            ),
            Container(
                registration_date,
                margin=ft.margin.only(right=20),
                width=250,
                height=150,
                bgcolor=colors.GREY_200,
            )
        ],
        spacing=0
    )

    body = Column(
        spacing=10,
        height=500,
        width=1250,
        scroll=ft.ScrollMode.ALWAYS,
        adaptive=True
    )

    i = 0
    while i < 10:
        body.controls.append(patient_content)
        i += 1

    # rail = NavigationRail(
    #     # selected_index=0,
    #     # label_type=ft.NavigationRailLabelType.ALL,
    #     # min_width=100,
    #     # min_extended_width=400,
    #     # leading=FloatingActionButton(icon=icons.CREATE, text="Додати\nпацієнта"),
    #     # group_alignment=-0.9,
    #     destinations=[
    #         NavigationRailDestination(
    #             icon=icons.PEOPLE,
    #             selected_icon=icons.PEOPLE_OUTLINE,
    #             label="Пацієнти"
    #         ),
    #         NavigationRailDestination(
    #             icon_content=Icon(icons.PERSON_2),
    #             selected_icon_content=Icon(icons.PERSON_2_OUTLINED),
    #             label="Лікарі",
    #         ),
    #         NavigationRailDestination(
    #             icon_content=Icon(icons.BOOKMARK),
    #             selected_icon_content=Icon(icons.BOOKMARK_BORDER_SHARP),
    #             label="Мої записи",
    #         ),
    #         NavigationRailDestination(
    #             icon=icons.SETTINGS_OUTLINED,
    #             selected_icon_content=Icon(icons.SETTINGS),
    #             label_content=Text("Settings"),
    #         ),
    #     ],
    #     on_change=lambda e: print("Selected destination:", e.control.selected_index),
    # )

    main_body = Row(
        [
            Column(
                [
                    header,
                    navigation,
                    Container(body, border=ft.border.all(1))
                ]
            ),
        ],
        height=1500,
        width=900
    )

    return main_body
