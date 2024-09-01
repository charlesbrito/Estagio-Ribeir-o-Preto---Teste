#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
#  (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar 
# onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;




def verificar_numero(numero):
    a,b = 0,1
    
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a+b 
    return False

numero = int(input("Digite o número que deseja verificar"))
if verificar_numero(numero):
    print(f" {numero} está na sequência Fibonacci")
else:
    print(f"{numero} não está na sequência Fibonacci")