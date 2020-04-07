bos_harf = ""
with open ("siir.txt","r",encoding="utf-8")as file:
    for i in file:
        bos_harf+= i[0]
    print(bos_harf)