from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import  declarative_base , sessionmaker
from sqlalchemy import create_engine

from models.foto import Foto

# ### ------------------------ public functions ------------------------ ###
db_url = 'sqlite:///unsplash.db'

engine = create_engine(
    db_url,
    logging_name='sqlite',
    pool_size=20,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=3600,
)
Base = declarative_base()

Foto.__table__.create(bind=engine, checkfirst=True)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




# ### ------------------------ internal functions ------------------------ ###




# ### ------------------------ test functions ------------------------ ###

def __test():
    raise NotImplementedError('Test not implemented')


if __name__ == '__main__':
    __test()