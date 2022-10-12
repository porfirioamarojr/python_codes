import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

a = tf.constant([[1,2,3], [4,5,6]])
b = tf.constant([[0,0], [1,0], [0,1]])
x = tf.constant([0, 1, 0]) #x = tf.constant([[0], [1], [0]])#/Outra forma de alcançar o resultado2 +


#Redimensionando matriz x
x = tf.expand_dims(x,1) # - sem prescisar dessa linha

resultado = tf.matmul(a,b)
resultado2 = tf.matmul(a,x)
transposta = tf.transpose(a)# transposta de a

print(tf.Session().run(resultado2))
print(tf.Session().run(transposta))