import ahpy

preco_comparisons  = {( 'Casa1' , 'Casa2' ): 7 , ( 'Casa1' , 'Casa3' ): 9 , ( 'Casa2' , 'Casa3' ): 5 }
local_comparisons  = { ( 'Casa1' , 'Casa2' ): 5 , ( 'Casa1' , 'Casa3' ): 1 / 9 , ( 'Casa2' , 'Casa3' ):3 }
quarto_comparisons  = {( 'Casa1' , 'Casa2' ): 1/7 , ( 'Casa1' , 'Casa3' ): 3 , ( 'Casa2' , 'Casa3' ): 5 }
garagem_comparisons  = {( 'Casa1' , 'Casa2' ): 1 / 5 , ( 'Casa1' , 'Casa3' ): 5 , ( 'Casa2' , 'Casa3' ): 7 }

criteria_comparisons  = {( 'Preco' , 'Local' ): 3 , ( 'Preco' , 'Quarto' ): 5 , ( 'Preco' , 'Garagem' ): 9 ,
( 'Local' , 'Quarto' ): 3 , ( 'Local' , 'Garagem' ): 7 ,
( 'Quarto' , 'Garagem' ): 3 }
preco  =  ahpy . Compare ( 'Preco' , preco_comparisons , precision=3, random_index='saaty')
local  =  ahpy . Compare ( 'Local' , local_comparisons , precision=3, random_index='saaty')
quarto  =  ahpy . Compare ('Quarto' , quarto_comparisons , precision=3, random_index='saaty')
garagem  =  ahpy . Compare ( 'Garagem' , garagem_comparisons , precision=3, random_index='saaty')
criteria  =  ahpy . Compare ( 'Critérios' , criteria_comparisons , precision=3, random_index='saaty')
criteria . add_children ([ preco , local , quarto , garagem ])
print (criteria.target_weights)
print(preco.weight)

print(preco.consistency_ratio)

print(preco.local_weights)

print(preco.global_weights)
print(local.weight)

print(local.consistency_ratio)

print(local.local_weights)

print(local.global_weights)
print(quarto.weight)

print(quarto.consistency_ratio)

print(quarto.local_weights)

print(quarto.global_weights)
print(garagem.weight)

print(garagem.consistency_ratio)

print(garagem.local_weights)

print(garagem.global_weights)