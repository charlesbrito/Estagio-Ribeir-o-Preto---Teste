#4) Descubra a lógica e complete o próximo elemento:

#a) 1, 3, 5, 7, ___
sequencia1 = [1,3,5,7]
diferenca = sequencia1[1] - sequencia1[0]
proximo_numero1 = sequencia1[-1] + diferenca
print(proximo_numero1)
#output: 9 


#b) 2, 4, 8, 16, 32, 64, ____
sequencia2 = [2,4,8,16,32,64]
diferenca2 = sequencia2[1] - sequencia2[0]
proximo_numero2 = sequencia2[-1] * diferenca2
print(proximo_numero2)
#output: 128


#c) 0, 1, 4, 9, 16, 25, 36, ____
sequencia4 = [0,1,4,9,16,25,36]
ultimo_numero = sequencia4[-1]
proximo_numero3 = (int(ultimo_numero**0.5)+1)**2
print(proximo_numero3)
#output: 49



#d) 4, 16, 36, 64, ____
sequencia3 = [4,16,36,64]
proximo_numero3 = sequencia3[-1] + (sequencia3[-1] - sequencia3[-2]) + (sequencia3[-1] - 2 * sequencia3[-2] + sequencia3[-3])
print(proximo_numero3)
#output: 100



#e) 1, 1, 2, 3, 5, 8, ____
n = 8
a,b = 0,1
for numero in range(n):
    print(a, end=" ")
    a,b=b,a+b
#output: 13 



#f) 2,10, 12, 16, 17, 18, 19, ____
sequencia5 = [2,10,12,16,17,18,19]
diferenca3 = [sequencia5[i] - sequencia5[i-1] for i in range(1, len(sequencia5))]
ultima_diferenca = diferenca3[-1]
proximo_numero4 = sequencia5[-1] + ultima_diferenca
print()
print(proximo_numero4)
#output: 20 