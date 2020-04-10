l1 = list(range(1, 10))
l2 = list('hello')

s_num = '-'.join(map(str, l1))

space = " "
s_string = space.join(l2)

print(s_num)
print(s_string)