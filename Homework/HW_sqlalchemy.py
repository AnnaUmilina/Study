from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = 'homework.db'
engine = create_engine(f'sqlite:///{DATABASE_NAME}')
session = sessionmaker(bind=engine)
Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)
