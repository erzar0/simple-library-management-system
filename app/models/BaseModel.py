from .db_settings import postgresql as settings

def get_pg_connection_string(settings):
    pguser = settings["pguser"]
    pgpasswd = settings["pgpasswd"]
    pghost = settings["pghost"]
    pgport = settings["pgport"]
    pgdb = settings["pgdb"]
    return f"postgresql://{pguser}:{pgpasswd}@{pghost}:{pgport}/{pgdb}"

class BaseModel():
    def __init__(self):
        self.connStr = get_pg_connection_string(settings)
    

    

