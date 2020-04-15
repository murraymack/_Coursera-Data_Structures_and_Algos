def EuclidGCD(a, b):

    a_temp = int(a)
    b_temp = int(b)
    
    if b > a:
        a_temp = int(b)
        b_temp = int(a)
        
    if a == b:
        return a
    
    while a_temp % b_temp != 0:
        old_b_temp = b_temp
        b_temp = a_temp % b_temp
        a_temp = old_b_temp
    
    return b_temp

a,b = input().split(" ")
print(EuclidGCD(a,b))