def pisahkanGenapGanjil(inputBilangan):
    list_genap = []
    list_ganjil = []

    for x in inputBilangan.split():
        bilangan = int(x)
        if bilangan % 2 == 0:
            list_genap.append(bilangan)
        else:
            list_ganjil.append(bilangan)

    tuple_ganjil = tuple(list_ganjil)
    return list_genap, tuple_ganjil

inputBilangan = input("masukkan beberapa bilangan(pisahkan spasi) : ")

resultGenap, resultGanjil = pisahkanGenapGanjil(inputBilangan)

print("Hasil Genap : ", resultGenap)
print("Hasil Ganjil : ", resultGanjil)