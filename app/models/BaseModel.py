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
            return conn.execute(text(f"select * from {self.schema}.{self.tableName}")).all()
    
    def findById(self, id: int):
        with self.engine.connect() as conn:
            result = conn.execute(text(f"select * from {self.schema}.{self.tableName} where id = :id"), {"id": id})
            return result.one_or_none() 

    def findStrict(self, filters: dict):
        with self.engine.connect() as conn:
            sql = f"select * from {self.schema}.{self.tableName} where"
            for k in filters.keys():
                sql += f" {k} = :{k} and "
            sql += "1=1"

            return conn.execute(text(sql), filters).all()

    def findLike(self, filters: dict, matchCase: bool = False):
        with self.engine.connect() as conn:
            i = "" if matchCase else "i"
            sql = f"select * from {self.schema}.{self.tableName} where"
            for k in filters.keys():
                sql += f" cast({k} as text) {i}like :{k} and "
            sql += "1=1"

            filters = { k: f"%{v}%" for k,v in filters.items()}
            return conn.execute(text(sql), filters).all()
    
    @abstractmethod
    def add(self, recordData):
        pass
    

