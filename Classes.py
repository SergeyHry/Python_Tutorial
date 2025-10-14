import datetime


class keys ():
    def __init__(self, name, key):
        self.name = name
        self.__key = key
        self.__date = datetime.datetime.now()
    def __str__(self):
        return  "Webseite: " + self.name + "\nKey: " + str(self.__key) + "\nErstellt am: " + str(self.__date.strftime("%d.%m.%Y"))
    def __repr__(self):
        return self.__str__()
    def get_key(self):
        return self.__key
    def set_key(self, key):
        self.__key = key
    def __len__(self):
        return len(self.__key)
#-----------------------------------------------------------------------------

class keysRecover(keys):
    def __init__(self, name, key):
        super(). __init__(name, key)
    def __str__(self):
        super(). __str__()
        return "für die Wiederherstellung von Passwort " + self.name + "bitte geben erste 3 Zeichen von Ihren Passwort: " + "***" + str(self.get_key()[3:])
keysi = keys("Youtube", "awdfg124 ")
keydi = keysRecover("Youtube", keysi.get_key())

print(keysi)
print(len(keysi))
print()
print(keydi)
# Prüffe welches Type ist und ob es um ein Objekt oder typ handelt

print(isinstance(keysi, keysRecover)) # Objekt aus Elternklasse ist kein Objekt von kindklasse
print(isinstance(keydi, keys)) # Objekt aus Kindklasse ist ein Objekt von Elternklasse
beaf = None
print(type(beaf)) # class None ^^ 