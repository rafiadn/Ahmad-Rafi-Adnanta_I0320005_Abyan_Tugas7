data_usia = input("Masukkan Data Usia (Dipisahkan dengan Spasi) : ").split()

#Konversi menjadi tipe int
for u in range(len(data_usia)):
    data_usia[u] = int(data_usia[u])
print("Data Usia : ", data_usia)

import math
#Max
print("Usia paling tua adalah", max(data_usia))

#Min
print("Usia paling muda adalah", min(data_usia))

#Rata-rata
rata2 = sum(data_usia)/len(data_usia)
print("Rata-rata usia adalah ", rata2)

#Ceil
print("Rata-rata usia dengan pembulatan ke atas adalah ", math.ceil(rata2))

#Floor
print("Rata-rata usia dengan pembulatan ke bawah adalah ", math.floor(rata2))
