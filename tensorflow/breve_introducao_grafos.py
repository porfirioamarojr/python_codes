import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
#tarefas primarias
a = tf.constant(5)
b = tf.constant(3)
c = tf.constant(2)
#tarefas secundarias
d = tf.multiply(a,b)
e = tf.add(b,c)
#tarefa final
f = tf.subtract(d,e)

sess = tf.Session()
saida = sess.run(f)
sess.close()
print(saida)
