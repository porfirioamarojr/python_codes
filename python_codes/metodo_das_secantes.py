import math #Essa é a bibliotéca de matemática do python que carrega métodos com o de raiz quadrada e funções essênciais
import matplotlib.pyplot as plt #Bibliotéca para a criação de gráficos
import numpy as np #É usada principalmente para realizar cálculos em Arrays

def f(x): #Aqui é a declaração da função f(x)
  return(2*x*x + x + 4) # Essa linha retornará o resultado do cálculo da função
  #Exemplo para testar no lugar do cálculo função acima (x*x - x - 2)
  
x = [] #Declarando uma lista 'x' que irá guardar os valores do 'x' atual e o 'x' passado
xn = 0 #Inicializando 'xn' como '0'

tol = float(input("Entre com um valor real para tolerância/aproximação ou coloque o valor padrão 0.0000001: ")) #Nessa linha o usuário informa um valor real para a tolerância 'tol'
#O valor definido acima para 'tol' é o limite máximo de aproximação da raiz

n0 = int(input("Entre com o número de iterações/execuções desejado 'N0': "))
#Na linha acima a variavél 'N0' está recebendo um valor Inteiro e atráves de um Cast(uma conversão) feito na fução input para converter o valor recebido em um número inteiro
#'n0' corresponde ao número de iterações ou seja o valor máximo de vezes que a esturtura de repetição abaixo irá executar

a = float(input("Entre com o ponto 'a' do intervalo [a;b]: "))
#Na linha acima a variavél 'a' está recebendo um valor Real atráves de um Cast(uma conversão) feito na fução 'input' para converter o valor recebido em um número Real

b = float(input("Entre com o ponto 'b' do intervalo [a;b]: "))
#Na linha acima a variavél 'a' está recebendo um valor Real atráves de um 'Cast'(uma conversão) feito na fução 'input' para converter o valor recebido em um número Real

x.append(a)
#A função 'append' adiciona o valor recebido de 'a' na lista 'x'
x.append(b)
#A função 'append' adiciona o valor recebido de 'b' no vetor 'x'
#exemplo na posição 0 da lista 'x' vai ficar o valor de 'a' na posição 1 o valor de 'b' ex: 'x[a,b]'

n = 1 #Declarando um contador para verificar o número de iterações realizadas

while(math.fabs(f(xn)) > tol): #O método 'fabs' retornará o valor absoluto da função 'f(x)' enquanto for maior que a tolerância.
  #OBS-1: Se essa condição não encerrar o laço de repetição
  xn = x[n] - (x[n] - x[n - 1])/(f(x[n]) - f(x[n-1]))*f(x[n]) #Formulção do cálculo do método das secantes, realiza a aproximação da raiz
  x.append(xn) # Essa linha adiciona o valor de 'xn' recebido da linha acima na lista 'x'
  n = n + 1 #serve para controlar o número de vezes que a nossa estrutura de repetição 'while' irá executar
  
  if(n >= n0): #Essa condição é para parar o número de iterações quando 'i' for maior ou igual a 'n0' 
    #OBS-2: Obrigatóriamente essa condição encerra o laço de repetição
    break #O comando 'break' encerra o laço de repetição se a condição do 'while' não for satisfeita.

print("Raíz: {}\nIterações: {}\nf({}) = {}\n".format(xn,n,xn,f(xn)))
#Basicamente a função 'format' que já identifica os tipos das variáveis e os locais por ordem de prescedência ex '{a},{b},{c}'.format(a,b,c) 

plt.xlabel("Eixo X") #Define um nome para o eixo X
plt.ylabel("Eixo Y") # Define um nome para o eixo Y
plt.grid() #Corta o gráfico
xn = np.arange(-3,4, 0.1) #Essa linha com a linha de código abaixo
plt.plot(xn, f(xn)) #Geram os gráficos
plt.show() #Esse comando mostra o gŕafico para o usuário



