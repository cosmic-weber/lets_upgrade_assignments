def arms():
    # program for Armstrong Number
    for i in range(1, 1001):
         order = len(str(i))
         sum = 0
         temp = i
         while temp > 0:
             a = temp % 10
             sum = sum + a ** order
             temp = int(temp/10)
         if i == sum:
             yield i

a = print(list(arms()))
