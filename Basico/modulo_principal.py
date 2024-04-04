# Exemplos de import
# 1º Tipo
# import modulo_funcoes

# def main()
#     modulo_funcoes.soma(num1, num2)

#2º Tipo
# import modulo_funcoes as mf

# def main()
#     mf.soma(num1, num2)

#3º Tipo ( Importando as funcoes que eu quero trabalhar)
# import modulo_funcoes
# from modulo_funcoes import soma, subtracao

# def main()
#     soma(num1, num2)

#4º Tipo ( Importando todas as funcoes do modulo)
import modulo_funcoes
from modulo_funcoes import *

def main()
    soma(num1, num2)



import modulo_funcoes 
from modulo_funcoes import *


def main():
    num1 = float(input("Digite um numero para calculo:"))
    num2 = float(input("Digite outro numero para calculo:"))

    operacao = input("Digite a operacao a ser realizada (+, -, /, *):")

    if operacao == '+':
        res = soma(num1, num2)
        print("O resultado da operacao eh: ", res)
    elif operacao == '-':
        res = subtracao(num1, num2)
        print("O resultado da operacao eh: ", res)
    elif operacao == '/':
        if num2 != 0: 
            res = divisao(num1, num2)
            print("O resultado da operacao eh: ", res)
        else:
            print("Não existe divisao por zero!!!")
    elif operacao == '*':
        res = multiplicacao(num1, num2)
        print("O resultado da operacao eh: ", res)
    else:
        print("Operacao Invalida!!!")

if __name__ == "__main__":
    main()