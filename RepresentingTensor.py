#Use NumpPy matrices in Tensor Flow

import pip
pip.main(["install", "numpy"])
pip.main(["install","tensorflow"])

import numpy as np
import tensorflow as tf




#Defines two by two matrix
m1 = [[1.0,2.0],[3.0,4.0]]

m2 = np.array([[1.0,2.0],[3.0,4.0]], dtype=np.float32)

m3 = tf.constant([[1.0,2.0],[3.0,4.0]])

#Prints the type for each matrix
print(type(m1))
print(type(m2))
print(type(m3))


#Creates tensor objects out of the various types
t1 = tf.convert_to_tensor(m1, dtype=tf.float32)
t2 = tf.convert_to_tensor(m2, dtype=tf.float32)
t3 = tf.convert_to_tensor(m3, dtype=tf.float32)

#Notices same types will follow.
print(type(t1))
print(type(t2))
print(type(t3))

