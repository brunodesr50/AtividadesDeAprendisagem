def verificar_perfeito(numero):
    lista=[]
    for a in range(1,numero):
        if numero%a==0:
            lista.append(a)
            somado=sum(lista)
        if a==numero-1:
            if somado==numero:
                print(numero,"é um numero perfeito")
           
            else:
                print(numero,"nao é um numero perfeito")


def ate_perfeito():
    coisa=int(input("digite um numero para saber quais vai ser perfeito ate ele : "))  
   
    for numero in range(1, coisa+1):
        listaa=[]
        for a in range(1,numero):
            if numero%a==0:
                listaa.append(a)
                somado=sum(listaa)
            if a==numero-1:
                if somado==numero:
                    print(numero,"é um numero perfeito")        




     
numero= int(input("digite um numero para ver se ele é perfeito: "))


verificar_perfeito(numero)
ate_perfeito()

