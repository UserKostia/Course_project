import os
import random
import sqlite3
import datetime
import flet as ft

from datetime import datetime, timedelta
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
    TextButton,
    FontWeight,
    DatePicker,
    CircleAvatar,
    ElevatedButton)


def doc_records_view(page: Page):
    page.title = "Записи"
    page.window_maximizable = True
    page.window_resizable = True
    faker = Faker()

    avatar = CircleAvatar(
        foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
        content=Text("FF"),
    )

    title = Text("Записи до лікарів", font_family="Merriweather", size=40, weight=FontWeight.W_600)
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

    find_record_field = TextField(label="Пошук по списку: введіть ПІБ лікаря",
                                  width=800,
                                  height=45)

    scroll_left_date_btn = ElevatedButton(text="<", height=35)

    date_picker = DatePicker(on_change=change_date,
                             on_dismiss=date_picker_dismissed,
                             first_date=datetime(2023, 10, 1),
                             last_date=datetime(2024, 10, 1),)

    scroll_right_date_btn = ElevatedButton(text=">", height=35)
    # page.overlay.append(date_picker)

    def pick_date(self):
        self.open = True
        self.update()

    date_button = ElevatedButton(
        "Pick date",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: date_picker.pick_date(),
    )

    def pr(e):
        print("Hello")

    record_btn = TextButton("Записатись", width=120, height=20, on_click=pr)
    navigation = Row(
        [
        Container(content=find_record_field),
        Container(content=record_btn),
        Container(content=scroll_left_date_btn),
        Container(content=date_button),
        Container(content=scroll_right_date_btn),
        ]
    )

    name = Text("name", size=18, font_family="TimesNewRoman")
    surname = Text("surname", size=18, font_family="TimesNewRoman")
    maddlename = Text("maddlename", size=18, font_family="TimesNewRoman")

    complaint = Text("complaint", size=16, font_family="TimesNewRoman")
    registration_date = Text("Дата та час", size=16, font_family="TimesNewRoman")
    record_content = Row(
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
                width=400,
                bgcolor=colors.GREY_200,
                height=150,
            ),
            Container(
                Column([complaint]),
                bgcolor=colors.GREY_200,
                height=150,
                width=400,
            ),
            Container(
                registration_date,
                margin=ft.margin.only(right=20),
                width=200,
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

    def fill_docs_records():
        db = sqlite3.connect("docs_records.db")
        c = db.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS patients(
            id INTEGER PRIMARY KEY,
            photo BLOB,
            name VARCHAR(30),
            surname VARCHAR(40),
            middle_name VARCHAR(30),
            diagnos VARCHAR,
            registration_date DATE
            )
            """
        )

        query = """
        INSERT INTO patients (photo, name, surname, middle_name, diagnos, registration_date)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        patients_names = [
            "Олександр",
            "Ірина",
            "Віктор",
            "Олена",
            "Сергій",
            "Наталія",
            "Іван",
            "Тетяна",
            "Василь",
            "Оксана",
            "Михайло",
            "Анна",
            "Петро",
            "Віра",
            "Євген",
            "Людмила",
            "Дмитро",
            "Лариса",
            "Андрій",
            "Світлана",
            "Ігор",
            "Ганна",
            "Олексій",
            "Лідія",
            "Володимир",
            "Оксана",
            "Станіслав",
            "Олександра",
            "Владислав",
            "Ірина",
            "Степан",
            "Ольга",
            "Максим",
            "Інна",
            "Роман",
            "Марія",
            "Микола",
            "Єлизавета",
            "Юрій",
            "Надія",
            "Валерій",
            "Софія",
            "Вікторія",
            "Віталій",
            "Яна",
            "Василь",
            "Євгенія",
            "Володимир",
            "Тамара",
            "Василь",
            "Лілія",
            "Лев",
            "Світлана",
            "Олексій",
            "Тетяна",
            "Валентин",
            "Ірина",
            "Олег",
            "Ангеліна",
            "Руслан",
            "Олена",
            "Віталіна",
            "Анатолій",
            "Любов",
            "Георгій",
            "Лілія",
            "Анатолій",
            "Галина",
            "Вадим",
            "Віра",
            "Євген",
            "Наталя",
            "Віктор",
            "Наташа",
            "Сергій",
            "Лілія",
            "Микола",
            "Ірина",
            "Олександр",
            "Ірина",
            "Максим",
            "Валентина",
            "Олексій",
            "Ірина",
            "Олександр",
            "Людмила",
            "Олег",
            "Надія",
            "Андрій",
            "Валерія",
            "Іван",
            "Любов",
            "Віктор",
            "Оксана",
            "Лев",
            "Світлана",
            "Ігор",
            "Тетяна",
            "Сергій",
            "Оксана"
        ]

        patients_surnames = [
            "Петров",
            "Іванов",
            "Сидоров",
            "Козлов",
            "Михайлов",
            "Сергієнко",
            "Лисенко",
            "Дмитрієв",
            "Кузьменко",
            "Яковенко",
            "Ткаченко",
            "Григорович",
            "Кравченко",
            "Левченко",
            "Шевченко",
            "Бондаренко",
            "Мельник",
            "Волков",
            "Федоренко",
            "Коваленко",
            "Павленко",
            "Семенов",
            "Мироненко",
            "Захаренко",
            "Тимошенко",
            "Ковальова",
            "Попов",
            "Іщенко",
            "Литвиненко",
            "Мазур",
            "Єрьоменко",
            "Романенко",
            "Полякова",
            "Чернова",
            "Соколова",
            "Котенко",
            "Комарова",
            "Гриценко",
            "Красніков",
            "Максимова",
            "Орлова",
            "Макаренко",
            "Даниленко",
            "Білоус",
            "Савченко",
            "Поляков",
            "Радченко",
            "Бєлова",
            "Щербаков",
            "Федорова",
            "Гаврилюк",
            "Кузьмін",
            "Лапін",
            "Миронюк",
            "Яремчук",
            "Дорошенко",
            "Гончаренко",
            "Шевельова",
            "Петренко",
            "Бондар",
            "Кравець",
            "Черненко",
            "Рибак",
            "Тарасенко",
            "Козак",
            "Ковальчук",
            "Степанова",
            "Харченко",
            "Білик",
            "Савін",
            "Кулікова",
            "Шаповалова",
            "Калініна",
            "Маслов",
            "Бобров",
            "Чередніченко",
            "Носова",
            "Кулаков",
            "Стороженко",
            "Глущенко",
            "Бондаренко",
            "Іванова",
            "Петрова",
            "Лисенко",
            "Сергієнко",
            "Дмитрієв",
            "Кузьміна",
            "Яковенко",
            "Ткаченко",
            "Григорович",
            "Кравченко",
            "Левченко",
            "Шевченко",
            "Бондаренко",
            "Мельник",
            "Волков",
            "Федоренко",
            "Коваленко",
            "Павленко",
            "Семенов"
        ]

        patients_middle_names = [
            "Олександрович",
            "Іванович",
            "Васильович",
            "Миколайович",
            "Сергійович",
            "Андрійович",
            "Дмитрович",
            "Якович",
            "Петрович",
            "Григорович",
            "Олексійович",
            "Степанович",
            "Павлович",
            "Володимирович",
            "Віталійович",
            "Максимович",
            "Олегович",
            "Анатолійович",
            "Георгійович",
            "Михайлович",
            "Юрійович",
            "Тарасович",
            "Ігорович",
            "Вікторович",
            "Романович",
            "Семенович",
            "Артемович",
            "Антонович",
            "Тимофійович",
            "Андріянович",
            "Владиславович",
            "Олексієвич",
            "Борисович",
            "Сергієвич",
            "Костянтинович",
            "Васильєвич",
            "Валентинович",
            "Валерійович",
            "Денисович",
            "Євгенович",
            "Данилович",
            "Вікторович",
            "Єгорович",
            "Ілліч",
            "Вадимович",
            "Миронович",
            "Савелійович",
            "Ігнатович",
            "Трохимович",
            "Арсенійович",
            "Федорович",
            "Богданович",
            "Русланович",
            "Андійович",
            "Вітольдович",
            "Леонідович",
            "Михеевич",
            "Олександрович",
            "Вітольдович",
            "Олегович",
            "Ростиславович",
            "Русланович",
            "Тарасович",
            "Олександрович",
            "Ярославович",
            "Євгенійович",
            "Григорійович",
            "Родіонович",
            "Артемівич",
            "Адамович",
            "Кирилович",
            "Богданович",
            "Вікторович",
            "Вікентійович",
            "Святославович",
            "Олексійович",
            "Миронович",
            "Олексійович",
            "Валентинович",
            "Ігорович",
            "Романович",
            "Артемівич",
            "Максимович",
            "Вадимович",
            "Володимирович",
            "Євгенійович",
            "Михайлович",
            "Ігнатьевич",
            "Володимирович",
            "Сергійович",
            "Максимович",
            "Олексійович",
            "Васильович",
            "Миколайович",
            "Сергійович",
            "Андрійович",
            "Олексійович",
            "Євгенійович",
            "Анатолійович",
            "Олександрович"
        ]

        diagnoses = [
            "гастрит", "перелом", "дерматит", "тромбоз", "астма",
            "грип", "артрит", "гіпертензія", "діабет", "мігрень",
            "гепатит", "інсульт", "кон'юнктивіт", "зубний біль", "ревматизм",
            "застуда", "бронхіт", "грижа", "депресія", "альцгеймер",
            "остеопороз", "рак", "ендометріоз", "панкреатит", "гломерулонефрит",
            "артроз", "катаракта", "пневмонія", "туберкульоз", "коронавірус",
            "шлункова виразка", "констрипація", "гіпергідроз", "анемія", "гонорея",
            "сифіліс", "герпес", "скарлатина", "варикоз", "бронхіальна астма",
            "глаукома", "деменція", "псоріаз", "панік-атака", "вірусний гепатит",
            "печінкова недостатність", "пневмоторакс", "емфізема", "остеоартрит", "кератит",
            "діарея", "гострий апендицит", "мієлома", "холера", "залізодефіцитна анемія",
            "таласемія", "варикозна хвороба", "лімфома", "лейкемія", "фіброз",
            "тендовагініт", "кон'юнктивіт", "кератокон'юнктивіт", "меланома", "акне",
            "гіпотиреоз", "гіпертиреоз", "коклюш", "тетанус", "дифтерія",
            "гістоплазмоз", "аскаридоз", "опісторхоз", "токсоплазмоз", "ботулізм",
            "вітіліго", "склеродермія", "псоріатичний артрит", "діабетична ретинопатія", "гліома",
            "міастенія", "невралгія", "хронічний бронхіт", "бронхіальна обструкція", "пневмоконіоз",
            "ларингіт", "ларинготрахеїт", "паротит", "хвороба Вільсона", "морбілі",
            "рубеола", "карієс", "гінгівіт", "періодонтит", "пухлини головного мозку",
            "тромбофлебіт", "емболія", "міокардит", "кардіоміопатія", "фіброміалгія",
            "гранульома", "саркоїдоз", "міастенічний синдром", "паркинсонізм", "геморой"
        ]

        start_date = datetime.now() - timedelta(days=730)  # Дата два роки тому
        end_date = datetime.now()  # Поточна дата

        def random_date(start, end):
            """
            Генерує рандомну дату в діапазоні між start та end
            """
            return start + timedelta(
                days=random.randint(0, int((end - start).days))
            )

        patients_data = [
            (
                faker.random_element(elements="./img/docs_img"),
                faker.random_element(elements=patients_names),
                faker.random_element(elements=patients_surnames),
                faker.random_element(elements=patients_middle_names),
                faker.random_element(elements=diagnoses),
                random_date(start_date, end_date).strftime('%Y-%m-%d %H:%M:%S')
        ) for _ in range(10)]

        c.executemany(query, patients_data)
        db.commit()

    fill_docs_records()

    image_files = [f for f in os.listdir('./img/docs_img/') if os.path.isfile(os.path.join('./img/docs_img/', f))]

    def display_docs_records():
        db = sqlite3.connect("docs_records.db")
        c = db.cursor()
        c.execute("SELECT name, surname, middle_name, diagnos, registration_date FROM patients")
        patient_rec = c.fetchall()
        for index, rec in enumerate(patient_rec):
            name_val, surname_val, middle_name_val, diagnos_val, registration_date_val = rec

            # Виберіть поточне зображення зі списку файлів
            current_image = f"./img/docs_img/{image_files[index % len(image_files)]}"

            # Створення нових контролів для кожного документа
            new_name = Text(value=name_val, size=18, font_family="TimesNewRoman")
            new_surname = Text(value=surname_val, size=18, font_family="TimesNewRoman")
            new_middle_name = Text(value=middle_name_val, size=18, font_family="TimesNewRoman")
            new_place = Text(value=diagnos_val, size=16, font_family="TimesNewRoman")
            new_specialty = Text(value=registration_date_val, size=16, font_family="TimesNewRoman")

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

    display_docs_records()

    return main_body
