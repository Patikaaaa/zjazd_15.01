print("program do obliczania pola kwadratu")
a=int(input("Podaj długość boku"))
p=a**2
print("pole kwadratu wynosi",p)

print("program do obliczania pola prostokątu")
a=int(input("Podaj długość boku"))
b=int(input("Podaj długość boku"))
p=a*b
print("pole prostokąta wynosi",p)

print("program do obliczania pola trójąta")
a=int(input("Podaj długość boku"))
h=int(input("Podaj długość wysokości"))
p=(a*h)/2
print("pole trójąta wynosi",p)

d=int(input("podaj dzień:"))
m=input("podaj miesiąc(w dopełniaczu):")
r=int(input("podaj rok:"))
print(d, m, r, "r")
# mamy date

print("zad5a")
# a+b -x^2
a=int(input("Podaj wartość liczby a"))
b=int(input("Podaj wartość liczby b"))
x=int(input("Podaj wartość liczby x"))
p=a+b-x**2
print("zad5a",p)

print("zad5b")
# a-b/c-3
a=int(input("Podaj wartość liczby a"))
b=int(input("Podaj wartość liczby b"))
c=int(input("Podaj wartość liczby c"))
p=a-b/c-3
print("zad5b",p)

print("zad5c")
# 3(4+5a)(b-c^3)
a=int(input("Podaj wartość liczby a"))
b=int(input("Podaj wartość liczby b"))
c=int(input("Podaj wartość liczby c"))
p=3*(4+(5*a))*(b-(c**3))
print("zad5c",p)

print("zad6a")
# a=a+4
a=int(input("Podaj wartość liczby a"))
p=a+4
print("zad6a",p)  
