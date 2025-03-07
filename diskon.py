total = int(input("Masukan total belanjaan :"))
if total >= 100000:
    dis10 = total * 0.1
    hasil10 = total - dis10
    print("Total Belajaan : Rp.",total)
    print("mendapatkan diskon 10% menjadi : Rp.",hasil10)
elif total >=50000:
    dis5 = total * 0.05
    hasil5 = total - dis5
    print("Total Belajaan : Rp.",total)
    print("mendapatkan diskon 5% menjadi : Rp.",hasil5)
else:
    print("Total Belajaan : ",total)