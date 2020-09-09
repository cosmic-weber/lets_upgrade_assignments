lst  = [1,5,6,4,1,2,3,5]

ast = [1,1,5]
b = list()
for i in ast:
    for n in lst:
        if i == n:
            b.append(i)
            if lst.index(n)==0:
                lst.remove(n)
            else:
                del lst[:int(lst.index(n))+1]
            break

if b == ast:
    print("it's a Match")
else:
    print("it's a gone")
