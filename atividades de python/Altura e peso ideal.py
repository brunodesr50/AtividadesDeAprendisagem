

def masculino(altura,peso):
    peso_homem = 52 + (0.75 * (altura - 152.4))
   
    m=m+1


    if peso_homem>peso:
        maiorph=maiorph+1
    else:
         menorph=menorph+1
   
    return(m,peso_homem,maiorph,menorph)


def feminino(altura,peso):
    peso_mulher = 62,1 * (altura - 44,7)
   
    f=f+1
    if peso_homem>peso:
        maiorpm=maiorpm+1
    else:
         menorpm=menorpm+1
    return(f,peso_mulher,maiorpm,menorpm)








while True:
    peso=0
    altura=0
    sexo= "a"


    peso=float(input("coloque o peso: "))
    if peso<0:
        break
   
    sexo= input("digite seu genero: ")
    while sexo!= "Masculino" and sexo!= "Feminino":
         sexo= input("digite um genero existente(Masculino ou  Feminino): ")
   
    altura=float(input("digite a altura: "))


    if sexo== "feminino":
            feminino(altura,peso)
            f,peso_mulher,maiorpm,menorpm=(feminino())
    elif sexo == "masculino":
            masculino (altura,peso)
            m,peso_homem,maiorph,menorph=(masculino())






def regras (peso_mulher,m,peso_homem,maiorpm,menorpm,maiorph,menorph):
     
    print(f"tem {f} mulheres no programa e {m} homens ")
    mediagenero=(peso_homem+peso_mulher)/(f+m)
    print("a meida dos dois generos é:", mediagenero)
   
    mediahomem=peso_homem/m
    print(f"a media de peso de todos os homens são: {mediahomem}")


    mediamulher=peso_mulher/f
    print(f"a media de peso de todas as mulheres é: {mediamulher}")


    print(f"a quantidade de pessoas acima da media é {maiorph+maiorpm}")
    print(f"a quantidade de pessoas abaixo da media é {menorph+menorpm}")
     
regras(f,peso_mulher,m,peso_homem,maiorpm,menorpm,maiorph,menorph)
