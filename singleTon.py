from abc import ABCMeta, abstractmethod
from sqlalchemy import create_engine
import pandas as pd


#1. Abstracte Classe erstellen mit info() methode
#2. konrete unter Klasse erstellen
#3. Instance erstellen
#4. statische Methode get_instance() (prüft ob die Instanz ==None)
#5. __init__
#6. info methode überschreiben
#7 testen
class Databank(metaclass=ABCMeta):
    @abstractmethod
    def engineCreate(self):
        pass

class MariaDB(Databank):
    __instance = None
    @staticmethod
    def get_instance():
        if MariaDB.__get_instance == None:
            MariaDB(db, "user", "pass", "host", 3307, "databank")
        else:
            return MariaDB.__instance
    def __init__(self, user, password, host,port,database):
        if MariaDB.__instance != None:
            raise Exception("die Verbindung ist shon gestellt")
        else:
            self.user = user
            self.password = password
            self.host = host
            self.port = port
            self.database = database
            MariaDB.__instance = self


    def engineCreate(self):
        engine = create_engine(f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}")
        df = pd.read_sql("SELECT * FROM baby_names LIMIT 10", engine)
        print(df.head())

db = MariaDB( "root", "1111", "localhost",3307, "bookstore")
db.engineCreate()
newDb = MariaDB( "root", "2222", "localhost",3306, "filter")
newDb.engineCreate() #Fehler Meldung Verbindung shon Erstellt
