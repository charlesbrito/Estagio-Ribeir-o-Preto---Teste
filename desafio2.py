#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, 
# além de informar a quantidade de vezes em que ela ocorre.

#IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;


def contar_a(s):
    contar_maiusculo = s.count('A')
    contar_minusculo = s.count('a')
    
    return contar_maiusculo, contar_minusculo

texto = str(input("Escreva um texto "))
maisculo,minusculo = contar_a(texto)
print(f"Quantidade de A maiúsculo: {maisculo}")
print(f"Quantidade de A minúsculo {minusculo}")
