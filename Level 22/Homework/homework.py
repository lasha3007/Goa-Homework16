def numbers_product():
    strt= int(input("start: "))
    end = int(input("end: "))
    step = int(input("step: "))

    s = strt

    listn  = 1

    while s<=end: 
        if s % 3 == 0:
            listn=listn * s
        s+=step


    print(listn)

numbers_product()



