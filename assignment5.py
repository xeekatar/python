#Jimmy Wallace
#CA 5
#50 Minutes
#Got some help from my Dad

epsilon = .001
x = float(input('Please enter a number: '))    #Variables
i = 1.01

while True:
    if i * i > x - epsilon and i * i < x + epsilon:    #Checks to see if i * i is close enough to the input
        print(i,'is the square root of',x)
        break
    elif i > x:    #For debugging
        print('Error')
        print('i became larger than x!')
        break
    i += epsilon

