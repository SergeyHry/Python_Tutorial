from sqlalchemy import create_engine
import pandas as pd

# Verbindung aufbauen (anpassen!)
user = "root"
password = "****"
host = "localhost"
port = 3307
database = "bookstore"

# SQLAlchemy-Engine erzeugen
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

# Daten auslesen
df = pd.read_sql("SELECT * FROM baby_names", engine)

# Als CSV speichern
df.to_csv(r"C:\Users\Student\Desktop\export.csv", index=False, sep=";")

print("Export erfolgreich!")

