
class Contact(object):
    def __init__(self, first_name, last_name, phone_number, email, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.birth_year = birth_year
        self.age = 2016 - int(self.birth_year)

    def izpisi_kontakt(self):
        return self.last_name + ", " + self.first_name + ", " + str(self.phone_number) + ", " + self.email + ", " + str(self.birth_year) + ", " + str(self.age) 

moji_kontakti = []

while True:
    odgovor = raw_input("Ali zelis koncati? ")
    if odgovor == "da":
                        break
    ime = raw_input("ime ")
    priimek = raw_input("priimek ")
    phone = raw_input("telefon ")
    email = raw_input("email ")
    year = raw_input("leto rojstva ")

    kontakt = Contact(ime, priimek, phone, email, year)

    moji_kontakti.append(kontakt)
        
for kontakt in moji_kontakti:
        print(kontakt.izpisi_kontakt())
