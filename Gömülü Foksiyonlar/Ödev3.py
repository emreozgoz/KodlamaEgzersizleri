from functools import reduce
listesayi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtre = list(filter(lambda x:x%2==0,listesayi))
print(reduce(lambda x,y:x+y,filtre))