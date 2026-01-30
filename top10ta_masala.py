
##1-Masala:
# class Transport:
#     def __init__(self,model:str,yil:int):
#         self.model = model
#         self.yil = yil
#
#     def malumot(self)-> str:
#         return f"Model: {self.model} Yil: {self.yil}"
#
# class Avtomobil(Transport):
#     def __init__(self, model: str , yil:int, yonilgi_turi: str):
#         super().__init__(model,yil)
#         self.yonilgi_turi = yonilgi_turi
#
#     def malumot(self):
#         baza = super().malumot()
#         return f"{baza} , Yonilg'i:{self.yonilgi_turi}"
#
# class Avtobus(Transport):
#     def __init__(self, model: str , yil:int,orinlar_soni: str ):
#         super().__init__(model,yil)
#         self.orinlar_soni = orinlar_soni
#     def malumot(self):
#         baza = super().malumot()
#         return f"{baza} , O'rindiqlar soni:{self.orinlar_soni}"
#
# a = Avtomobil("Cobalt",2022,"benzin")
# print(a.malumot())
#
# b = Avtomobil("Isuzu",2018,"40")
# print(b.malumot())
#

##2-masala:
# class Kitob:
#     def __init__(self, nom,muallif,yil):
#         self.nom = nom
#         self.muallif = muallif
#         self.yil = yil
#
#     def taqdimot(self):
#         return f"Kitob nomi:{self.nom},Kitob muallifi:{self.muallif},Yili: {self.yil}"
#
# class ElektronKitob(Kitob):
#     def __init__(self, nom,muallif,yil,fayl_hajmi_mb):
#         super().__init__(nom,muallif,yil)
#         self.fayl_hajmi_mb = fayl_hajmi_mb
#
#     def taqdimot(self):
#         baza = super().taqdimot()
#         return f"{baza}, [Elektron :{self.fayl_hajmi_mb}]"
#
# class AudioKitob(Kitob):
#     def __init__(self, nom,muallif,yil,davomiylik_soat):
#         super().__init__(nom, muallif, yil)
#         self.davomiylik_soat = davomiylik_soat
#
#     def taqdimot(self):
#         baza = super().taqdimot()
#         return f"{baza}, [Audio :{self.davomiylik_soat} soat]"
#
# e = ElektronKitob("Python asoslari", "Ali", 2023, 5)
# print(e.taqdimot())
#
# a = AudioKitob("O'tkan kunlar", "Abdulla Qodiriy", 2020, 12)
# print(a.taqdimot())

##3-Masala:
# class Xodim:
#     def __init__(self, ism,asosiy_maosh):
#         self.ism = ism
#         self.asosiy_maosh = asosiy_maosh
#
#     def oylik(self):
#         return self.asosiy_maosh
#
#     def malumot(self):
#         return f"Ism:{self.ism},Oylik:{self.oylik()}"
#
# class Oqsoch(Xodim):
#     def __init__(self, ism,asosiy_maosh,bonus_foiz):
#         super().__init__(ism,asosiy_maosh)
#         self.bonus_foiz = bonus_foiz
#
#     def oylik(self):
#         bonus = self.asosiy_maosh * self.bonus_foiz // 100
#         return f"{bonus},Bonus_foizi:{self.bonus_foiz}"
#
# class SoatbayXodim(Xodim):
#     def __init__(self, ism,soat,soatlik_stavka):
#         super().__init__(ism,soat * soatlik_stavka)
#         self.soat = soat
#         self.soatlik_stavka = soatlik_stavka
#
# o = Oqsoch("Dilshod", 5_000_000, 20)
# print(o.malumot())
#
# s = SoatbayXodim("Aziza", soat=160, soatlik_stavka=50_000)
# print(s.malumot())

##4-Masala:
# class Mahsulot:
#     def __init__(self, nom, narx):
#         self.nom = nom
#         self.narx = narx
#
#     def chegirmali_narx(self, foiz):
#         chegirma = self.narx * foiz / 100
#         return int(self.narx - chegirma)
#
#
# class Elektronika(Mahsulot):
#     def __init__(self, nom, narx, kafolat_oy):
#         super().__init__(nom, narx)
#         self.kafolat_oy = kafolat_oy
#
#     def malumot(self):
#         return f"Nom: {self.nom}, Narx: {self.narx}, Kafolat: {self.kafolat_oy} oy"
#
#
# class OziqOvqat(Mahsulot):
#     def __init__(self, nom, narx, yaroqlilik_kuni):
#         super().__init__(nom, narx)
#         self.yaroqlilik_kuni = yaroqlilik_kuni
#
#     def malumot(self):
#         return f"Nom: {self.nom}, Narx: {self.narx}, Yaroqlilik: {self.yaroqlilik_kuni}"
#
# telefon = Elektronika("iPhone 15", 15_000_000, 24)
# non = OziqOvqat("Non", 4_000, "2026-12-31")
#
# print(telefon.malumot())
# print("Chegirmali narx:", telefon.chegirmali_narx(10))
#
# print(non.malumot())
# print("Chegirmali narx:", non.chegirmali_narx(5))
#

##5-Masala:
# class Shaxs:
#     def __init__(self,ism):
#         self.ism = ism
#
# class Talaba(Shaxs):
#     def __init__(self,ism,id_raqam):
#         super().__init__(ism)
#         self.id_raqam = id_raqam
#
# class ImtihonNatijasi(Talaba):
#     def __init__(self,ism,id_raqam,baholar):
#         super().__init__(ism,id_raqam)
#         self.baholar = baholar
#
#     def ortalama(self):
#         if not self.baholar:
#             return 0
#         return sum(self.baholar) / len(self.baholar)
#
#     def status(self):
#         a = self.ortalama()
#         if a >= 86:
#             return "A'lo "
#         elif 71 <= a < 85:
#             return "Yaxshi "
#         elif 56 <= a < 70:
#             return "Qoniqarli "
#         else:
#             return "Qoniqarsiz"
#
# natija = ImtihonNatijasi("Ali", "T001", [90, 80, 100])
# print(f"Ism:{natija.ism}")  # Ali
# print(f"Id_raqamingiz:{natija.id_raqam}")  # T001
# print(f"Ballingiz:{natija.ortalama()}")  #90.0
# print(f"Sizning statusingiz:{natija.status()}") # A'lo

##6-Masala:


















