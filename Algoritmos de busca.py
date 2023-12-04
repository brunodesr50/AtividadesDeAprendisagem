
lista = [333,44,5,6,3342,6,7,43,42,1,8,9,9,-1,-145,55,434,88,99,76,56,789,432,236,879]
lista.sort()
print(lista)




def busca_ordenada(lista,elemento,tamanho):
    if elemento < lista[0]:
        print(f"elemento {elemento} nao esta na lista")
    elif elemento > lista[tamanho-1]:
        print(f"elemento {elemento} nao esta na lista")
   


    for indice in range(tamanho):
        if lista[indice] == elemento:
            print(f"elemento {elemento} encontrado na posição {indice}")
            break
        elif elemento< indice:
            print(f"elemento {elemento} nao esta na lista")
            break
     
def busca_binaria(lista, elemento, tamanho):
    inicio = 0  
    fim = tamanho - 1
    while inicio <= fim:
        meio = round((inicio + fim) /2)
        numero = lista[meio]


        if numero == elemento:
            print(f"Elemento {elemento} encontrado na posição {meio}")
            return meio
        elif elemento < numero:
            fim = meio - 1
        else:
            inicio = meio + 1


    print(f"Elemento {elemento} não está na lista")




elemento= int(input("coloque o numero: "))
print("resposta por lista ordenada:")
busca_ordenada(lista,elemento,len(lista))
print("resposta por lista binaria:")


busca_binaria(lista,elemento,len(lista))

