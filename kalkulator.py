#kalkulator sederhana

print('Kalkulator Sederhana')
print(20*"-")

angka1 = float(input("Masukkan Angka 1 : "))
operator = input("Operator (+,-,x,/) : ")
angka2 = float(input("Masukkan Angka 2 : "))

#Percabangan
if operator == "+" :
    hasil = angka1 + angka2
    print(15 * "-")
    print(f"Hasil : ", hasil)
    print(15 * "-")
elif operator =="-" :
    hasil = angka1 - angka2
    print(15 * "-")
    print(f"Hasil : ", hasil)
    print(15 * "-")
elif operator == "x" :
    hasil = angka1 * angka2
    print(15 * "-")
    print(f"Hasil : ", hasil)
    print(15 * "-")
elif operator == "/" :
    hasil = angka1 / angka2
    print(15 * "-")
    print(f"Hasil : ", hasil)
    print(15 * "-")
else :
    print("Ada Kesalahan")
