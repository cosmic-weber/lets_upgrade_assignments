def primenumbers(item):

    if item>1:
        for a in range(2, item):
            if item%a == 0:
                break
        else:
            return True

lst = list(range(1, 2501))
lst_new = filter(primenumbers, lst)
print(list(lst_new))
