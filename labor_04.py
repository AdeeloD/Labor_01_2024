import labor_04_modul
from labor_04_modul import adatok_bekerese ,muveletek_vegrehajtasa,eredmenyek_megejelenitese

jel, szam1, szam2 = labor_04_modul.adatok_bekerese()
eredmeny = labor_04_modul.muveletek_vegrehajtasa(jel, szam1, szam2)
eredmenyek=labor_04_modul.eredmenyek_megejelenitese(eredmeny)
