def Alan_hesapla(demet):
    return demet[0]*demet[1]
demet = [(3,4),(10,3),(5,6),(1,9)]
print(list(map(Alan_hesapla,demet)))