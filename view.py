import PySimpleGUI as Sg
from controller import get_flights, get_plane_list, save_to_docx, authorization


def main_window():
    flights = []
    is_authorized = False
    Sg.theme("DarkAmber")

    search = [[Sg.Text('Номер літака'), Sg.OptionMenu(get_plane_list())],
              [Sg.Text('Кількість льотних годин'), Sg.InputText('')],
              [Sg.Button('Вибрати')],
              ]

    table = [
        Sg.Table(
            headings=['Номер літака', 'Кількість льотних годин', 'Номер рейсу'],
            values=[
                []
            ], key='-table-'
        )
    ]

    col1 = [[Sg.Button("Зберегти в файл")],
            [Sg.Frame('Пошук рейсів',
                      layout=[
                          [Sg.Column(search, element_justification='c')]
                      ]
                      )
             ]
            ]

    col2 = [[Sg.Button('Рейси', visible=False)]]

    col3 = [
        [Sg.Button('Пошук рейсів')],
        table,

    ]

    col4 = [[Sg.Button('Авторизація')]]

    layout = [[
        Sg.Column(
            col1,
            vertical_alignment='t',
            element_justification='c'
        ),
        Sg.Column(
            col2,
            vertical_alignment='t',
            element_justification='c'
        ),
        Sg.Column(
            col3,
            vertical_alignment='t',
            element_justification='c'
        ),
        Sg.Column(
            col4,
            vertical_alignment='t',
            element_justification='c'
        )
    ]]

    window = Sg.Window("title", layout)

    while True:
        event, values = window.read()
        if event == Sg.WINDOW_CLOSED or event == "Cancel":
            break
        elif event == "Вибрати":
            flights = get_flights(values[0], values[1])
            window.Element('-table-').update(flights)
        elif event == "Зберегти в файл":
            save_to_docx(flights)
        elif event == "Авторизація":
            is_authorized = authorization()
            if is_authorized:
                pass

        print('you entered ', values[0], ' ', values[1])


main_window()
