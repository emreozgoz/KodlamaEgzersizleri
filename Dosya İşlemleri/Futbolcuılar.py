with open("futbolcular.txt","r",encoding="utf-8") as file:

    bjk = list()
    gs = list()
    fb = list()

    for satir in file:
        satir =satir[:-1]
        satir_elemanları = satir.split(",")
        if(satir_elemanları[1]=="Fenerbahçe"):
            fb.append(satir+"\n")
        elif(satir_elemanları[1] == "Galatasaray"):
            gs.append(satir+"\n")

        else:
            bjk.append(satir+"\n")

    with open("gs.txt","w",encoding="utf-8") as file123:
        for i in gs:
             file123.write(i)

    with open("bjk.txt","w",encoding="utf-8") as file2:
        for i in bjk:
            file2.write(i)

    with open("fb.txt","w",encoding="utf-8") as file3:
        for i in fb:
            file3.write(i)