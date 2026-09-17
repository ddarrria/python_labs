a = input('строка: ')
r = ''
n1 = 0
n2 = 0
for i in range(len(a)):
    if a[i] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        r = r + a[i]
        n1 = i
        break
for i in range(len(a)):
    if a[i] in '1234567890':
        r = r + a[i+1]
        n2 = i+1
        break
z = n2-n1
for i in range(n2 + z,len(a),z):
    if a[i]=='.':
        r += a[i]
        break
    else:
        r = r + a[i]
print(r)

   