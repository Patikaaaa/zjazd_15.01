zmienna = 1
while zmienna < 5:
    print ("python")
    zmienna += 1

# program wyświetlający liczby od 1 do 100
for i in range(1,101):
    print(i)
# prgram wyświetlający liczby od 100 do 0
    liczba = 100
    while liczba >= 1:
        print(liczba)
        liczba -= 1

# napisz program wyświetlający liczby parzyste od 2 do 50
        zmienna = 2
        while zmienna <= 50:
            print(zmienna)
            zmienna += 2
# Napisz program wyświetlający liczby podzielne przez 8 (w zakresie 1..100)
zmienna = 8
while zmienna <= 100:
    print(zmienna)
    zmienna += 8

# Napisz program wyświetlający liczby podzielne przez 3 lub 5 (w zakresie 1..100)
for x in range (0,100):
            if (x % 3 == 0 or x % 5==0):
                 print(x)

 #Napisz program wyświetlający liczby podzielne przez 3 albo 5 ( w zakresie 1..100) (nie wypisuj tych podzielnych jednocześnie przez 3 i 5)
for x in range (0,100):
            if((x % 3==0 or x % 5==0) and x % 15!= 0):
                  print(x)

#Napisz program, który obliczy i wypisze sumę pięciocyfrowej liczby całkowitej dodatniej.
print(12345+54321)

#Napisz program, który obliczy i wypisz sumę dowolnej liczby całkowitej dodatniej



for wyraz in 'Patrycja':
    print(wyraz)

#Napisz program wyświetlający na konsoli 17 gwiazdek w jednym rzędzie.
zmienna=''
for znak in range (17):
    zmienna=zmienna + '*'
print(zmienna)

#Napisz program wyświetlający na konsoli prostokąt z liter P. Wykorzystaj pętle.
figura=''
for wiersz in range(5):
    for znak in range (17):
        figura=figura + 'p'
    figura=figura+'\n'
print(figura)


