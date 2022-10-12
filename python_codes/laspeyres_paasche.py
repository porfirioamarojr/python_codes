import numpy as np

q = []
x = ''
while (x != '1') and (x != '2'):
	print("laspeyres 1 ou paasche 2?")
	x = input()

print("informe os periodos")
t = int(input())

for i in range(0,t):
   q.append(float(input()))
 
for i in range(0,t): 
	print(q[i])

