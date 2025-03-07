nomor = int(input("masukan angka :"))
if nomor == 0:
    bil = "nol"
elif nomor >= 0:
    bil = "Positif"
elif nomor <= 0:
    bil = "Negatif"

print(nomor,"= angka kamu adalah",bil)