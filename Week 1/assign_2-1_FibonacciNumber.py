# Exercise 2-1: Fibonacci Number

def FibNumber(n):
    mySeq = []
    
    if n == 0 or n == 1:
        return n
    elif n == 2:
        return 1
    else:
        mySeq = [0, 1]
        for i in range(n-1):
            appendVal = mySeq[len(mySeq)-1]
            appendVal2 = mySeq[len(mySeq)-2]
            mySeq.append(appendVal + appendVal2)

    return mySeq[-1:][0]

a = int(input())
print(FibNumber(a))