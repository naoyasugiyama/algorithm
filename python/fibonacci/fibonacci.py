import math

def fibonacci01(c):
    if c < 2:
        return c
    return fibonacci01(c-2) + fibonacci01(c-1)

def fibonacci02(c):
    x,y = 0, 1
    for _ in range(c):
        x,y = y, x+y    
    return x

def fibonacci03(c):
   return round( (math.pow((1+math.sqrt(5))/2,c ) - math.pow((1-math.sqrt(5))/2,c))/math.sqrt(5) )
    

if __name__ == '__main__':
    print('get fibonacci')
