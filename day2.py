# List and it's default function
lst = ["Nevada", 1, 9, "berlin", 0]
print(lst)

lst.append("genau")
print(lst)

lst.extend(["proxima"])
print(lst)

lst.insert(0, "utah")
print(lst)

lst.remove("utah")
print(lst)

lst.pop(1)
print(lst)

print('\n')

# Dictionary and it's default function
my_dict = {1: 'apple', 2: 'ball'}
print(my_dict.get(2))
my_dict[3] = 'sweden'
print(my_dict)
print(my_dict.keys())
print(my_dict.pop(3))
my_dict.update({1: 'klingon'})
print(my_dict)


# Sets and it's default function
a = set()
a = {5,4}
print(a)
a.add(99)
print(a)
a.discard(99)
print(a)
A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(A | B)
print(A & B)
print(A - B)
print(B - A)

# Tuple and it's method
my_tup = tuple()
my_tup = ('p', 'q', 'r', 's', 't', 'u', 'v')
print(my_tup)
print(my_tup[0:3])
print(my_tup[-7])
q_tup = (1, 2, 5, [0,33])
print(q_tup[3][1])
print(2 in q_tup)
print('s'in my_tup)

# String and it's default function
str = "i love to learn new programming languages"
print(str)
print(str[3:12])
st = str + " beleive me not everyone is good in python" + ' 23'
print(st)
a = st.index('23')
print(int(a)+16)
print(st*2)
