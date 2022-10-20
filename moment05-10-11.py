#10
with open('utskrift.txt', 'w') as fw: ##öppnar eller skapar en txt fil 'utskrift.txt' i skrivläge och skriver över redan existerande innehåll.
  fw.write('''1 2 3
4 5 6
7 8 9
''') #Skriver till filen denna text
  fw.write('\nHär var det rutigt!') #Skriver till filen denna text
with open('utskrift.txt', 'r') as fr: #öppnar filen 'utskrift.txt i läsläge, programmet kan inte ändra filen
  print(fr.read()) #skriver ut filens innehåll

  
  
 #11
rent = 1.03
cRent = 1.03
sCash = 10000
cCash = 10000
tRent= 3
with open('rant.txt', 'w') as bnkW:
    for i in range(1, 16):
        cRent = rent**i
        tRent = (cRent - 1)*100
        cCash = sCash * rent
        bnkW.write('{0}|{1:.0f}|{2:.2f}\n'.format(i,cCash,tRent ))
with open('rant.txt', 'r') as bnkR:
    print(bnkR.read())
