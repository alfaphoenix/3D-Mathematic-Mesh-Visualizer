ip = input('введите ip: ')
a = ip.split('/')
b = ''
b+= int()
for i in range(32):
    if int(a[1]) < 32:
        b+= '1'
    else:
        b+= '0'
print(b)
