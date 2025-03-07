matematika = int(input("Masukkan nilai Matematika (0-100): "))
while matematika < 0 or matematika > 100:
    matematika = int(input("Nilai tidak valid. Masukkan nilai Matematika (0-100): "))

sains = int(input("Masukkan nilai Sains (0-100): "))
while sains < 0 or sains > 100:
    sains = int(input("Nilai tidak valid. Masukkan nilai Sains (0-100): "))

bahasa_inggris = int(input("Masukkan nilai Bahasa Inggris (0-100): "))
while bahasa_inggris < 0 or bahasa_inggris > 100:
    bahasa_inggris = int(input("Nilai tidak valid. Masukkan nilai Bahasa Inggris (0-100): "))


rata_rata = (matematika + sains + bahasa_inggris) / 3


jumlah_bawah_70 = sum(1 for nilai in [matematika, sains, bahasa_inggris] if nilai < 70)
nilai_sempurna = any(nilai == 100 for nilai in [matematika, sains, bahasa_inggris])


if rata_rata > 75 and jumlah_bawah_70 <= 1 and nilai_sempurna:
    print("Anda Lulus!")
else:
    print("Anda Tidak Lulus.")
