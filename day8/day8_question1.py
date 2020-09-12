def getinput(calculate_arg_fun):
    def fibonacci():
        print("This is a fibonnaci series function")
        a = int(input("Enter starting number: "))
        b = int(input("Enter ending number: "))
        calculate_arg_fun(a,b)
    return fibonacci

@getinput
def terms(a,b):
    n1, n2 = 0, 1
    while True:
        nth = n1 + n2
        c = n2
        noth = 0
        if nth == a:
            print("starting: " , end =" ")
            print(a)
            while noth!=b:
                noth = c + a
                print(noth)
                c = a
                a = noth
        n1 = n2
        n2 = nth
        if noth == b:
            break
terms()
