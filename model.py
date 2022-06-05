from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Time, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

host = "ec2-54-165-178-178.compute-1.amazonaws.com"
db = "dbvhl0gmdq014r"
user = "glygllyaluruqa"
port = "5432"
password = "dd27e4dc8a6c33f7842bfea2c025ebf2536b93d235c9239e13ffe23cca3e439b"

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}/{db}")
conn = engine.connect()

metadata = MetaData()
rozklad = Table("rozklad", metadata,
                Column('id', Integer(), primary_key=True, nullable=False),
                Column('number', String(6), nullable=False),
                Column("city", String(25), nullable=False),
                Column('depature_time', Time(), nullable=False),
                Column('free_seats', Integer(), nullable=False),
                )


def create_table():
    metadata.drop_all(engine)
    metadata.create_all(engine)


def insert_value():
    conn.execute(insert(rozklad), [
        {  # 1
            "number": 'КА-123',
            "city": "Київ",
            "depature_time": "21:25:00",
            "free_seats": 80
        },
        {  # 2
            "number": 'КЛ-307',
            "city": "Лондон",
            "depature_time": "06:15:00",
            "free_seats": 72
        },
        {  # 3
            "number": 'КП-003',
            "city": "Париж",
            "depature_time": "08:10:00",
            "free_seats": 48
        },
        {  # 4
            "number": 'КВ-834',
            "city": "Відень",
            "depature_time": "13:40:00",
            "free_seats": 45
        },
        {  # 5
            "number": 'КМ-608',
            "city": "Мюнхен",
            "depature_time": "15:30:00",
            "free_seats": 2
        },
        {  # 6
            "number": 'КБ-716',
            "city": "Берлін",
            "depature_time": "17:05:00",
            "free_seats": 23
        },
        {  # 7
            "number": 'КА-199',
            "city": "Київ",
            "depature_time": "00:55:00",
            "free_seats": 6
        },
        {  # 8
            "number": 'КМ-602',
            "city": "Мюнхен",
            "depature_time": "07:35:00",
            "free_seats": 32
        },
        {  # 9
            "number": 'КЛ-352',
            "city": "Лондон",
            "depature_time": "19:00:00",
            "free_seats": 4
        },
        {  # 10
            "number": 'КМ-607',
            "city": "Мюнхен",
            "depature_time": "22:10:00",
            "free_seats": 0
        },
        {  # 11
            "number": 'КМ-523',
            "city": "Мадрид",
            "depature_time": "21:20:00",
            "free_seats": 13
        }, {
            "number": 'КБ-709',
            "city": "Берлін",
            "depature_time": "07:05:00",
            "free_seats": 0
        },
    ])


class Flight(declarative_base()):

    __tablename__ = "rozklad"

    id = Column(Integer, primary_key=True)
    number = Column(String)
    city = Column(String)
    depature_time = Column(Time)
    free_seats = Column(Integer)


Session = sessionmaker(bind=engine)
session = Session()
for i in session.query(Flight).all():
    print(i.__dict__)
