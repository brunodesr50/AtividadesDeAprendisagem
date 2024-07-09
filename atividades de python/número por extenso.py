
numero_principal = int(input("coloque um numero nessa porraaaaaa: "))


lista_numeros= [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


lista_unidade=["","Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove"]


lista_unidade_dois=["","Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez"]
Lista_diabo=["Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove"]


lista_dezenas=["","dez","Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta", "Setenta", "Oitenta", "Noventa"]


lista_centena=["","Cento", "Duzentos", "Trezentos", "Quatrocentos", "Quinhentos", "Seiscentos", "Setecentos", "Oitocentos", "Novecentos"]




def numeros_dezenas(numero_principal):
   
    unidade = numero_principal % 10
    dezena = numero_principal // 10
    if unidade==0:    
        print(f"{lista_dezenas[dezena]}")
    else:
        print(f"o numero {numero_principal} por extenso fica: {lista_dezenas[dezena]} e {lista_unidade[unidade]}")
   
       
def numeros_centenas(numero_principal):
   
    unidade = numero_principal % 10
    dezena = ((numero_principal%100)//10)
    centena= numero_principal//100
   
    if unidade==0:
        print(f"o numero {numero_principal} por extenso fica:{lista_centena[centena]} e {lista_dezenas[dezena]} ")
    elif dezena==0:
        print(f"o numero {numero_principal} por extenso fica:{lista_centena[centena]}  e {lista_unidade[unidade]}")
    else:
        print(f"o numero {numero_principal} por extenso fica:{lista_centena[centena]} e {lista_dezenas[dezena]} e {lista_unidade[unidade]}")
       
def numeros_mill(numero_principal):
   
    unidade = numero_principal % 10
    dezena = ((numero_principal%100)//10)
    centena= ((numero_principal%1000)//100)
    mill= numero_principal//1000
   
    unidade_mill = mill % 10
    dezena_mill = ((mill%100)//10)
    centena_mill= mill//100
   
    if mill==1:
        print(f"o numero {numero_principal} por extenso fica:  mill {lista_centena[centena]} e {lista_centena[centena]} e {lista_unidade[unidade]} ")
    elif mill==1 and numero_principal>=1 and numero_principal<=19:
        print(f"o numero {numero_principal} por extenso fica: mill {lista_centena[centena]}  e {lista_unidade[numero_principal]} ")
       
    elif mill>=1 and mill<=19 and numero_principal>=1 and numero_principal<=19:
        print(f"o numero {numero_principal} por extenso fica: {lista_unidade[mill]} mill {lista_centena[centena]} e   {lista_unidade[numero_principal]} ")
   
    elif numero_principal>=1 and numero_principal<=19:
        print(f"o numero {numero_principal} por extenso fica: {lista_unidade[mill]} mill {lista_centena[centena]} e  {lista_unidade[numero_principal]} ")
       
    elif mill>=1 and mill<=19:
        print(f"o numero {numero_principal} por extenso fica: {lista_unidade[mill]} mill {lista_centena[centena]} e {lista_dezenas[dezena]} e {lista_unidade[unidade]} ")




    else:
        print(f"o numero {numero_principal} por extenso fica:{lista_centena[centena_mill]} e {lista_dezenas[dezena_mill]} e {lista_unidade[unidade_mill]} mill {lista_centena[centena]} e {lista_dezenas[dezena]} e {lista_unidade[unidade]} ")




def numeros_milhao(numero_principal):
   
    unidade = numero_principal % 10
    dezena = ((numero_principal%100)//10)
    centena= ((numero_principal%1000)//100)
    mill= ((numero_principal//1000)%1000)
    milhao=numero_principal//1000000
   
    unidade_mill = mill % 10
    dezena_mill = ((mill%100)//10)
    centena_mill= mill//100
   
    unidade_milh = milhao % 10
    dezena_milh = ((milhao%100)//10)
    centena_milh= milhao//100
   
   
    if milhao>=1 and milhao<=19    and mill>=1 and mill<=19 :
        print(f"o numero {numero_principal} por extenso fica:  {lista_unidade[milhao]} milhoes {lista_unidade[mill]} mill {lista_centena[centena]} e {lista_dezenas[dezena]} e {lista_unidade[unidade]} ")
       
    elif milhao>=1 and milhao<=19:
        print(f"o numero {numero_principal} por extenso fica:  {lista_unidade[milhao]} milhoes {lista_centena[centena_mill]} e {lista_dezenas[dezena_mill]} e {lista_unidade[unidade_mill]} mill {lista_centena[centena]} e {lista_dezenas[dezena]} e {lista_unidade[unidade]} ")
    else:  
        print(f"o numero {numero_principal} por extenso fica:{lista_centena[centena_milh]} e {lista_dezenas[dezena_milh]} e {lista_unidade[unidade_milh]} milhoes {lista_centena[centena_mill]} e {lista_dezenas[dezena_mill]} e {lista_unidade[unidade_mill]} mill {lista_centena[centena]} e {lista_dezenas[dezena]} e {lista_unidade[unidade]} ")
       
def numero_bilhao(numero_pricipal):
    unidade = numero_principal % 10
    dezena = ((numero_principal%100)//10)
    centena= ((numero_principal%1000)//100)
    mill= ((numero_principal//1000)%1000)
    milhao=((numero_principal//1000000)%1000)
    bilhao= numero_pricipal//1000000000
   
    print(f"unidades: {unidade, dezena,centena,mill,milhao,bilhao}")
   
    unidade_mill = mill % 10
    dezena_mill = ((mill%100)//10)
    centena_mill= mill//100
   
    unidade_milh = milhao % 10
    dezena_milh = ((milhao%100)//10)
    centena_milh= milhao//100
   
    unidade_bi = bilhao % 10
    dezena_bi = ((bilhao%100)//10)
    centena_bi= bilhao//100
   
    if milhao>=1 and milhao<=19:
        print(f"o numero {numero_principal} por extenso fica:  {lista_unidade[milhao]} milhoes {lista_centena[centena_mill]} e {lista_dezenas[dezena_mill]} e {lista_unidade[unidade_mill]} mill {lista_centena[centena]} e {lista_dezenas[dezena]} e {lista_unidade[unidade]} ")
       
    elif bilhao>=1 and bilhao<=19:
        print(f"o numero {numero_principal} por extenso fica:{lista_unidade[bilhao]} bilhoes {lista_centena[centena_milh]} e {lista_dezenas[dezena_milh]} e {lista_unidade[unidade_milh]} milhoes {lista_centena[centena_mill]} e {lista_dezenas[dezena_mill]} e {lista_unidade[unidade_mill]} mill {lista_centena[centena]} e {lista_dezenas[dezena]} e {lista_unidade[unidade]} ")
    else:  
        print(f"o numero {numero_principal} por extenso fica:{lista_centena[centena_bi]} e {lista_dezenas[dezena_bi]} e {lista_unidade[unidade_bi]} bilhoes {lista_centena[centena_milh]} e {lista_dezenas[dezena_milh]} e {lista_unidade[unidade_milh]} milhoes {lista_centena[centena_mill]} e {lista_dezenas[dezena_mill]} e {lista_unidade[unidade_mill]} mill {lista_centena[centena]} e {lista_dezenas[dezena]} e {lista_unidade[unidade]} ")






if numero_principal<=19 :
    print(f"o numero {numero_principal} por extenso fica: {lista_unidade[numero_principal]}")
           
elif numero_principal>=20 and numero_principal<=99:
    numeros_dezenas(numero_principal)
   
elif numero_principal>=100 and numero_principal<=999:
    print(f"o numero {numero_principal} por extenso fica:")
    numeros_centenas(numero_principal)
   
elif numero_principal>=1000 and numero_principal<=999999:
    numeros_mill(numero_principal)
   
elif numero_principal>=1000000 and numero_principal<=999999999:
    numeros_milhao(numero_principal)
   
elif numero_principal>=1000000000 and numero_principal<=999999999999:
    numero_bilhao(numero_principal)
else:
    print("coloque um numero menor q 1 trilhao nmrl msm, com um numero desse vc quebra a perna do pião")