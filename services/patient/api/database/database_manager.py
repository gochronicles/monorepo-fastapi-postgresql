from api import config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, create_engine, DDL, event
from contextlib import contextmanager
from api.utils import logger

logging = logger(__name__)


class DatabaseManager:
    __instance = None

    def __setup_schema(self):
        event.listen(
            self.Base.metadata,
            "before_create",
            DDL("CREATE SCHEMA IF NOT EXISTS patient_schema"),
        )

    @staticmethod
    def sharedInstance():
        """ Static access method. """
        if DatabaseManager.__instance is None:
            DatabaseManager()
        return DatabaseManager.__instance

    def __init__(self):
        """Virtually private constructor. """
        if DatabaseManager.__instance is not None:
            try:
                raise Exception("Instance exists!")
            except Exception as e:
                logging.debug(e)
        else:
            self.db_url = config.get("database").get("POSTGRES_URI")
            logging.debug(f"Database Url: {self.db_url}")

            self.metadata = MetaData(schema="patient_schema")
            self.engine = create_engine(self.db_url, pool_pre_ping=True)
            self.Base = declarative_base(metadata=self.metadata)
            self.SessionMaker = sessionmaker(bind=self.engine)
            self.__setup_schema()
            DatabaseManager.__instance = self
