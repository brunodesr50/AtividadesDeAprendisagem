

def zerar():
    lista_pilha= [-1]*50
    lista_fila= [-1]*50




    fim_pilha=-1
    fim_fila=-1
    ini_fila=-1
    return lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila




def adicionar(lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila):
   
    numero = int(input("Coloque o numero: "))
    if fim_pilha < 49:  
        if fim_pilha==-1:
            fim_pilha=1


        else:
            fim_pilha += 1
    lista_pilha[fim_pilha] = numero
   
   
    if fim_fila < 49:
        if fim_fila==-1:
            fim_fila=1
           
        else:
            fim_fila += 1
    lista_fila[fim_fila] = numero
    return lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila




def retirar(lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila):
    if -1 != fim_pilha:
        fim_pilha +=- 1
    else:
        print("lista ta cheia")




    if ini_fila != fim_fila:
        ini_fila += 1
    else:
        print("lista ta cheia")
    return lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila




def retirar_elem(lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila):
   
    n = int(input("coloque quantos numeros vc quer retirar: "))
    if fim_pilha>= n:
           
        fim_pilha += -n
       
    else:
        print(" nao da pra tirar essa quantidade de elementos")




    if ini_fila+n<=fim_fila :
       
        if ini_fila==-1:
            ini_fila = n
        else:
            ini_fila+=n
    else:
        print(" nao da pra tirar essa quantidade de elementos")


    return lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila


           










def zerar_total():
    ini_fila=fim_fila
    fim_pilha=-1
    return lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila




def exibir(lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila):
   
    print("fim da pilha", fim_pilha)
    print("fim da fila", fim_fila)
    print("ini da fila", ini_fila)
    print(lista_fila,lista_pilha)
   




lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila= zerar()
lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila=adicionar(lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila)
exibir(lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila)


lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila=adicionar(lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila)
lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila=adicionar(lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila)
lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila=adicionar(lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila)
exibir(lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila)


lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila=retirar_elem(lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila)
exibir(lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila)


lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila=adicionar(lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila)
lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila=adicionar(lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila)
lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila=retirar(lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila)
exibir(lista_fila, lista_pilha, fim_fila, fim_pilha,ini_fila)






"nome das pessoas q fizeram em sala : Bruno De Souza, Darlan Rosario, Danilo Rosario, Claudio Roberto, Emily rachel, rafaela, asafe, rafael ferreira, yuri"
