def cift_tek(a):
    if(a%2 == 0):

        return a
    else:
        raise ValueError

liste = [1,23,4345,564,123,23,14,16,18,24]
for i in liste:
    try:
        print(cift_tek(i))
    except ValueError:
        pass