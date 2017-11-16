file = open("kttekst.txt", "r")
mSõnad = 0
for words in file:
    word = words.split()
    mSõnad += len(word)
sPikkus = 0
for pikk in words:
    if(len(pikk) < 5):
        Pikkus = pikk.split()
        sPikkus += len(Pikkus)
file.close()
print("Failis on: " + str(mSõnad) + " sõna")
print("Failis on: " + str(sPikkus) + " sõna, mis on väiksemad, kui 5")    
