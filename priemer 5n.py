a=int(input("kolko celych cisiel:"))
priemer=0

for i in range(a):
    cisiel = float(input("zadaj cele cislo: "))
    priemer +=cisiel

avg = priemer/a


print ("priemer", a ,"cislo je: ",avg)
