NumList1 = [11, 15, 6, 13, 13, 25, 32, 11, 20, 5, 31, 16, 32, 29, 11, 13, 3, 29, 28, 24]
NumList2 = [5, 19, 16, 4, 12, 7, 2, 28, 34, 29, 29, 36, 6, 8, 24, 18, 31, 7, 1, 7]
#1)
print("-----------(1)-----------")
print("Sarnased arvud on: ")
print(set(NumList1) & set(NumList2))

#2)
print("-----------(2)-----------")
suur = max(NumList1 + NumList2)
print("Kahe listi suurim arv on: ", suur)

#3)
print("-----------(3)-----------")
väike = min(NumList1 + NumList2)
print("Kahe listi väikseim arv on: ", väike)

#4)
print("-----------(4)-----------")
a = sum(NumList1) / 20
print("Esimese listi keskmine summa on: ", a)

b = sum(NumList2) / 20
print("Teise listi keskmine summa on: " , b)

#5)
print("-----------(5)-----------")

a = (sum(NumList1) + sum(NumList2)) / 40

print("Kahe listi keskmine summa on: ", a)
