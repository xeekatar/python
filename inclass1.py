def findOdds (num1, num2):
    c = ()
    for i in range(num1, num2 + 1):
        if i % 2 != 0:
            c += (i,)
        if i % 2 == 0:
            pass
    return c
            
        
        
    
