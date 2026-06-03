#Calcular IMC
#Ana Gabriely - Calculos
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

#Maria Eduarda pellegrini - status
def gerar_aviso(status, imc_valor):
    print(f"seu IMC é: {imc_valor:.2f}")
    if status == "NORMAL":
        return "muito bem seu IMC é normal! mantenha-se saudável"
    else:
     return "seu IMC é acima de 25.., cultive uma rotina equilibrada! isso manterá sua saúde em dia!!!"
#Ana Gabriely - Variaveis (peso,altura)
peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))
