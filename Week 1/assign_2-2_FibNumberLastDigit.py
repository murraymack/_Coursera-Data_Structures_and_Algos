# Exercise 2-2: Last Digit of Large Fibonacci Number

def FibNumberLastDigit(n):
    mySeq = [0,1,1]
    sixtyCycle = [0,1,1]
    
    for i in range(60):
        currentLen = len(mySeq)
        appendVal = mySeq[len(mySeq)-1]
        appendVal2 = mySeq[len(mySeq)-2]
        mySeq.append(appendVal + appendVal2)
        last_digit = int(str(mySeq[-1])[-1:])
        sixtyCycle.append(last_digit)
    sixtyCycle = sixtyCycle[0:60]
    
    target = n % 60
    
    return sixtyCycle[target]

a = int(input())
print(FibNumberLastDigit(a))