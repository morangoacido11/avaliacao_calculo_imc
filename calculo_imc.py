#Calcular IMC
print("="*30)
print("Calculador de IMC")
print("="*30)

def calcular_imc(peso,altura):
    imc = peso/(altura*altura)
    return imc
def classificar_imc(valor_imc):
    if valor_imc < 25:
        return "NORMAL"
    else:
        return "ACIMA DO PESO"
    
