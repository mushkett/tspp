from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert

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
                Column('plain_number', String(6), nullable=False),
                Column("hours", Integer(), nullable=False),
                Column('route_number', String(25), nullable=False)
                )


def create_table():
    metadata.drop_all(engine)
    metadata.create_all(engine)


def insert_value():
    conn.execute(insert(rozklad), [
        {  # 1
            "plain_number": 'КА-123',
            "hours": 25,
            "route_number": "M-22"
        },
        {  # 2
            "plain_number": 'КЛ-307',
            "hours": 13,
            "route_number": "M-12"
        },
        {  # 3
            "plain_number": 'КП-003',
            "hours": 16,
            "route_number": "M-34"
        },
        {  # 4
            "plain_number": 'КВ-834',
            "hours": 8,
            "route_number": "M-11"
        },
        {  # 5
            "plain_number": 'КМ-608',
            "hours": 12,
            "route_number": "M-540"
        },
        {  # 6
            "plain_number": 'КБ-716',
            "hours": 17,
            "route_number": "M-111"
        },
        {  # 7
            "plain_number": 'КА-199',
            "hours": 14,
            "route_number": "M-215"
        },
        {  # 8
            "plain_number": 'КМ-602',
            "hours": 24,
            "route_number": "M-16"
        },
        {  # 9
            "plain_number": 'КЛ-352',
            "hours": 11,
            "route_number": "M-144"
        },
        {  # 10
            "plain_number": 'КМ-607',
            "hours": 20,
            "route_number": "M-121"
        },
        {  # 11
            "plain_number": 'КМ-523',
            "hours": 15,
            "route_number": "M-100"
        },
        {
            "plain_number": 'КБ-709',
            "hours": 13,
            "route_number": "M-81"
        },
    ])


create_table()
insert_value()
