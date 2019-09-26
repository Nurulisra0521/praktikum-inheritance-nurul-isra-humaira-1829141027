class Bakso(object):
    def __init__(self, rasa, bentuk):
        self.rasa = rasa
        self.bentuk = bentuk

    def besar(self):
        print("bakso besar")

    def enak(self):
        print("digemari banyakk orang")


# class Anak turunan dari class Bakso
class Baksokeju(Bakso):
    def __init__(self, rasa, bentuk, isi):
        self.rasa = rasa
        self.bentuk = bentuk
        self.isi = isi

    def besar(self):
        print("bakso kecil")

    def enak(self):
        print("digemari banyak orang")
    pass


a = Bakso("gurih", "bulat")
print()
print("rasa:", a.rasa)
print("bentuk:", a.bentuk)
a.besar()
a.enak()

# objek dari class baksokeju memiliki seluruh yang dimiliki class bakso
b = Baksokeju("asin manis", "kotak", "keju")
print()
print("anak turunan dari bakso")
print("rasa:", b.rasa)
print("bentuk:", b.bentuk)
print("isi:", b.isi)

b.besar()
b.enak()
