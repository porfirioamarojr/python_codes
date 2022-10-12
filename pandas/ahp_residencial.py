import pandas as pd

#Matriz de compapração por pares
diag=1
preco_local=3
preco_quart=5
preco_garag=9
local_quart=3
local_garag=7
quart_garag=3

inv_preco_local=1/preco_local   
inv_preco_quart=1/preco_quart       
inv_preco_garag=1/preco_garag
inv_local_quart=1/local_quart 
inv_local_garag=1/local_garag 
inv_quart_garag=1/quart_garag     

matriz_ini={
    'preco':{'preco':diag,'local':preco_local,'quart':preco_quart,'garag':preco_garag},
    'local':{'preco':inv_preco_local,'local':diag,'quart':local_quart,'garag':local_garag},
    'quart':{'preco':inv_preco_quart,'local':inv_local_quart,'quart':diag,'garag':quart_garag},
    'garag':{'preco':inv_preco_garag,'local':inv_local_garag,'quart':inv_quart_garag,'garag':diag}

}

ahp_passo_1=pd.DataFrame(matriz_ini)

print(ahp_passo_1)
print()
ahp_passo_1=ahp_passo_1.T

print()
print(ahp_passo_1)
print()

ahp_passo_1_a=ahp_passo_1.sum()

print()
print(ahp_passo_1_a)
print()

ahp_passo_1_a=pd.DataFrame(ahp_passo_1_a)
ahp_passo_1_a=ahp_passo_1_a.T

ahp_passo_1_b=ahp_passo_1.div(ahp_passo_1_a.iloc[0])

print()
print(ahp_passo_1_b)
print()

ahp_passo_1_c=ahp_passo_1_b.mean(axis=1)
ahp_passo_1_c=pd.DataFrame(ahp_passo_1_c)
ahp_passo_1_c=ahp_passo_1_c.T

print("Printando a prioridade final")
print(ahp_passo_1_c)
print()

#Cálulo de consistencia
lambda_max=(ahp_passo_1_a*ahp_passo_1_c)
lambda_max=lambda_max.sum(axis=1)

cc=((lambda_max-4)/3)/0.9

print()
print(cc)

################################# CÁLCULO DAS PRIORIDADES DAS ALTERNATIVAS #################################
# PARA PREÇO:
casa1_casa2=5
casa1_casa3=7
casa2_casa3=3

inv_casa1_casa2=1/casa1_casa2
inv_casa1_casa3=1/casa1_casa3
inv_casa2_casa3=1/casa2_casa3

preco_matriz_ini={
    'casa1':{'casa1':diag,'casa2':casa1_casa2,'casa3':casa1_casa3},
    'casa2':{'casa1':inv_casa1_casa2,'casa2':diag,'casa3':casa2_casa3},
    'casa3':{'casa1':inv_casa1_casa3,'casa2':inv_casa2_casa3,'casa3':diag},

}

preco_ahp_passo_1=pd.DataFrame(preco_matriz_ini)
preco_ahp_passo_1=preco_ahp_passo_1.T

preco_ahp_passo_1_a=preco_ahp_passo_1.sum()
preco_ahp_passo_1_a=pd.DataFrame(preco_ahp_passo_1_a)
preco_ahp_passo_1_a=preco_ahp_passo_1_a.T

preco_ahp_passo_1_b=preco_ahp_passo_1.div(preco_ahp_passo_1_a.iloc[0])

preco_ahp_passo_1_c=preco_ahp_passo_1_b.mean(axis=1)
preco_ahp_passo_1_c=pd.DataFrame(preco_ahp_passo_1_c)
col_preco = preco_ahp_passo_1_c
preco_ahp_passo_1_c=preco_ahp_passo_1_c.T

print("Printando a prioridade final")
print(col_preco)
print()


#Cálulo de consistencia
preco_lambda_max=(preco_ahp_passo_1_a*preco_ahp_passo_1_c)
preco_lambda_max=preco_lambda_max.sum(axis=1)

preco_cc=((preco_lambda_max-3)/2)/0.58

print(preco_cc)

################################# CÁLCULO DAS PRIORIDADES DAS ALTERNATIVAS #################################
# PARA LOCALIZAÇÃO:
casa1_casa2=5
casa1_casa3=1/7
casa2_casa3=3

inv_casa1_casa2=1/casa1_casa2
inv_casa1_casa3=7
inv_casa2_casa3=1/casa2_casa3

localizacao_matriz_ini={
    'casa1':{'casa1':diag,'casa2':casa1_casa2,'casa3':casa1_casa3},
    'casa2':{'casa1':inv_casa1_casa2,'casa2':diag,'casa3':casa2_casa3},
    'casa3':{'casa1':inv_casa1_casa3,'casa2':inv_casa2_casa3,'casa3':diag},

}

localizacao_ahp_passo_1=pd.DataFrame(localizacao_matriz_ini)
localizacao_ahp_passo_1=localizacao_ahp_passo_1.T

localizacao_ahp_passo_1_a=localizacao_ahp_passo_1.sum()
localizacao_ahp_passo_1_a=pd.DataFrame(localizacao_ahp_passo_1_a)
localizacao_ahp_passo_1_a=localizacao_ahp_passo_1_a.T

localizacao_ahp_passo_1_b=localizacao_ahp_passo_1.div(localizacao_ahp_passo_1_a.iloc[0])

localizacao_ahp_passo_1_c=localizacao_ahp_passo_1_b.mean(axis=1)
localizacao_ahp_passo_1_c=pd.DataFrame(localizacao_ahp_passo_1_c)
col_localizacao = localizacao_ahp_passo_1_c
localizacao_ahp_passo_1_c=localizacao_ahp_passo_1_c.T

print("Printando a prioridade final")
print(localizacao_ahp_passo_1_c)
print()

#Cálulo de consistencia
localizacao_lambda_max=(localizacao_ahp_passo_1_a*localizacao_ahp_passo_1_c)
localizacao_lambda_max=localizacao_lambda_max.sum(axis=1)

localizacao_cc=((localizacao_lambda_max-3)/2)/0.58

print(localizacao_cc)

################################# CÁLCULO DAS PRIORIDADES DAS ALTERNATIVAS #################################
# PARA QUARTOS:
casa1_casa2=1/7
casa1_casa3=3
casa2_casa3=5

inv_casa1_casa2=7
inv_casa1_casa3=1/casa1_casa3
inv_casa2_casa3=1/casa2_casa3

quartos_matriz_ini={
    'casa1':{'casa1':diag,'casa2':casa1_casa2,'casa3':casa1_casa3},
    'casa2':{'casa1':inv_casa1_casa2,'casa2':diag,'casa3':casa2_casa3},
    'casa3':{'casa1':inv_casa1_casa3,'casa2':inv_casa2_casa3,'casa3':diag},

}

quartos_ahp_passo_1=pd.DataFrame(quartos_matriz_ini)
quartos_ahp_passo_1=quartos_ahp_passo_1.T

quartos_ahp_passo_1_a=quartos_ahp_passo_1.sum()
quartos_ahp_passo_1_a=pd.DataFrame(quartos_ahp_passo_1_a)
quartos_ahp_passo_1_a=quartos_ahp_passo_1_a.T

quartos_ahp_passo_1_b=quartos_ahp_passo_1.div(quartos_ahp_passo_1_a.iloc[0])

quartos_ahp_passo_1_c=quartos_ahp_passo_1_b.mean(axis=1)
quartos_ahp_passo_1_c=pd.DataFrame(quartos_ahp_passo_1_c)
col_quartos = quartos_ahp_passo_1_c
quartos_ahp_passo_1_c=quartos_ahp_passo_1_c.T

print("Printando a prioridade final")
print(quartos_ahp_passo_1_c)
print()

#Cálulo de consistencia
quartos_lambda_max=(quartos_ahp_passo_1_a*quartos_ahp_passo_1_c)
quartos_lambda_max=quartos_lambda_max.sum(axis=1)
quartos_cc=((quartos_lambda_max-3)/2)/0.58

print(quartos_cc)

################################# CÁLCULO DAS PRIORIDADES DAS ALTERNATIVAS #################################
# PARA Garagem:
casa1_casa2=1/7
casa1_casa3=3
casa2_casa3=5

inv_casa1_casa2=7
inv_casa1_casa3=1/casa1_casa3
inv_casa2_casa3=1/casa2_casa3

garagem_matriz_ini={
    'casa1':{'casa1':diag,'casa2':casa1_casa2,'casa3':casa1_casa3},
    'casa2':{'casa1':inv_casa1_casa2,'casa2':diag,'casa3':casa2_casa3},
    'casa3':{'casa1':inv_casa1_casa3,'casa2':inv_casa2_casa3,'casa3':diag},

}

garagem_ahp_passo_1=pd.DataFrame(garagem_matriz_ini)
garagem_ahp_passo_1=garagem_ahp_passo_1.T

garagem_ahp_passo_1_a=garagem_ahp_passo_1.sum()
garagem_ahp_passo_1_a=pd.DataFrame(garagem_ahp_passo_1_a)
garagem_ahp_passo_1_a=garagem_ahp_passo_1_a.T

garagem_ahp_passo_1_b=garagem_ahp_passo_1.div(garagem_ahp_passo_1_a.iloc[0])

garagem_ahp_passo_1_c=garagem_ahp_passo_1_b.mean(axis=1)
garagem_ahp_passo_1_c=pd.DataFrame(garagem_ahp_passo_1_c)
col_garagem = garagem_ahp_passo_1_c
garagem_ahp_passo_1_c=garagem_ahp_passo_1_c.T

print("Printando a prioridade final")
print(garagem_ahp_passo_1_c)
print()

#Cálulo de consistencia
garagem_lambda_max=(garagem_ahp_passo_1_a*garagem_ahp_passo_1_c)
garagem_lambda_max=garagem_lambda_max.sum(axis=1)

garagem_cc=((garagem_lambda_max-3)/2)/0.58

print(garagem_cc)

#Matriz de prioridade finali



