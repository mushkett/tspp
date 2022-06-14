from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_session():
    host = "ec2-54-165-178-178.compute-1.amazonaws.com"
    db = "dbvhl0gmdq014r"
    user = "glygllyaluruqa"
    port = "5432"
    password = "dd27e4dc8a6c33f7842bfea2c025ebf2536b93d235c9239e13ffe23cca3e439b"

    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


