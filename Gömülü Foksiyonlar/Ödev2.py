def ucgen(ku):
    if (abs(ku[0]+ku[1]) > ku[2] and abs(ku[0]+ku[2]) > ku[1] and abs(ku[1]+ku[2]) > ku[0]):
        print(ku[0],ku[1],ku[2])
        return True
    else:
        return False

ku = [(3,4,5),(6,8,10),(3,10,7)]
print(list(filter(ucgen,ku)))