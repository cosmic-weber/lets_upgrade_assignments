for i in range(1, 201):
    if i>1:
        for a in range(2, i):
            if i%a == 0:
                break
        else:
            print(i)
