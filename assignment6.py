def power(num, power):

    ans = 1 

    for i in range(power):
        ans = num * ans
    return ans

def anyRoot(num, root, eps = .0001):

    guess = 1

    while True:
        ans = power(guess, root)
        if ans >= num - 100 * eps and ans <= num + 100 * eps:
            return guess
        elif guess > num:
            return 'Error'
        guess += eps



                
