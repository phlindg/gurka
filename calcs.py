from deck import *
from gurka import *
from game import *
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.preprocessing import scale
def calc_winpercent(bw,bl):
    total_len = len(bw)+len(bl)
    win_percent_list = []
    for i in [2,3,4,5,6,7,8,9,10,11,12,13,15,16]:
        win_count = bw.count(i)
        loose_count = bl.count(i)
        print ("KORT VALUE: ", i, "  WC: ", win_count, "  LC: ", loose_count)
        win_percent_list.append(round(float(win_count)/float(total_len), 3))
    print( win_percent_list)
    return win_percent_list

def tensorstuff():
	#Get the data
	total_features, total_prices = load_boston(True)

	#Beholl 300 for training:
	train_features = scale(total_features[:300])
	train_prices = total_prices[:300]
	#beholl 100 for validation
	valid_features = scale(total_features[300:400])
	valid_prices = total_prices[300:400]
	#beholl resten som test
	test_features = scale(total_features[400:])
	test_prices = total_prices[400:]


	w = tf.Variable(tf.truncated_normal([13,1], mean=0.0, stddev=1.0, dtype = tf.float64))
	b = tf.Variable(tf.zeros(1, dtype = tf.float64))

	y,  cost = calc_pred_error(train_features, train_prices,b,w)
	learning_rate = 0.025
	epochs = 3000
	points = [[], []]
	init = tf.global_variables_initializer() #denna initsierar variablerna
	optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
	with tf.Session() as ses:
	 	ses.run(init)
	 	for i in list(range(epochs)):
	  		ses.run(optimizer)
	  		if i % 10 == 0.:
	  			points[0].append(i+1)
	  			points[1].append(ses.run(cost))
	  		if i % 100 == 0.:
	  			print(ses.run(cost))
		plt.plot(points[0], points[1], 'r--')
		plt.axis([0, epochs, 50, 600])
		plt.show()	

		valid_cost = calc_pred_error(valid_features, valid_prices,b,w)[1]

		print('Validation error =', sess.run(valid_cost), '\n')
		
		test_cost = calc_pred_error(test_features, test_prices,b, w)[1]
		#denna raden nedan gor man ner man tror att man e klar.
		# print('Test error =', sess.run(test_cost), '\n')
def calc_pred_error(x,y,b,w):
	#Returns predictions and error
	predictions = tf.add(b, tf.matmul(x,w))
	error = tf.reduce_mean(tf.square(y-predictions))
	return predictions, error

tensorstuff()


	