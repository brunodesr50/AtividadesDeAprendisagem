

a = float(input("coloque A de Bhaskara: "))
while a==0:
    print("A nao pode ser igual a 0")
    a=float(input("coloque A de Bhaskara"))


b = float(input("coloque B de Bhaskara: "))
c = float(input("coloque C de Bhaskara: "))


def delta(a,b,c):
    result_delta= (b**2-4*a*c)
    print(result_delta)
    if result_delta<0:
   
   
        print("raiz negativa")
        exit()
    return result_delta
20
def baskara(a,b,result_delta):
    positivo_baskara= ((-1*b) + (result_delta**(1/2)))/(a*2)
    negativo_baskara= ((-1*b) - (result_delta**(1/2)))/(a*2)
    print( f"os resultado é {positivo_baskara} e {negativo_baskara}" )
    return


result_delta=delta(a,b,c)


baskara(a,b,result_delta)
