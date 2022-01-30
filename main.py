
def x3_1(x):
    returne x*3+1

def x2(x):
    return x/2

def f1():
    while True:
        try:
            x = int(input("Введите валидное число:\n"))
            return x
        except:
            pass

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
print(collatz(f1()))
