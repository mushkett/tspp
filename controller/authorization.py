import PySimpleGUI as Sg


def authorization():
    is_authorized = False
    log = 'admin'
    passw = 'admin'

    login = Sg.popup_get_text("Input login", "Authorization")
    password = Sg.popup_get_text("Input password", "Authorization", password_char='*')
    if log == login and passw == password:
        is_authorized = True
        Sg.popup("You are authorized now!", title="Success!")
    else:
        Sg.Popup("Incorrect login or password", title="Error")
    return is_authorized
