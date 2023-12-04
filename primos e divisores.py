def intp():
    primo=0
    naoprimo=0
    x = int(input("Digite um numero positivo:"))
    while x<0:
         x = int(input("Digite x um numero positivo seu acefalo:"))
    if x == 2 or x == 3 or x == 5 or x == 7:
        primo=x
    elif x%2==0:
        naoprimo=x
    elif x%3==0:
        naoprimo=x
    elif x%5==0:
        naoprimo=x
    elif x%7==0:
        naoprimo=x
    else:
        primo=x
    if naoprimo!=0:
        indev(naoprimo)
    else:
        print("primo", primo )


def indev(y):
   
    for t in range(1,y+1):
        if y%t==0:
         
         print(t)
intp()

