str = input("Tulis kalimat : ")

#Capitalize
c = str.capitalize()
print("Penulisan dengan huruf awal kapital :", c)

#Upper & Lower
u = str.upper()
l = str.lower()
print("Kalimat dengan semua huruf kapital :", u)
print("Kalimat dengan semua huruf kecil :", l)

#Count
a = str.count('a')
e = str.count('e')
print("jumlah huruf a :", a)
print("jumlah huruf e :", e)

#Center
cntr = str.center(50, "*")
print("Kalimat dengan center :", cntr)

#Replace
r = str.replace("a", "b")
print("Kalimat dengan huruf 'a' diganti 'b' :", r)