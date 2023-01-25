from .db_settings import postgresql as settings

def get_pg_connection_string(settings, elephant=False):
    pguser = settings["pguser"]
    pgpasswd = settings["pgpasswd"]
    pghost = settings["pghost"]
    pgport = settings["pgport"]
    pgdb = settings["pgdb"]
    if(elephant):
        return "postgres://isbeupgx:XVPRjDW95qhTEcziYal05_GgcvGZAws6@hattie.db.elephantsql.com/isbeupgx"
    return f"postgresql://{pguser}:{pgpasswd}@{pghost}:{pgport}/{pgdb}"

class BaseModel():
    def __init__(self):
        self.connStr = get_pg_connection_string(settings, elephant=True)
    

    

