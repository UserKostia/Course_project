import sqlite3
import flet as ft
from flet import (
    Row,
    Text,
    Image,
    Column,
    colors,
    padding,
    Container,
    TextField,
    FontWeight,
    TextButton,
    OutlinedButton)

from State import global_state
from pythonflet.src.classes.doctor import Doctor as Doc
from pythonflet.src.components.userAvatar.index import get_avatar
from pythonflet.src.components.navigation_bar.nav_bar import show_menu_bar


def index_view(_):
    page = global_state.get_state_by_key('page')
    page.title = "Лікарі"
    user_ava = get_avatar()
    title = Text("ЛІКАРІ", font_family="Merriweather", size=40, weight=FontWeight.W_600)
    title.text_align = ft.TextAlign.CENTER

    header = ft.Row(
        [
            Container(
                content=title,
                bgcolor=colors.BLUE_GREY_50,
                padding=padding.only(left=20),
                border=ft.border.all(1, ft.colors.GREY),
                height=60,
                width=1200,
            ),
            Container(
                content=user_ava,
                padding=padding.only(right=10, top=10),
                height=60,
                width=60,
            ),
        ],
        width=1310,
    )

    find_doctor_field_by_name = TextField(label="Пошук по списку: введіть ПІБ лікаря",
                                          width=500,
                                          height=70,
                                          input_filter=ft.InputFilter(allow=True,
                                                                      regex_string=r"[а-яА-ЯіІЇї]",
                                                                      replacement_string=""),
                                          max_length=55)

    find_doctor_field_by_specialty = TextField(label="Пошук по списку: введіть спеціальність лікаря",
                                               width=400,
                                               height=70,
                                               input_filter=ft.InputFilter(allow=True,
                                                                           regex_string=r"[а-яА-ЯіІЇї]",
                                                                           replacement_string=""),
                                               max_length=55)

    def delete_doc(record_id):
        db = sqlite3.connect("clinic.db")
        cursor = db.cursor()
        cursor.execute(
        """
            DELETE FROM docs
            WHERE id=?
        """, (int(record_id),))
        db.commit()
        db.close()
        body.clean()
        display_docs()
        main_body.update()

    def display_all(_):
        find_doctor_field_by_name.value = ""
        find_doctor_field_by_specialty.value = ""
        navigation.update()
        body.clean()
        display_docs()
        body.update()

    def display_docs():
        db = sqlite3.connect("clinic.db")
        c = db.cursor()
        c.execute("SELECT * FROM docs")
        docs = c.fetchall()

        doctors = []
        for doc in docs:
            id_val, name_val, surname_val, middle_name_val, full_name, place_val, specialty_val, schedule_val = doc

            doctor = Doc(id_val,
                         name_val,
                         surname_val,
                         middle_name_val,
                         full_name,
                         place_val,
                         specialty_val,
                         schedule_val)

            doctors.append(doctor)

        for doc in doctors:
            id_val = doc.get_id()
            new_name = Text(value=doc.get_name(), size=18, font_family="TimesNewRoman")
            new_surname = Text(value=doc.get_surname(), size=18, font_family="TimesNewRoman")
            new_middle_name = Text(value=doc.get_middle_name(), size=18, font_family="TimesNewRoman")
            new_place = Text(value=doc.get_place(), size=16, font_family="TimesNewRoman")
            new_specialty = Text(value=doc.get_specialty(), size=16, font_family="TimesNewRoman")

            timetable = ""
            table = doc.get_schedule().split(".")
            for line in table:
                timetable += line + "\n"

            new_schedule = Text(value=timetable, size=16, font_family="TimesNewRoman")
            current_image = f"./assets/img/docs_img/person.png"

            def navigate_to_add_new_rec(id: id_val):
                page.go("/add_pnt", data={'doctor_id': id})

            add_record_this_doctor_btn = ft.ElevatedButton(text="Записатись",
                                                           width=140,
                                                           on_click=lambda _: navigate_to_add_new_rec(doc.get_id))

            delete_doc_btn = ft.IconButton(
                icon=ft.icons.DELETE_FOREVER_ROUNDED,
                icon_size=40,
                icon_color="pink600",
                tooltip="Видалити лікаря",
                on_click=lambda e, record_id=id_val: delete_doc(record_id), data=id_val
            )

            new_doctor_content = Row(
                [
                    Container(
                        content=Image(
                            src=current_image,
                            width=150,
                            height=150,
                        ),
                        height=165,
                        padding=ft.padding.only(left=10, top=10, bottom=10, right=20),
                        bgcolor=colors.GREY_200,
                        alignment=ft.alignment.center,
                        margin=ft.margin.only(left=30),
                    ),
                    Container(
                        Column([
                            Container(
                                content=new_surname,
                                margin=ft.margin.only(top=3),
                            ),
                            Container(
                                content=new_name,
                            ),
                            Container(
                                content=new_middle_name,
                            ),
                            Container(
                                content=add_record_this_doctor_btn
                            )
                        ]),
                        width=230,
                        height=165,
                        bgcolor=colors.GREY_200,
                    ),
                    Container(
                        Column(
                            [
                                new_place,
                                delete_doc_btn,
                            ],
                            alignment=ft.alignment.center
                        ),
                        padding=padding.only(top=70),
                        bgcolor=colors.GREY_200,
                        height=165,
                        width=350,
                    ),
                    Container(
                        content=new_specialty,
                        padding=padding.only(top=70),
                        bgcolor=colors.GREY_200,
                        width=200,
                        height=165,
                    ),
                    Container(
                        Column(
                            [
                                new_schedule,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        padding=padding.only(left=70, right=10, top=25),
                        margin=ft.margin.only(right=20),
                        bgcolor=colors.GREY_200,
                        width=220,
                        height=165,
                    ),
                ],
                spacing=0,
            )

            body.controls.append(new_doctor_content)
        db.close()

    def find_doc(_):
        if not find_doctor_field_by_name.value and not find_doctor_field_by_specialty:
            return

        db = sqlite3.connect("clinic.db")
        try:
            c = db.cursor()
            body.controls.clear()

            if find_doctor_field_by_name.value and find_doctor_field_by_specialty.value:

                search_query_full_name = find_doctor_field_by_name.value
                search_query_specialty = find_doctor_field_by_specialty.value

                if search_query_full_name and search_query_specialty:
                    query = """
                              SELECT *
                              FROM docs
                              WHERE specialty LIKE ? 
                              AND full_name LIKE ?
                            """
                    c.execute(query, ('%' + search_query_specialty + '%', '%' + search_query_full_name + '%'))
                    docs = c.fetchall()
                    print(docs)

                    doctors = []
                    for doc in docs:
                        id_val, name_val, surname_val, middle_name_val,\
                            full_name, place_val, specialty_val, schedule_val = doc

                        doctor = Doc(id_val, name_val, surname_val, middle_name_val, full_name, place_val,
                                     specialty_val,
                                     schedule_val)
                        doctors.append(doctor)

                    for doc in doctors:
                        id_val = doc.get_id()
                        new_name = Text(value=doc.get_name(), size=18, font_family="TimesNewRoman")
                        new_surname = Text(value=doc.get_surname(), size=18, font_family="TimesNewRoman")
                        new_middle_name = Text(value=doc.get_middle_name(), size=18, font_family="TimesNewRoman")
                        new_place = Text(value=doc.get_place(), size=16, font_family="TimesNewRoman")
                        new_specialty = Text(value=doc.get_specialty(), size=16, font_family="TimesNewRoman")

                        timetable = ""
                        table = doc.get_schedule().split(".")
                        for line in table:
                            timetable += line + "\n"

                        new_schedule = Text(value=timetable, size=16, font_family="TimesNewRoman")

                        current_image = f"./assets/img/docs_img/person.png"

                        def navigate_to_add_new_rec(id: id_val):
                            page.go("/add_pnt", data={'doctor_id': id})

                        add_record_this_doctor_btn = ft.ElevatedButton(text="Записатись",
                                                                       width=140,
                                                                       on_click=lambda _: navigate_to_add_new_rec(
                                                                           doc.get_id))

                        delete_doc_btn = ft.IconButton(
                            icon=ft.icons.DELETE_FOREVER_ROUNDED,
                            icon_color="pink600",
                            icon_size=40,
                            tooltip="Видалити лікаря",
                            on_click=lambda record_id=id_val: delete_doc(record_id), data=id_val
                        )

                        new_doctor_content = Row(
                            [
                                Container(
                                    content=Image(
                                        src=current_image,
                                        width=150,
                                        height=150,
                                    ),
                                    padding=ft.padding.only(left=10, top=10, bottom=10, right=20),
                                    margin=ft.margin.only(left=30),
                                    alignment=ft.alignment.center,
                                    bgcolor=colors.GREY_200,
                                    height=165,
                                ),
                                Container(
                                    Column([
                                        Container(
                                            content=new_surname,
                                            margin=ft.margin.only(top=3),
                                        ),
                                        Container(
                                            content=new_name,
                                        ),
                                        Container(
                                            content=new_middle_name,
                                        ),
                                        Container(
                                            content=add_record_this_doctor_btn
                                        )
                                    ]),
                                    bgcolor=colors.GREY_200,
                                    width=230,
                                    height=165,
                                ),
                                Container(
                                    Column(
                                        [
                                            new_place,
                                            delete_doc_btn,
                                        ],
                                        alignment=ft.alignment.center,
                                    ),
                                    padding=padding.only(top=70),
                                    bgcolor=colors.GREY_200,
                                    height=165,
                                    width=350,
                                ),
                                Container(
                                    content=new_specialty,
                                    padding=padding.only(top=70),
                                    bgcolor=colors.GREY_200,
                                    width=200,
                                    height=165,
                                ),
                                Container(
                                    Column(
                                        [
                                            new_schedule,
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    padding=padding.only(left=70, right=25),
                                    margin=ft.margin.only(right=20),
                                    bgcolor=colors.GREY_200,
                                    width=220,
                                    height=165,
                                ),
                            ],
                            spacing=0,
                        )
                        body.controls.append(new_doctor_content)

            elif find_doctor_field_by_name.value and not find_doctor_field_by_specialty.value:
                search_query = find_doctor_field_by_name.value
                if search_query:
                    query = """
                      SELECT *
                      FROM docs
                      WHERE full_name LIKE ?
                    """
                    c.execute(query, ('%' + search_query + '%',))
                    docs = c.fetchall()

                    doctors = []
                    for doc in docs:

                        id_val, name_val, surname_val, middle_name_val,\
                        full_name, place_val, specialty_val, schedule_val = doc

                        doctor = Doc(id_val, name_val, surname_val, middle_name_val, full_name,
                                     place_val, specialty_val, schedule_val)

                        doctors.append(doctor)

                    for doc in doctors:
                        id_val = doc.get_id()
                        new_name = Text(value=doc.get_name(), size=18, font_family="TimesNewRoman")
                        new_surname = Text(value=doc.get_surname(), size=18, font_family="TimesNewRoman")
                        new_middle_name = Text(value=doc.get_middle_name(), size=18, font_family="TimesNewRoman")
                        new_place = Text(value=doc.get_place(), size=16, font_family="TimesNewRoman")
                        new_specialty = Text(value=doc.get_specialty(), size=16, font_family="TimesNewRoman")

                        timetable = ""
                        table = doc.get_schedule().split(".")
                        for line in table:
                            timetable += line + "\n"

                        new_schedule = Text(value=timetable, size=16, font_family="TimesNewRoman")

                        current_image = f"./assets/img/docs_img/person.png"

                        def navigate_to_add_new_rec(id: id_val):
                            page.go("/add_pnt", data={'doctor_id': id})

                        add_record_this_doctor_btn = ft.ElevatedButton(text="Записатись",
                                                                       width=140,
                                                                       on_click=lambda _: navigate_to_add_new_rec(
                                                                           doc.get_id))

                        delete_doc_btn = ft.IconButton(
                            icon=ft.icons.DELETE_FOREVER_ROUNDED,
                            icon_size=40,
                            icon_color="pink600",
                            tooltip="Видалити лікаря",
                            on_click=lambda record_id=id_val: delete_doc(record_id), data=id_val
                        )

                        new_doctor_content = Row(
                            [
                                Container(
                                    content=Image(
                                        src=current_image,
                                        width=150,
                                        height=150,
                                    ),
                                    height=165,
                                    padding=ft.padding.only(left=10, top=10, bottom=10, right=20),
                                    bgcolor=colors.GREY_200,
                                    alignment=ft.alignment.center,
                                    margin=ft.margin.only(left=30),
                                ),
                                Container(
                                    Column([
                                        Container(
                                            content=new_surname,
                                            margin=ft.margin.only(top=3),
                                        ),
                                        Container(
                                            content=new_name,
                                        ),
                                        Container(
                                            content=new_middle_name,
                                        ),
                                        Container(
                                            content=add_record_this_doctor_btn,
                                        )
                                    ]),
                                    width=230,
                                    bgcolor=colors.GREY_200,
                                    height=165,
                                ),
                                Container(
                                    Column(
                                        [
                                            new_place,
                                            delete_doc_btn,
                                        ],
                                        alignment=ft.alignment.center,
                                    ),
                                    padding=padding.only(top=70),
                                    bgcolor=colors.GREY_200,
                                    height=165,
                                    width=350,
                                ),
                                Container(
                                    new_specialty,
                                    padding=padding.only(top=70),
                                    width=200,
                                    height=165,
                                    bgcolor=colors.GREY_200,
                                ),
                                Container(
                                    Column(
                                        [
                                            new_schedule,
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    margin=ft.margin.only(right=20),
                                    width=220,
                                    height=165,
                                    bgcolor=colors.GREY_200,
                                    padding=padding.only(left=70, right=25),
                                ),
                            ],
                            spacing=0,
                        )

                        body.controls.append(new_doctor_content)

            elif not find_doctor_field_by_name.value and find_doctor_field_by_specialty.value:
                search_query = find_doctor_field_by_specialty.value
                print(search_query)
                if search_query:
                    query = """
                          SELECT *
                          FROM docs
                          WHERE specialty LIKE ?
                        """
                    c.execute(query, ('%' + search_query + '%',))
                    docs = c.fetchall()

                    doctors = []
                    for doc in docs:
                        id_val, name_val, surname_val, middle_name_val,\
                            full_name, place_val, specialty_val, schedule_val = doc

                        doctor = Doc(id_val, name_val, surname_val, middle_name_val, full_name, place_val,
                                     specialty_val,
                                     schedule_val)
                        doctors.append(doctor)

                    for doc in doctors:
                        id_val = doc.get_id()
                        new_name = Text(value=doc.get_name(), size=18, font_family="TimesNewRoman")
                        new_surname = Text(value=doc.get_surname(), size=18, font_family="TimesNewRoman")
                        new_middle_name = Text(value=doc.get_middle_name(), size=18, font_family="TimesNewRoman")
                        new_place = Text(value=doc.get_place(), size=16, font_family="TimesNewRoman")
                        new_specialty = Text(value=doc.get_specialty(), size=16, font_family="TimesNewRoman")

                        timetable = ""
                        table = doc.get_schedule().split(".")
                        for line in table:
                            timetable += line + "\n"

                        new_schedule = Text(value=timetable, size=16, font_family="TimesNewRoman")

                        current_image = f"./assets/img/docs_img/person.png"

                        def navigate_to_add_new_rec(id: id_val):
                            page.go("/add_pnt", data={'doctor_id': id})

                        add_record_this_doctor_btn = ft.ElevatedButton(text="Записатись",
                                                                       width=140,
                                                                       on_click=lambda _: navigate_to_add_new_rec(
                                                                           doc.get_id))

                        delete_doc_btn = ft.IconButton(
                            icon=ft.icons.DELETE_FOREVER_ROUNDED,
                            icon_size=40,
                            icon_color="pink600",
                            tooltip="Видалити лікаря",
                            on_click=lambda record_id=id_val: delete_doc(record_id), data=id_val
                        )

                        new_doctor_content = Row(
                            [
                                Container(
                                    Image(
                                        src=current_image,
                                        width=150,
                                        height=150,
                                    ),
                                    height=165,
                                    bgcolor=colors.GREY_200,
                                    alignment=ft.alignment.center,
                                    margin=ft.margin.only(left=30),
                                    padding=ft.padding.only(left=10, top=10, bottom=10, right=20),
                                ),
                                Container(
                                    Column([
                                        Container(
                                            content=new_surname,
                                            margin=ft.margin.only(top=3),
                                        ),
                                        Container(
                                            content=new_name,
                                        ),
                                        Container(
                                            content=new_middle_name,
                                        ),
                                        Container(
                                            content=add_record_this_doctor_btn,
                                        )
                                    ]),
                                    bgcolor=colors.GREY_200,
                                    width=230,
                                    height=165,
                                ),
                                Container(
                                    Column(
                                        [
                                            new_place,
                                            delete_doc_btn,
                                        ],
                                        alignment=ft.alignment.center,
                                    ),
                                    padding=padding.only(top=70),
                                    bgcolor=colors.GREY_200,
                                    height=165,
                                    width=350,
                                ),
                                Container(
                                    content=new_specialty,
                                    bgcolor=colors.GREY_200,
                                    padding=padding.only(top=70),
                                    width=200,
                                    height=165,
                                ),
                                Container(
                                    Column(
                                        [
                                            new_schedule,
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=colors.GREY_200,
                                    margin=ft.margin.only(right=20),
                                    padding=padding.only(left=70, right=10, top=25),
                                    width=220,
                                    height=165,
                                ),
                            ],
                            spacing=0,
                        )

                        body.controls.append(new_doctor_content)

        except Exception as e:
            print(e)
        finally:
            if len(body.controls) == 0:
                page.snack_bar = ft.SnackBar(ft.Text('Записів нема!', size=22))
                page.snack_bar.open = True
            db.close()
            page.update()

    find_doc_btn = TextButton("Знайти",
                              width=110,
                              on_click=find_doc)

    body = Column(
        spacing=10,
        height=500,
        width=1250,
        adaptive=True,
        scroll=ft.ScrollMode.ALWAYS,
    )

    display_docs()

    display_all_docs_btn = OutlinedButton(text="Показати\n     всіх",
                                          on_click=display_all)

    def navigate_to_add_new_doc(_):
        page.go("/add_doc")

    add_doc_btn = ft.IconButton(
        icon=ft.icons.PERSON_ADD,
        icon_color="blue700",
        icon_size=40,
        tooltip="Додати нового лікаря",
        on_click=navigate_to_add_new_doc
    )

    navigation = Row(
        [
            Container(content=find_doctor_field_by_name),
            Container(content=find_doctor_field_by_specialty,
                      margin=ft.margin.only(left=10)),
            Container(content=find_doc_btn,
                      width=110),
            Container(content=display_all_docs_btn,
                      width=120),
            Container(content=add_doc_btn),
        ],
    )

    main_body = Row(
        [
            Column(
                [
                    show_menu_bar(page),
                    header,
                    navigation,
                    Container(body, border=ft.border.all(1)),
                ]
            ),
        ],
        height=1500,
        width=2560,
    )

    return main_body
