from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Database import Base

# ----------------------------------------------------------
#  DATABASE SETUP
#  SQLite database
# ----------------------------------------------------------
def Database(directory_database, load=False):
    try:
        engine = create_engine(directory_database)

        # delete database, reload data
        if load:
            Base.metadata.drop_all(engine)

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)

        return Session
    
    except:
        print("SQLITE DATABASE FILE NOT FOUND: {}".format(directory_database))
