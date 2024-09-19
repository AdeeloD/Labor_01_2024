#Netto jövedelemszámítás bruttóból
print("Jövedelemszámítás")

brutto=int(input("Mennyi a bruttó jövedelme:"))
kor=int(input("Hány éves vagy?"))

if kor<25:
    if brutto> 599790:
        szja=(brutto*599790)*0.15
    else:
        szja=0
else:
    szja= brutto*0.15
nyugdij=brutto*0.1
tb=brutto*0.07
munkanelkuli=brutto*0.015
netto=brutto-szja-nyugdij-munkanelkuli
print("Jövedelem".center(50))
print("\nBruttó jövedelem:".ljust(25, "_"), str(int(brutto)).rjust(25, "_"),"Ft",sep="")
print("\nSZJA:".ljust(25, "_"), str(szja).rjust(25, "_"),"Ft",sep="")
print("\nNyugdíj:".ljust(25, "_"), str(nyugdij).rjust(25, "_"),"Ft",sep="")
print("\nTB Járulék:".ljust(25, "_"), str(nyugdij).rjust(25, "_"),"Ft",sep="")
print("\nMunkanélküli::".ljust(25, "_"), str(munkanelkuli).rjust(25, "_"),"Ft",sep="")
print("\nNetto Jövedelem:".ljust(25, "_"), str(netto).rjust(25, "_"),"Ft",sep="")