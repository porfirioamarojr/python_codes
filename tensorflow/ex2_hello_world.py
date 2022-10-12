import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
frase = tf.constant('Hello world!')
#with tf.compat.v1.Session() as sess:
#   rodar = sess.run(frase)
print(tf.Session().run(frase).decode('UTF-8'))