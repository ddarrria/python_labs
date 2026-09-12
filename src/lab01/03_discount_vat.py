price = int(input('price(₽): '))
discount = int(input('discount(%): '))
vat = int(input('vat(%): '))
base = price*(1-discount/100)
vat_amout = base*(vat/100)
total = base + vat_amout
print(f'База после скидки: {base:.2f} ₽')
print(f'НДС: {vat_amout:.2f} ₽')
print(f'Итого к оплате: {total:.2f} ₽')