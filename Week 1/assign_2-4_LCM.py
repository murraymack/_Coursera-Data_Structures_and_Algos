# Exercise 2-4 Least Common Multiple

def LCM(a, b):

    a_temp = int(a)
    b_temp = int(b)
    
    large_base = max(a_temp, b_temp)
    small_base = min(a_temp, b_temp)
    large = max(a_temp, b_temp)
    small = min(a_temp, b_temp)
    
    if large == 0 or small == 0:
        return large_base
    if large == small:
        return small_base
    
    ratio = large/small
    mod = a_temp % b_temp
    
    if mod / b_temp > 0.5: 
        mod50thresh = mod / b_temp
    
    while ratio != 1:
        if large > small:
            small = small + small_base
            ratio = large / small
        if large < small:
            large = large + large_base
            ratio = large / small
    return small

a,b = input().split(" ")
print(LCM(a,b))