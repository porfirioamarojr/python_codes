import ahpy

custo_comparisons  = {( 'Carro1' , 'Carro2' ): 7 }
conforto_comparisons  = {( 'Carro1' , 'Carro2' ): 1/5 }
seguranca_comparisons  = {( 'Carro1' , 'Carro2' ): 1/9 }
criteria_comparisons  = {( 'custo' , 'conforto' ): 7 , ( 'custo' , 'seguranca' ): 3 , ( 'conforto' , 'seguranca' ): 3 }

custo  =  ahpy.Compare ( 'custo' , custo_comparisons , precision=3, random_index='saaty')
conforto  =  ahpy.Compare ( 'conforto' , conforto_comparisons , precision=3, random_index='saaty')
seguranca  =  ahpy.Compare ('seguranca' , seguranca_comparisons , precision=3, random_index='saaty')
criteria  =  ahpy.Compare ( 'Critérios' , criteria_comparisons , precision=3, random_index='saaty')

criteria.add_children ([custo, conforto, seguranca])

print(custo.consistency_ratio)
print(custo.local_weights)

print(custo.global_weights)
print(conforto.weight)

print(conforto.consistency_ratio)
print(conforto.local_weights)

print(conforto.global_weights)
print(seguranca.weight)

print(seguranca.consistency_ratio)
print(seguranca.local_weights)

print(seguranca.global_weights)
print(criteria.target_weights)

# https://bpmsg.com/ahp/ahp-calc1.php?t=AHP+priorities&n=3&new=Go