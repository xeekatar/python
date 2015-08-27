##Temperature Calculator

print('Temperature Converter')
print()
print(' 1: Fahrenheit to Celcius')
print(' 2: Fahrenheit to Kelvin')
print(' 3: Celcius to Fahrenheit')
print(' 4: Celcius to Kelvin')
print(' 5: Kelvin to Fahrenheit')
print(' 6: Kelvin to Celcius')
print(' 7: Danks to Memes')
print()

while True:
    choice = input('Please choose a conversion (1,2,3,etc): ')
    print()
    num = int(input('Please enter the number you want to convert: '))
    print()
    if choice == '1':
        result = (num - 32) * 5/9
        print(result, 'degrees celcius')
        break
    if choice == '2':
        result = (num + 459.67) * 5/9
        print(result, 'degrees kelvin')
        break
    if choice == '3':
        result = num * 9/5 + 32
        print(result, 'degrees fahrenheit')
        break
    if choice == '4':
        result = num + 273.15
        print(result, 'degrees kelvin')
        break
    if choice == '5':
        result = (num - 273.15) * 1.8 + 32
        print(result, 'degrees fahrenheit')
        break
    if choice == '6':
        result = num - 273.15
        print(result, 'degrees celcius')
        break
    if choice == '7':
        print('R' + num * 'E' + '!!!!')
        break
    
    
