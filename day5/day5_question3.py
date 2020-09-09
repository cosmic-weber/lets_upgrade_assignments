str = "hey this is sai, I am in mumbai,...."
ls =[]
print(str)
#function
def strcap(String):
    lst = list(str.split())
    for i in lst:
        a = i.capitalize()
        ls.append(a)
    for i in ls:
        print(i, end=" ")

strcap(str)
