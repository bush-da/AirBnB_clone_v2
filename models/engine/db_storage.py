#!/usr/bin/python3
""" Defination of DBStorage """
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage():
    """ Description of a database engine with
    Attributes:
       __engine: SQLAlchemy engine
       __session: SQLAlchemy session
    """

    __engine = None
    __session = None

    def __init__(self):
        """ initilize a new DBStorage instance """

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)


        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query on the current database session of all objects

        depending on the given class if cls is None

        queries all types of objects

        Return:
              Dictionary of classes formated <classname>.<obj.id> = obj
        """
        objects = []
        if (cls is None):
            objects = self.__session.query(State).all()
            objects.extend(self.__session.query(User).all())
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(Place).all())
            objects.extend(self.__session.query(Amenity).all())
            objects.extend(self.__session.query(Review).all())
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            objects = self.__session.query(cls).all()

        return {"{}.{}".format(type(o).__name__, o.id): o for o in objects}


    def new(self, obj):
        """Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database sesson """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None """
        self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database and

        Create the current database session from the engine by using sessionmaker """

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
