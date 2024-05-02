import os
import sqlite3
import flet as ft
from faker import Faker
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
    TextButton,
    CircleAvatar,
    ElevatedButton)


def index_view(page: Page):
    page.title = "Лікарі"
    faker = Faker()

    avatar = CircleAvatar(
        foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
        content=Text("FF"),
    )

    title = Text("ЛІКАРІ", font_family="Merriweather", size=40, weight=FontWeight.W_600)
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
        width=1310
    )

    def find_doc(e):
        body.clean()
        db = sqlite3.connect("doctors.db")
        c = db.cursor()

        search_query = find_doctor_field.value
        if search_query:
            query = f"""
            SELECT name, surname, middle_name, place, specialty
            FROM docs
            WHERE name LIKE {search_query} OR surname LIKE {search_query} OR middle_name LIKE {search_query}
            """
            c.execute(query, ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%'))
            docs = c.fetchall()
            print(docs)
            # Очистка відображуваного списку лікарів
            body.clean()

            for doc in docs:
                name_val, surname_val, middle_name_val, place_val, specialty_val = doc

                # Виберіть поточне зображення зі списку файлів
                current_image = f"./img/docs_img/{image_files[docs.index(doc) % len(image_files)]}"

                # Створення нових контролів для кожного документа
                new_name = Text(value=name_val, size=18, font_family="TimesNewRoman")
                new_surname = Text(value=surname_val, size=18, font_family="TimesNewRoman")
                new_middle_name = Text(value=middle_name_val, size=18, font_family="TimesNewRoman")
                new_place = Text(value=place_val, size=16, font_family="TimesNewRoman")
                new_specialty = Text(value=specialty_val, size=16, font_family="TimesNewRoman")

                new_doctor_content = Row(
                    [
                        Container(
                            Image(
                                src=current_image,
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
                                    new_name,
                                    margin=ft.margin.only(top=20),
                                ),
                                Container(
                                    new_surname,
                                ),
                                Container(
                                    new_middle_name,
                                )
                            ]),
                            width=400,
                            bgcolor=colors.GREY_200,
                            height=150,
                        ),
                        Container(
                            Column([new_place]),
                            bgcolor=colors.GREY_200,
                            height=150,
                            width=400,
                        ),
                        Container(
                            new_specialty,
                            margin=ft.margin.only(right=20),
                            width=200,
                            height=150,
                            bgcolor=colors.GREY_200,
                        ),
                    ],
                    spacing=0
                )

                body.controls.append(new_doctor_content)

            db.close()
        print("World")

    find_doctor_field = TextField(label="Пошук по списку: введіть ПІБ лікаря",
                                  width=870,
                                  height=45,
                                  )

    find_doc_btn = TextButton("Знайти", width=110, on_click=find_doc)

    navigation = Row(
        [
            Container(content=find_doctor_field),

            Container(
                content=find_doc_btn,
                # margin=ft.margin.only(top=0, left=30),
                # padding=ft.padding.only(top=0)
            )
        ]
    )

    body = Column(
        spacing=10,
        height=500,
        width=1250,
        scroll=ft.ScrollMode.ALWAYS,
        adaptive=True
    )

    image_files = [f for f in os.listdir('./assets/img/docs_img/') if os.path.isfile(os.path.join('./assets/img/docs_img/', f))]

    def display_docs():
        db = sqlite3.connect("doctors.db")
        c = db.cursor()
        c.execute("SELECT name, surname, middle_name, place, specialty FROM docs")
        docs = c.fetchall()
        for index, doc in enumerate(docs):
            name_val, surname_val, middle_name_val, place_val, specialty_val = doc

            # Виберіть поточне зображення зі списку файлів
            current_image = f"./img/docs_img/{image_files[index % len(image_files)]}"

            # Створення нових контролів для кожного документа
            new_name = Text(value=name_val, size=18, font_family="TimesNewRoman")
            new_surname = Text(value=surname_val, size=18, font_family="TimesNewRoman")
            new_middle_name = Text(value=middle_name_val, size=18, font_family="TimesNewRoman")
            new_place = Text(value=place_val, size=16, font_family="TimesNewRoman")
            new_specialty = Text(value=specialty_val, size=16, font_family="TimesNewRoman")

            new_doctor_content = Row(
                [
                    Container(
                        Image(
                            src=current_image,
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
                                new_name,
                                margin=ft.margin.only(top=20),
                            ),
                            Container(
                                new_surname,
                            ),
                            Container(
                                new_middle_name,
                            )
                        ]),
                        width=400,
                        bgcolor=colors.GREY_200,
                        height=150,
                    ),
                    Container(
                        Column([new_place]),
                        bgcolor=colors.GREY_200,
                        height=150,
                        width=400,
                    ),
                    Container(
                        new_specialty,
                        margin=ft.margin.only(right=20),
                        width=200,
                        height=150,
                        bgcolor=colors.GREY_200,
                    ),
                ],
                spacing=0
            )

            body.controls.append(new_doctor_content)
        db.close()

    display_docs()

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

    # def fill_docs():
    #     db = sqlite3.connect("doctors.db")
    #     c = db.cursor()
    #     c.execute(
    #         """
    #         CREATE TABLE IF NOT EXISTS docs(
    #         id INTEGER PRIMARY KEY,
    #         photo BLOB,
    #         name VARCHAR(30),
    #         surname VARCHAR(40),
    #         middle_name VARCHAR(30),
    #         place VARCHAR,
    #         specialty VARCHAR
    #         )
    #         """
    #     )
    #
    #     query = """
    #     INSERT INTO docs (photo, name, surname, middle_name, place, specialty)
    #     VALUES (?, ?, ?, ?, ?, ?)
    #     """
    #
    #     docs_names = [
    #         "Олександр",
    #         "Ірина",
    #         "Віктор",
    #         "Олена",
    #         "Сергій",
    #         "Наталія",
    #         "Іван",
    #         "Тетяна",
    #         "Василь",
    #         "Оксана",
    #         "Михайло",
    #         "Анна",
    #         "Петро",
    #         "Віра",
    #         "Євген",
    #         "Людмила",
    #         "Дмитро",
    #         "Лариса",
    #         "Андрій",
    #         "Світлана",
    #         "Ігор",
    #         "Ганна",
    #         "Олексій",
    #         "Лідія",
    #         "Володимир",
    #         "Оксана",
    #         "Станіслав",
    #         "Олександра",
    #         "Владислав",
    #         "Ірина",
    #         "Степан",
    #         "Ольга",
    #         "Максим",
    #         "Інна",
    #         "Роман",
    #         "Марія",
    #         "Микола",
    #         "Єлизавета",
    #         "Юрій",
    #         "Надія",
    #         "Валерій",
    #         "Софія",
    #         "Вікторія",
    #         "Віталій",
    #         "Яна",
    #         "Василь",
    #         "Євгенія",
    #         "Володимир",
    #         "Тамара",
    #         "Василь",
    #         "Лілія",
    #         "Лев",
    #         "Світлана",
    #         "Олексій",
    #         "Тетяна",
    #         "Валентин",
    #         "Ірина",
    #         "Олег",
    #         "Ангеліна",
    #         "Руслан",
    #         "Олена",
    #         "Віталіна",
    #         "Анатолій",
    #         "Любов",
    #         "Георгій",
    #         "Лілія",
    #         "Анатолій",
    #         "Галина",
    #         "Вадим",
    #         "Віра",
    #         "Євген",
    #         "Наталя",
    #         "Віктор",
    #         "Наташа",
    #         "Сергій",
    #         "Лілія",
    #         "Микола",
    #         "Ірина",
    #         "Олександр",
    #         "Ірина",
    #         "Максим",
    #         "Валентина",
    #         "Олексій",
    #         "Ірина",
    #         "Олександр",
    #         "Людмила",
    #         "Олег",
    #         "Надія",
    #         "Андрій",
    #         "Валерія",
    #         "Іван",
    #         "Любов",
    #         "Віктор",
    #         "Оксана",
    #         "Лев",
    #         "Світлана",
    #         "Ігор",
    #         "Тетяна",
    #         "Сергій",
    #         "Оксана"
    #     ]
    #
    #     docs_surnames = [
    #         "Петров",
    #         "Іванов",
    #         "Сидоров",
    #         "Козлов",
    #         "Михайлов",
    #         "Сергієнко",
    #         "Лисенко",
    #         "Дмитрієв",
    #         "Кузьменко",
    #         "Яковенко",
    #         "Ткаченко",
    #         "Григорович",
    #         "Кравченко",
    #         "Левченко",
    #         "Шевченко",
    #         "Бондаренко",
    #         "Мельник",
    #         "Волков",
    #         "Федоренко",
    #         "Коваленко",
    #         "Павленко",
    #         "Семенов",
    #         "Мироненко",
    #         "Захаренко",
    #         "Тимошенко",
    #         "Ковальова",
    #         "Попов",
    #         "Іщенко",
    #         "Литвиненко",
    #         "Мазур",
    #         "Єрьоменко",
    #         "Романенко",
    #         "Полякова",
    #         "Чернова",
    #         "Соколова",
    #         "Котенко",
    #         "Комарова",
    #         "Гриценко",
    #         "Красніков",
    #         "Максимова",
    #         "Орлова",
    #         "Макаренко",
    #         "Даниленко",
    #         "Білоус",
    #         "Савченко",
    #         "Поляков",
    #         "Радченко",
    #         "Бєлова",
    #         "Щербаков",
    #         "Федорова",
    #         "Гаврилюк",
    #         "Кузьмін",
    #         "Лапін",
    #         "Миронюк",
    #         "Яремчук",
    #         "Дорошенко",
    #         "Гончаренко",
    #         "Шевельова",
    #         "Петренко",
    #         "Бондар",
    #         "Кравець",
    #         "Черненко",
    #         "Рибак",
    #         "Тарасенко",
    #         "Козак",
    #         "Ковальчук",
    #         "Степанова",
    #         "Харченко",
    #         "Білик",
    #         "Савін",
    #         "Кулікова",
    #         "Шаповалова",
    #         "Калініна",
    #         "Маслов",
    #         "Бобров",
    #         "Чередніченко",
    #         "Носова",
    #         "Кулаков",
    #         "Стороженко",
    #         "Глущенко",
    #         "Бондаренко",
    #         "Іванова",
    #         "Петрова",
    #         "Лисенко",
    #         "Сергієнко",
    #         "Дмитрієв",
    #         "Кузьміна",
    #         "Яковенко",
    #         "Ткаченко",
    #         "Григорович",
    #         "Кравченко",
    #         "Левченко",
    #         "Шевченко",
    #         "Бондаренко",
    #         "Мельник",
    #         "Волков",
    #         "Федоренко",
    #         "Коваленко",
    #         "Павленко",
    #         "Семенов"
    #     ]
    #
    #     docs_middle_names = [
    #         "Олександрович",
    #         "Іванович",
    #         "Васильович",
    #         "Миколайович",
    #         "Сергійович",
    #         "Андрійович",
    #         "Дмитрович",
    #         "Якович",
    #         "Петрович",
    #         "Григорович",
    #         "Олексійович",
    #         "Степанович",
    #         "Павлович",
    #         "Володимирович",
    #         "Віталійович",
    #         "Максимович",
    #         "Олегович",
    #         "Анатолійович",
    #         "Георгійович",
    #         "Михайлович",
    #         "Юрійович",
    #         "Тарасович",
    #         "Ігорович",
    #         "Вікторович",
    #         "Романович",
    #         "Семенович",
    #         "Артемович",
    #         "Антонович",
    #         "Тимофійович",
    #         "Андріянович",
    #         "Владиславович",
    #         "Олексієвич",
    #         "Борисович",
    #         "Сергієвич",
    #         "Костянтинович",
    #         "Васильєвич",
    #         "Валентинович",
    #         "Валерійович",
    #         "Денисович",
    #         "Євгенович",
    #         "Данилович",
    #         "Вікторович",
    #         "Єгорович",
    #         "Ілліч",
    #         "Вадимович",
    #         "Миронович",
    #         "Савелійович",
    #         "Ігнатович",
    #         "Трохимович",
    #         "Арсенійович",
    #         "Федорович",
    #         "Богданович",
    #         "Русланович",
    #         "Андійович",
    #         "Вітольдович",
    #         "Леонідович",
    #         "Михеевич",
    #         "Олександрович",
    #         "Вітольдович",
    #         "Олегович",
    #         "Ростиславович",
    #         "Русланович",
    #         "Тарасович",
    #         "Олександрович",
    #         "Ярославович",
    #         "Євгенійович",
    #         "Григорійович",
    #         "Родіонович",
    #         "Артемівич",
    #         "Адамович",
    #         "Кирилович",
    #         "Богданович",
    #         "Вікторович",
    #         "Вікентійович",
    #         "Святославович",
    #         "Олексійович",
    #         "Миронович",
    #         "Олексійович",
    #         "Валентинович",
    #         "Ігорович",
    #         "Романович",
    #         "Артемівич",
    #         "Максимович",
    #         "Вадимович",
    #         "Володимирович",
    #         "Євгенійович",
    #         "Михайлович",
    #         "Ігнатьевич",
    #         "Володимирович",
    #         "Сергійович",
    #         "Максимович",
    #         "Олексійович",
    #         "Васильович",
    #         "Миколайович",
    #         "Сергійович",
    #         "Андрійович",
    #         "Олексійович",
    #         "Євгенійович",
    #         "Анатолійович",
    #         "Олександрович"
    #     ]
    #
    #     docs_places = [
    #         "1 корпус, 2 поверх, 10 кабінет",
    #         "2 корпус, 3 поверх, 18 кабінет",
    #         "3 корпус, 1 поверх, 22 кабінет",
    #         "4 корпус, 4 поверх, 5 кабінет",
    #         "5 корпус, 2 поверх, 15 кабінет",
    #         "1 корпус, 3 поверх, 12 кабінет",
    #         "2 корпус, 1 поверх, 8 кабінет",
    #         "3 корпус, 4 поверх, 21 кабінет",
    #         "4 корпус, 2 поверх, 17 кабінет",
    #         "5 корпус, 3 поверх, 24 кабінет",
    #         "1 корпус, 1 поверх, 7 кабінет",
    #         "2 корпус, 4 поверх, 13 кабінет",
    #         "3 корпус, 2 поверх, 9 кабінет",
    #         "4 корпус, 3 поверх, 20 кабінет",
    #         "5 корпус, 1 поверх, 6 кабінет",
    #         "1 корпус, 4 поверх, 14 кабінет",
    #         "2 корпус, 2 поверх, 11 кабінет",
    #         "3 корпус, 3 поверх, 19 кабінет",
    #         "4 корпус, 1 поверх, 23 кабінет",
    #         "5 корпус, 5 поверх, 16 кабінет",
    #         "1 корпус, 2 поверх, 25 кабінет",
    #         "2 корпус, 3 поверх, 28 кабінет",
    #         "3 корпус, 1 поверх, 30 кабінет",
    #         "4 корпус, 4 поверх, 32 кабінет",
    #         "5 корпус, 2 поверх, 26 кабінет",
    #         "1 корпус, 3 поверх, 27 кабінет",
    #         "2 корпус, 1 поверх, 29 кабінет",
    #         "3 корпус, 4 поверх, 31 кабінет",
    #         "4 корпус, 2 поверх, 33 кабінет",
    #         "5 корпус, 3 поверх, 34 кабінет",
    #         "1 корпус, 1 поверх, 35 кабінет",
    #         "2 корпус, 4 поверх, 36 кабінет",
    #         "3 корпус, 2 поверх, 37 кабінет",
    #         "4 корпус, 3 поверх, 38 кабінет",
    #         "5 корпус, 1 поверх, 39 кабінет",
    #         "1 корпус, 4 поверх, 40 кабінет",
    #         "2 корпус, 2 поверх, 41 кабінет",
    #         "3 корпус, 3 поверх, 42 кабінет",
    #         "4 корпус, 1 поверх, 43 кабінет",
    #         "5 корпус, 5 поверх, 44 кабінет",
    #         "1 корпус, 2 поверх, 45 кабінет",
    #         "2 корпус, 3 поверх, 46 кабінет",
    #         "3 корпус, 1 поверх, 47 кабінет",
    #         "4 корпус, 4 поверх, 48 кабінет",
    #         "5 корпус, 2 поверх, 49 кабінет",
    #         "1 корпус, 3 поверх, 50 кабінет",
    #         "2 корпус, 1 поверх, 51 кабінет",
    #         "3 корпус, 4 поверх, 52 кабінет",
    #         "4 корпус, 2 поверх, 53 кабінет",
    #         "5 корпус, 3 поверх, 54 кабінет",
    #         "1 корпус, 1 поверх, 55 кабінет",
    #         "2 корпус, 4 поверх, 56 кабінет",
    #         "3 корпус, 2 поверх, 57 кабінет",
    #         "4 корпус, 3 поверх, 58 кабінет",
    #         "5 корпус, 1 поверх, 59 кабінет",
    #         "1 корпус, 4 поверх, 60 кабінет",
    #         "2 корпус, 2 поверх, 61 кабінет",
    #         "3 корпус, 3 поверх, 62 кабінет",
    #         "4 корпус, 1 поверх, 63 кабінет",
    #         "5 корпус, 5 поверх, 64 кабінет",
    #         "1 корпус, 2 поверх, 65 кабінет",
    #         "2 корпус, 3 поверх, 66 кабінет",
    #         "3 корпус, 1 поверх, 67 кабінет",
    #         "4 корпус, 4 поверх, 68 кабінет",
    #         "5 корпус, 2 поверх, 69 кабінет",
    #         "1 корпус, 3 поверх, 70 кабінет",
    #         "2 корпус, 1 поверх, 71 кабінет",
    #         "3 корпус, 4 поверх, 72 кабінет",
    #         "4 корпус, 2 поверх, 73 кабінет",
    #         "5 корпус, 3 поверх, 74 кабінет",
    #         "1 корпус, 1 поверх, 75 кабінет",
    #         "2 корпус, 4 поверх, 76 кабінет",
    #         "3 корпус, 2 поверх, 77 кабінет",
    #         "4 корпус, 3 поверх, 78 кабінет",
    #         "5 корпус, 1 поверх, 79 кабінет",
    #         "1 корпус, 4 поверх, 80 кабінет",
    #         "2 корпус, 2 поверх, 81 кабінет",
    #         "3 корпус, 3 поверх, 82 кабінет",
    #         "4 корпус, 1 поверх, 83 кабінет",
    #         "5 корпус, 5 поверх, 84 кабінет",
    #         "1 корпус, 2 поверх, 85 кабінет",
    #         "2 корпус, 3 поверх, 86 кабінет",
    #         "3 корпус, 1 поверх, 87 кабінет",
    #         "4 корпус, 4 поверх, 88 кабінет",
    #         "5 корпус, 2 поверх, 89 кабінет",
    #         "1 корпус, 3 поверх, 90 кабінет",
    #         "2 корпус, 1 поверх, 91 кабінет",
    #         "3 корпус, 4 поверх, 92 кабінет",
    #         "4 корпус, 2 поверх, 93 кабінет",
    #         "5 корпус, 3 поверх, 94 кабінет",
    #         "1 корпус, 1 поверх, 95 кабінет",
    #         "2 корпус, 4 поверх, 96 кабінет",
    #         "3 корпус, 2 поверх, 97 кабінет",
    #         "4 корпус, 3 поверх, 98 кабінет",
    #         "5 корпус, 1 поверх, 99 кабінет",
    #         "1 корпус, 4 поверх, 100 кабінет",
    #         "2 корпус, 2 поверх, 101 кабінет",
    #         "3 корпус, 3 поверх, 102 кабінет",
    #         "4 корпус, 1 поверх, 103 кабінет",
    #         "5 корпус, 5 поверх, 104 кабінет"
    #     ]
    #
    #     docs_specialty = [
    #         "Терапевт", "Кардіолог", "Невролог", "Ортопед", "Гастроентеролог", "Дерматолог", "Офтальмолог",
    #         "Акушер-гінеколог", "Уролог", "Педіатр", "Хірург", "Онколог", "Ендокринолог", "Пульмонолог", "Ревматолог",
    #         "Неонатолог", "ЛОР-лікар", "Нефролог", "Кардіохірург", "Нейрохірург", "Пластичний хірург", "Трансплантолог",
    #         "Гематолог", "Алерголог-імунолог", "Радіолог", "Торакальний хірург", "Вірусолог", "Фтизіатр",
    #         "Гінеколог-онколог", "Ендоскопіст", "Гепатолог", "Дієтолог", "Фізіотерапевт", "Масажист", "Косметолог",
    #         "Ортодонт", "Стоматолог", "Пародонтолог", "Протезувальник", "Імплантолог", "Ортопед-травматолог",
    #         "Ортопед-дентист", "Дитячий стоматолог", "Лікар з лікування біль", "Психіатр", "Психотерапевт", "Нарколог",
    #         "Геріатр", "Лікар з паліативної допомоги", "Гігієніст"
    #     ]
    #
    #     docs_data = [(faker.random_element(elements="./img/docs_img"),
    #                   faker.random_element(elements=docs_names),
    #                   faker.random_element(elements=docs_surnames),
    #                   faker.random_element(elements=docs_middle_names),
    #                   faker.random_element(elements=docs_places),
    #                   faker.random_element(elements=docs_specialty),
    #                   faker.random_int(min=1, max=10)) for _ in range(500)]
    #
    #     c.executemany(query, docs_data)
    #     db.commit()
