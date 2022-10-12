import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

a = tf.constant(2) #1x1 - zero dimensional - zero linha/colunas
b = tf.constant([3,1,5,8,6]) #1xn - dimensional - 1 linha 
c = tf.constant([[2, 0, 4], [3, 5, 7]]) #nxn - matriz - 3 linhas/colunas

sess = tf.Session()
saida = sess.run(c)
sess.close()

#############################################
import numpy as np

a1 = np.array(2)
b1 = np.array([3,1,5,8,6])
c1 = np.array([[2,0,4], [3,5,7]])

#############################################
print(c.shape)

#############################################
print(c1.shape)

#Declaração de tipo de Tensor
const = tf.constant(4.0) #Outra maneira .constant(4, dtype=tf.float64)
print(const)