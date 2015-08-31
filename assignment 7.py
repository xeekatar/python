def anyRoot(number, root, epsilon = .0001):
    guess = 1.0
    iterations = 0
    minimum = 1
    maximum = number
    guess = (minimum + maximum) / 2

    while abs(guess**root - number) >= epsilon:
        if guess**root > number:
            maximum = guess
        elif guess**root < number:
            minimum = guess
        guess = (minimum + maximum) / 2
        iterations += 1
        print(iterations,guess)
    print('Number of guesses =',iterations)
    return str(guess) + ' is root ' + str(root) + ' of ' +str(number)
    

