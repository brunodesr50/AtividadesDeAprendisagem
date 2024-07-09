lista=[]


while True:
    x= int(input("digite um numero e 0 para parar:"))
    if x==0:
        break
    else:
        lista.append(x)
   






y= sorted(lista,reverse=True)


while len(lista)>5:
    menor=min(lista)
    lista.remove(menor)
while True:
    if len(y)>5:
        y.pop(-1)
    else:
        break


print(f"os 5 maiores na ordem q foi digitardo: {lista}")
print(f"os 5 maiores na ordem decrescente: {y}")

