from sqlalchemy.exc import DataError
import PySimpleGUI as Sg
from controller.create_session import create_session
from model import Flight


def get_flights(plane_number, hours):
    session = create_session()
    result = []
    try:
        if hours and plane_number:

            result = session.query(Flight)\
                .filter(Flight.hours < int(hours))\
                .filter(Flight.plain_number == plane_number)\
                .order_by(Flight.id)\
                .all()

        elif hours:
            result = session.query(Flight)\
                .filter(Flight.hours >= int(hours)) \
                .order_by(Flight.id)\
                .all()
        elif plane_number:
            result = session.query(Flight)\
                .filter(Flight.plain_number == plane_number) \
                .order_by(Flight.id) \
                .all()
        else:
            result = session.query(Flight).order_by(Flight.id).all()

    except DataError:
        session.rollback()
        Sg.Popup('Виникла помилка! Перевірте правильність введених даних!', title="Error")
    else:
        if result:
            list_of_flights = []

            for i in result:
                temp_list = []
                i_dict = i.__dict__
                temp_list.append(i_dict['id'])
                temp_list.append(i_dict['plain_number'])
                temp_list.append(i_dict['hours'])
                temp_list.append(i_dict['route_number'])
                list_of_flights.append(temp_list)
            session.close()
            return list_of_flights
        else:
            Sg.Popup('Нічого не знайдено!', title='Error')


def get_plane_list():
    session = create_session()
    result = sorted(set([i[0] for i in session.query(Flight.plain_number).all()]))
    return result


def add_flight(flight_id, plain_number, hours, route_number):
    session = create_session()
    if flight_id:
        flight = session.query(Flight).filter(Flight.id == int(flight_id))
        record = flight.one()
        record.plain_number = plain_number
        record.hours = int(hours)
        record.route_number = route_number
        Sg.Popup('Рейс успішно оновлено', title='Success')

    else:
        new_flight = Flight(
            plain_number=plain_number,
            hours=hours,
            route_number=route_number
        )
        session.add(new_flight)
        Sg.Popup('Рейс успішно додано', title='Success')

    session.commit()
