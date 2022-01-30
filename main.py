def collatz(x):
    result=[]
    while(x!=1):
        result.append(x)
        if(x%2==0):
            x=x2(x)
        else:
            x=x3_1(x)
    result.append(x)
    return result
