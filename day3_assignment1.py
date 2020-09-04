# program for pilot
alt = int(input("Enter altitude: "))

if (alt == 1000 or alt < 1000):
    print('Safe to land')
elif ( alt > 1000 and alt < 5000):
    print('Bring down to 1000')
elif alt > 5000:
    print('Turn Around')
