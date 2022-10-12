import numpy as np
from scipy.optimize import linprog

obj = [-3,-4] #Contém os coeficientes da função objetivo.
lhs_ineq = [[1, 0],[0,1],[1,1]]#Contém os coeficientes do lado esquerdo das restrições de desigualdade
rhs_ineq = [29,10,35] #Contém os coeficientes do lado direito das restrições de desigualdade 
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="revised simplex")
#Função que realiza o calculo do metodo simplex

print('Solução Ótima:', opt.fun, '\nX:', opt.x)

#x é uma matriz NumPy contendo os valores ideais das variáveis ​​de decisão.
#fun é o valor da função objetivo no nível ideal (se encontrado).

#https://realpython.com/linear-programming-python/
#http://www.phpsimplex.com/simplex/solucion.php?l=pt