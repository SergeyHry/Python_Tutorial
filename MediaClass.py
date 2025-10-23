#1. Eltern Class erstellen titel, erscheinungsjahr, verfügbar methoden ausleihen(), zurückgeben, info()
#2. Under Class für vererbung und Methode überschreiben Buch Film Zeitschrift
#3.

class Media():
    def __init__(self, title, erscheinungsjahr, verfügbar):
        self.title = title
        self.erscheinungsjahr = erscheinungsjahr
        self.verfügbar = verfügbar
    def ausleihen(self):
        if not self.verfügbar:
            print("dieser Artikel ist nicht vorhanden")
        else:
            print("sie haben sich "+ self.title + " ausgeliehen")
            self.verfügbar =  False

    def info(self):
        if self.verfügbar==True:
            return "der Artikel:  " + self.title + " erscheinungsjahr: " + self.erscheinungsjahr
        else:
            return "der Artikel:  " + self.title + " ausgeliehen"
    def zurückgeben(self):
        if self.verfügbar == False:
            print("der Artikel ist zurükgegeben")
            self.verfügbar = True




class Buch(Media):
    def __init__(self, autor, title, erscheinungsjahr,seitenzahl, verfügbar):
        super().__init__(title, erscheinungsjahr, verfügbar)
        self.autor = autor
        self.seitenzahl = seitenzahl

    def ausleihen(self):
        return super().ausleihen()
    def zurückgeben(self):
        return super().zurückgeben()
    def info(self):

        print("Title: " + self.title + " Autor: " + self.autor + " Erscheinungsjar: " + self.erscheinungsjahr)

class Film(Media):
    def __init__(self, title, regisseur, dauer, ganre, erscheinungsjahr, verfügbar):
        super().__init__(title, erscheinungsjahr, verfügbar)
        self.regisseur = regisseur
        self.dauer = dauer
        self.ganre = ganre
    def info(self):
        print("Title: " + self.title + " Regisior: " + self.regisseur + " Erscheinungsjar: " + self.erscheinungsjahr + "Genre: " +self.ganre + "Duaer: " + self.dauer)
buchi = Buch("Autoridze", "Malkom der Vampir", "1994", "354", True)
buchi.ausleihen()
buchi.info()
buchi.zurückgeben()
buchi.info()

filmi =  Film("Funny Story", "Stiven Sigal", "150.49", "Comedy", "2021", True)
filmi.info()

media = Media("Olga Sweethart", "Lambada",  False)
media.ausleihen()