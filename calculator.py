#Számológép
from Tools.scripts.make_ctype import values

print("Számológép".center(50))
operator=input("Kérek egy műveleti jelet:{*,+,/-}")
if operator not in("+","-","*","/"):
    exit()
a=float(input("a="))
b=float(input("b="))
if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    if b != 0:
        result = a / b
    else:
        print("Hiba: Nullával való osztás nem lehetséges.")
        exit()
print("Eredmény:",result)