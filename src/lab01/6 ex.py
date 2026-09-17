och = 0
zaoch = 0
n = int(input('n = '))
for i in range(1,n+1):
    num = input('in_'+ str(i)+':' + ' ').split()
    if len(num)==4:
        if num[-1]== 'True' or num[-1]=='False':
            if num[-1]== 'True':
                och +=1
            else:
                zaoch +=1
        else:
            print('Данные некорректны')
    else:
        print('Данные некорректны')
print(f'out: {och} {zaoch}')
