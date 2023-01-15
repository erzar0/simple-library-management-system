from sqlalchemy import create_engine, text
from .db_settings import postgresql as settings
from abc import ABC, abstractmethod

def get_pg_connection_string(settings):
    pguser = settings["pguser"]
    pgpasswd = settings["pgpasswd"]
    pghost = settings["pghost"]
    pgport = settings["pgport"]
    pgdb = settings["pgdb"]
    return f"postgresql://{pguser}:{pgpasswd}@{pghost}:{pgport}/{pgdb}"

class BaseModel(ABC):
    def __init__(self, tableName):
        self.connectionString = get_pg_connection_string(settings)
        self.engine = create_engine(self.connectionString, pool_size=100, echo=False) 
        self.schema = "library"
        self.tableName = tableName 
    
    def getAll(self):
        with self.engine.connect() as conn:
            return conn.execute(text(f"select * from {self.schema}.{self.tableName}"))
    
    def getById(self, id):
        with self.engine.connect() as conn:
            result = conn.execute(text(f"select * from {self.schema}.{self.tableName} where id = :id"), {"id": id})
            return result 
    
    @abstractmethod
    def add(self, recordData):
        pass
    

