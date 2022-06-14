import PySimpleGUI as Sg
from controller import get_flights, get_plane_list, save_to_docx, authorization, add_flight


def main_window():
    is_authorized = False
    flights = get_flights('', '')
    plane_list = get_plane_list()
    plane_list.append('')

    is_adding = True
    Sg.theme("DarkAmber")

    search = [[Sg.Text('Номер літака'), Sg.OptionMenu(plane_list)],
              [Sg.Text('Кількість льотних годин'), Sg.InputText('')],
              [Sg.Button('Вибрати')],
              ]

    table_admin = [
        Sg.Table(
            headings=['id', 'Номер літака', 'Кількість льотних годин', 'Номер рейсу'],
            values=flights,
            key='-table_admin-',
            enable_click_events=True,
            enable_events=True,
            select_mode=Sg.TABLE_SELECT_MODE_BROWSE
        )
    ]

    table_user = [
        Sg.Table(
            headings=['id', 'Номер літака', 'Кількість льотних годин', 'Номер рейсу'],
            values=flights,
            key='-table-user'
        )
    ]

    col1_user = [[Sg.Button("Зберегти в файл")],
                 [Sg.Frame('Пошук рейсів',
                           layout=[
                               [Sg.Column(search, element_justification='c')]
                           ]
                           )
                  ]
                 ]

    col2_user = [[Sg.Button('Пошук рейсів')]]

    col3_user = [[Sg.Button('Авторизація')],
                 table_user]

    col1_admin = [
        [Sg.Button("Зберегти в файл")],
        table_admin
    ]

    col2_admin = [
        [Sg.Button("Рейси")],
        [Sg.Button('+', disabled=True, key='+')],
        [Sg.Button('/', disabled=False, key='/')]
    ]

    col3_admin = [
        [Sg.Button('Вийти')],
        [Sg.Frame('Рейс', layout=[
            [Sg.Text('ID'), Sg.InputText('', disabled=True, key='-id-')],
            [Sg.Text('Номер літака'), Sg.InputText('', key='-plane-')],
            [Sg.Text('Кількість льотних годин'), Sg.InputText('', key='-hours-')],
            [Sg.Text('Номер маршруту'), Sg.InputText('', key='-route-')],
            [Sg.Button('Зберегти')],
        ])
         ]
    ]

    layout = [[
        Sg.Column(
            col1_user,
            key="-COL-1-USER",
            vertical_alignment='t',
            element_justification='left'
        ),
        Sg.Column(
            col1_admin,
            key="-COL-1-ADMIN",
            vertical_alignment='t',
            element_justification='left',
            visible=False
        ),
        Sg.Column(
            col2_user,
            key="-COL-2-USER",
            vertical_alignment='t',
            element_justification='c'
        ),
        Sg.Column(
            col2_admin,
            key="-COL-2-ADMIN",
            vertical_alignment='t',
            element_justification='left',
            visible=False
        ),
        Sg.Column(
            col3_user,
            key="-COL-3-USER",
            vertical_alignment='t',
            element_justification='right',
        ),
        Sg.Column(
            col3_admin,
            vertical_alignment='t',
            element_justification='right',
            key="-COL-3-ADMIN",
            visible=False
        )
    ]]

    window = Sg.Window("title", layout)

    while True:
        event, values = window.read()
        if event == Sg.WINDOW_CLOSED or event == "Cancel":
            break

        elif event == "Вибрати":
            flights = get_flights(values[0], values[1])
            window.Element('-table-user').update(flights)

        elif event == "Зберегти в файл":
            save_to_docx(flights)

        elif event == "Авторизація":
            is_authorized = authorization()
            if is_authorized:
                window.Element('-COL-1-USER').update(visible=False)
                window.Element('-COL-2-USER').update(visible=False)
                window.Element('-COL-3-USER').update(visible=False)

                window.Element('-COL-1-ADMIN').update(visible=True)
                window.Element('-COL-2-ADMIN').update(visible=True)
                window.Element('-COL-3-ADMIN').update(visible=True)

        elif event == 'Вийти':
            is_authorized = False
            window.Element('-COL-1-USER').update(visible=True)
            window.Element('-COL-2-USER').update(visible=True)
            window.Element('-COL-3-USER').update(visible=True)

            window.Element('-COL-1-ADMIN').update(visible=False)
            window.Element('-COL-2-ADMIN').update(visible=False)
            window.Element('-COL-3-ADMIN').update(visible=False)

        elif event == '-table_admin-':
            try:
                data_selected = [flights[row] for row in values[event]][0]
            except IndexError:
                continue
            if not is_adding:
                print(data_selected)
                window.Element('-id-').update(data_selected[0])
            window.Element('-plane-').update(data_selected[1])
            window.Element('-hours-').update(data_selected[2])
            window.Element('-route-').update(data_selected[3])

        elif event == "/":
            window.Element('-id-').update(disabled=False)
            window.Element('+').update(disabled=False)
            window.Element('/').update(disabled=True)
            is_adding = False

        elif event == "+":
            window.Element('-id-').update('', disabled=True)
            window.Element('+').update(disabled=True)
            window.Element('/').update(disabled=False)
            is_adding = True

        elif event == 'Зберегти':
            add_flight(values['-id-'], values['-plane-'], values['-hours-'], values['-route-'])

            flights = get_flights('', '')
            window.Element('-table_admin-').update(flights)


main_window()
