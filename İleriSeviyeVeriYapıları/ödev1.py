Kelime = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
sözlük = dict()
for i in Kelime:
    if(i in sözlük):
        sözlük[i] +=1
    else:
        sözlük[i] = 1
print(sözlük)
