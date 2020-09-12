print("This code is gonna open a file and try to write in read only mode")

f = open("mbox.txt", "r")
try:
    f.write("2024 is the year in which mars gonna have human colonizing the planet for human exploration")
except:
    for i in f:
        print(i)

f.close()
