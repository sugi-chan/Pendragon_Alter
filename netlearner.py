from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import RMSprop,Adam
import numpy as np
import pandas as pd
from colosseum import team_chaldela
import itertools
from random import choice
from keras.models import load_model

def use_predicted_probability(predicted_classs):
	
	if predicted_classs == 0:
		hand_to_play = (0, 1, 2)
		
	elif predicted_classs == 1:
		hand_to_play = (0, 1, 3)
		
	elif predicted_classs == 2:
		hand_to_play = (0, 1, 4)
		
	elif predicted_classs == 3:
		hand_to_play = (0, 2, 1)
		
	elif predicted_classs == 4:
		hand_to_play = (0, 2, 3)
		
	elif predicted_classs == 5:
		hand_to_play = (0, 2, 4)
		
	elif predicted_classs == 6:
		hand_to_play = (0, 3, 1)
		
	elif predicted_classs == 7:
		hand_to_play = (0, 3, 2)
		
	elif predicted_classs == 8:
		hand_to_play = (0, 3, 4)
		
	elif predicted_classs == 9:
		hand_to_play = (0, 4, 1)
		
	elif predicted_classs == 10:
		hand_to_play = (0, 4, 2)
		
	elif predicted_classs == 11:
		hand_to_play = (0, 4, 3)
		
	elif predicted_classs == 12:
		hand_to_play = (1, 0, 2)
		
	elif predicted_classs == 13:
		hand_to_play = (1, 0, 3)
		
	elif predicted_classs == 14:
		hand_to_play = (1, 0, 4)
		
	elif predicted_classs == 15:
		hand_to_play = (1, 2, 0)
		
	elif predicted_classs == 16:
		hand_to_play = (1, 2, 3)
		
	elif predicted_classs == 17:
		hand_to_play = (1, 2, 4)
		
	elif predicted_classs == 18:
		hand_to_play = (1, 3, 0)
		
	elif predicted_classs == 19:
		hand_to_play = (1, 3, 2)
		
	elif predicted_classs == 20:
		hand_to_play = (1, 3, 4)
		
	elif predicted_classs == 21:
		hand_to_play = (1, 4, 0)
		
	elif predicted_classs == 22:
		hand_to_play = (1, 4, 2)
		
	elif predicted_classs == 23:
		hand_to_play = (1, 4, 3)
		
	elif predicted_classs == 24:
		hand_to_play = (2, 0, 1)
		
	elif predicted_classs == 25:
		hand_to_play = (2, 0, 3)
		
	elif predicted_classs == 26:
		hand_to_play = (2, 0, 4)
		
	elif predicted_classs == 27:
		hand_to_play = (2, 1, 0)
		
	elif predicted_classs == 28:
		hand_to_play = (2, 1, 3)
		
	elif predicted_classs == 29:
		hand_to_play = (2, 1, 4)
		
	elif predicted_classs == 30:
		hand_to_play = (2, 3, 0)
		
	elif predicted_classs == 31:
		hand_to_play = (2, 3, 1)
		
	elif predicted_classs == 32:
		hand_to_play = (2, 3, 4)
		
	elif predicted_classs == 33:
		hand_to_play = (2, 4, 0)
		
	elif predicted_classs == 34:
		hand_to_play = (2, 4, 1)
		
	elif predicted_classs == 35:
		hand_to_play = (2, 4, 3)
		
	elif predicted_classs == 36:
		hand_to_play = (3, 0, 1)
		
	elif predicted_classs == 37:
		hand_to_play = (3, 0, 2)
		
	elif predicted_classs == 38:
		hand_to_play = (3, 0, 4)
		
	elif predicted_classs == 39:
		hand_to_play = (3, 1, 0)
		
	elif predicted_classs == 40:
		hand_to_play = (3, 1, 2)
		
	elif predicted_classs == 41:
		hand_to_play = (3, 1, 4)
		
	elif predicted_classs == 42:
		hand_to_play = (3, 2, 0)
		
	elif predicted_classs == 43:
		hand_to_play = (3, 2, 1)
		
	elif predicted_classs == 44:
		hand_to_play = (3, 2, 4)
		
	elif predicted_classs == 45:
		hand_to_play = (3, 4, 0)
		
	elif predicted_classs == 46:
		hand_to_play = (3, 4, 1)
		
	elif predicted_classs == 47:
		hand_to_play = (3, 4, 2)
		
	elif predicted_classs == 48:
		hand_to_play = (4, 0, 1)
		
	elif predicted_classs == 49:
		hand_to_play = (4, 0, 2)
		
	elif predicted_classs == 50:
		hand_to_play = (4, 0, 3)
		
	elif predicted_classs == 51:
		hand_to_play = (4, 1, 0)
		
	elif predicted_classs == 52:
		hand_to_play = (4, 1, 2)
		
	elif predicted_classs == 53:
		hand_to_play = (4, 1, 3)
		
	elif predicted_classs == 54:
		hand_to_play = (4, 2, 0)
		
	elif predicted_classs == 55:
		hand_to_play = (4, 2, 1)
		
	elif predicted_classs == 56:
		hand_to_play = (4, 2, 3)
		
	elif predicted_classs == 57:
		hand_to_play = (4, 3, 0)
		
	elif predicted_classs == 58:
		hand_to_play = (4, 3, 1)
		
	else:
		hand_to_play = (4, 3, 2)
		
	return hand_to_play

def random_pick_cards():
    list1= list(itertools.permutations([0,1,2,3,4],3))
    hand = choice(list1)
    return hand

def convert_card_list(card_list_input):
	out_array = []
	for card in card_list_input:
		if card== 'buster':
			out_array.append(1)

		if card== 'arts':
			out_array.append(2)
		if card== 'quick':
			out_array.append(3)
	#print('outarray: ',out_array)
	out_array2 = np.reshape(np.asarray(out_array), (1, 5))
	return 	out_array2

class DQNLearner(team_chaldela):
	def __init__(self):
		super().__init__()
		self._learning = True
		self._learning_rate = .1
		self._discount = .1
		self._epsilon = .9

		# Create Model
		# as of 9/17 best model is the 5-64-128 layer mlp. 
		# may try lstm as stated before
		#this network may work better as a LSTM.... 
		#input is a len 5 array of quick arts and buster... that I probably have to one hot encode
		model = Sequential()

		model.add(Dense(5, init='glorot_normal', activation = 'relu', input_dim=5))

		model.add(Dense(64, init='glorot_normal', activation = 'relu'))
		model.add(Dense(128, init='glorot_normal', activation = 'relu'))
		model.add(Dense(128, init='glorot_normal', activation = 'relu'))
		#output in this case should be a 60 way classification
		#representing the 60 ways you can choose 3 cards out of 5

		model.add(Dense(60, init='glorot_normal',activation='linear'))

		opt = RMSprop()
		model.compile(loss='mse', optimizer=opt)

		self._model = model



	'''
	for me state is going to be the 5 cards that are delt. 
	need to convert it into an array to be fed into the model... lets use keras cuz why not...

	then test against _epsilon the same way as listed here

	else randomly pick between 1 of the 60 permutaions of 5P3 
	'''
	def get_action(self, state):
		#need to modify the way that it does the prediction.... 
		#print(state.shape)
		#print(convert_card_list(state),convert_card_list(state).shape,type(convert_card_list(state)))

		rewards = self._model.predict(convert_card_list(state), batch_size=1)

		predicted_classs = np.argmax(rewards)
		#print('class', predicted_classs, rewards.shape)
		#print('looking at weird thing',rewards[0][0],rewards[0][1],rewards)
		# can probably solve using a mapping of the actions and just outputing the label of the max of the chain
		if np.random.uniform(0,1) < self._epsilon:
			#get argmax of 60 way classification array
			# see use_predicted_probability() in choice testing notebook
			action = use_predicted_probability(predicted_classs)

		else:
			#if above the epsilon value, then choose one of 60
			# see picked_cards() in battle_prototype
			action = random_pick_cards() #i can generate the permutations and throw the list in here

		self._last_state = convert_card_list(state)
		self._last_action = action
		self._last_target = rewards


		return action
	
	def update(self,new_state,reward):
		if self._learning:
			rewards = self._model.predict([convert_card_list(new_state)], batch_size=1)
			maxQ = np.amax(rewards)
			new = self._discount * maxQ
			
			#### This looks annoying AF... 
			if self._last_action == (0, 1, 2):
				self._last_target[0][0] = reward+new

			elif self._last_action == (0, 1, 3):
				self._last_target[0][1] = reward+new

			elif self._last_action == (0, 1, 4):
				self._last_target[0][2] = reward+new

			elif self._last_action == (0, 2, 1):
				self._last_target[0][3] = reward+new

			elif self._last_action == (0, 2, 3):
				self._last_target[0][4] = reward+new

			elif self._last_action == (0, 2, 4):
				self._last_target[0][5] = reward+new

			elif self._last_action == (0, 3, 1):
				self._last_target[0][6] = reward+new

			elif self._last_action == (0, 3, 2):
				self._last_target[0][7] = reward+new

			elif self._last_action == (0, 3, 4):
				self._last_target[0][8] = reward+new

			elif self._last_action == (0, 4, 1):
				self._last_target[0][9] = reward+new

			elif self._last_action == (0, 4, 2):
				self._last_target[0][10] = reward+new

			elif self._last_action == (0, 4, 3):
				self._last_target[0][11] = reward+new

			elif self._last_action == (1, 0, 2):
				self._last_target[0][12] = reward+new

			elif self._last_action == (1, 0, 3):
				self._last_target[0][13] = reward+new

			elif self._last_action == (1, 0, 4):
				self._last_target[0][14] = reward+new

			elif self._last_action == (1, 2, 0):
				self._last_target[0][15] = reward+new

			elif self._last_action == (1, 2, 3):
				self._last_target[0][16] = reward+new

			elif self._last_action == (1, 2, 4):
				self._last_target[0][17] = reward+new

			elif self._last_action == (1, 3, 0):
				self._last_target[0][18] = reward+new

			elif self._last_action == (1, 3, 2):
				self._last_target[0][19] = reward+new

			elif self._last_action == (1, 3, 4):
				self._last_target[0][20] = reward+new

			elif self._last_action == (1, 4, 0):
				self._last_target[0][21] = reward+new

			elif self._last_action == (1, 4, 2):
				self._last_target[0][22] = reward+new

			elif self._last_action == (1, 4, 3):
				self._last_target[0][23] = reward+new

			elif self._last_action == (2, 0, 1):
				self._last_target[0][24] = reward+new

			elif self._last_action == (2, 0, 3):
				self._last_target[0][25] = reward+new

			elif self._last_action == (2, 0, 4):
				self._last_target[0][26] = reward+new

			elif self._last_action == (2, 1, 0):
				self._last_target[0][27] = reward+new

			elif self._last_action == (2, 1, 3):
				self._last_target[0][28] = reward+new

			elif self._last_action == (2, 1, 4):
				self._last_target[0][29] = reward+new

			elif self._last_action == (2, 3, 0):
				self._last_target[0][30] = reward+new

			elif self._last_action == (2, 3, 1):
				self._last_target[0][31] = reward+new

			elif self._last_action == (2, 3, 4):
				self._last_target[0][32] = reward+new

			elif self._last_action == (2, 4, 0):
				self._last_target[0][33] = reward+new

			elif self._last_action == (2, 4, 1):
				self._last_target[0][34] = reward+new

			elif self._last_action == (2, 4, 3):
				self._last_target[0][35] = reward+new

			elif self._last_action == (3, 0, 1):
				self._last_target[0][36] = reward+new

			elif self._last_action == (3, 0, 2):
				self._last_target[0][37] = reward+new

			elif self._last_action == (3, 0, 4):
				self._last_target[0][38] = reward+new

			elif self._last_action == (3, 1, 0):
				self._last_target[0][39] = reward+new

			elif self._last_action == (3, 1, 2):
				self._last_target[0][40] = reward+new

			elif self._last_action == (3, 1, 4):
				self._last_target[0][41] = reward+new

			elif self._last_action == (3, 2, 0):
				self._last_target[0][42] = reward+new

			elif self._last_action == (3, 2, 1):
				self._last_target[0][43] = reward+new

			elif self._last_action == (3, 2, 4):
				self._last_target[0][44] = reward+new

			elif self._last_action == (3, 4, 0):
				self._last_target[0][45] = reward+new

			elif self._last_action == (3, 4, 1):
				self._last_target[0][46] = reward+new

			elif self._last_action == (3, 4, 2):
				self._last_target[0][47] = reward+new

			elif self._last_action == (4, 0, 1):
				self._last_target[0][48] = reward+new

			elif self._last_action == (4, 0, 2):
				self._last_target[0][49] = reward+new

			elif self._last_action == (4, 0, 3):
				self._last_target[0][50] = reward+new

			elif self._last_action == (4, 1, 0):
				self._last_target[0][51] = reward+new

			elif self._last_action == (4, 1, 2):
				self._last_target[0][52] = reward+new

			elif self._last_action == (4, 1, 3):
				self._last_target[0][53] = reward+new

			elif self._last_action == (4, 2, 0):
				self._last_target[0][54] = reward+new

			elif self._last_action == (4, 2, 1):
				self._last_target[0][55] = reward+new

			elif self._last_action == (4, 2, 3):
				self._last_target[0][56] = reward+new

			elif self._last_action == (4, 3, 0):
				self._last_target[0][57] = reward+new

			elif self._last_action == (4, 3, 1):
				self._last_target[0][58] = reward+new

			else:
				self._last_target[0][59] = reward+new

			#print('last_state', self._last_state[0])
			# Update model
			self._model.fit(self._last_state, self._last_target, batch_size=1, epochs=1, verbose=0)
	
	def save_rl_model(self,name_model):
		self._model.save(str(name_model)+'.h5')


	
