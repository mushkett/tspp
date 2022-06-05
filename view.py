import PySimpleGUI as Sg


def main_window():
    Sg.theme("DarkAmber")
    search = [[Sg.Text('Місто'), Sg.OptionMenu(['Київ', 'Суми', 'Париж'])],
              [Sg.InputText('ХХ годин')],
              [Sg.Button('Вибрати')],
              [Sg.Button('Зберегти')], ]

    table = [
        Sg.Table(
            headings=['Номер рейсу', 'Пункт призначення', 'Кількість льотних годин', 'Номер маршруту'],
            values=[
                ['1', '2', '3', '4']
            ]
        )
    ]

    col1 = [[Sg.Button("Файл")],
            [Sg.Frame('Пошук рейсів',
                      layout=[
                          [Sg.Column(search, element_justification='c')]
                      ]
                      )
             ]
            ]

    col2 = [[Sg.Button('Рейси')]]

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
        print('you entered ', values[0], ' ', values[1])


main_window()
