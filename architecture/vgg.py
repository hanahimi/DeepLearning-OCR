from keras.layers import Input, Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.models import Model
from keras.layers.normalization import BatchNormalization

def build_vgg_10(channels, width, height, output_size, nb_classes):
	# input
	inputs = Input(shape=(channels, height, width))
	# 1 conv
	conv1_1 = Convolution2D(64, 3, 3, border_mode='same', activation='relu', W_regularizer='l2')(inputs)
	conv1_2 = Convolution2D(64, 3, 3, border_mode='same', activation='relu', W_regularizer='l2')(conv1_1)
	bn1 = BatchNormalization(mode=0, axis=1)(conv1_2)
	pool1 = MaxPooling2D(pool_size=(2,2), strides=(2,2))(bn1)
	drop1 = Dropout(0.5)(pool1)
	# 2 conv
	conv2_1 = Convolution2D(128, 3, 3, border_mode='same', activation='relu', W_regularizer='l2')(drop1)
	conv2_2 = Convolution2D(128, 3, 3, border_mode='same', activation='relu', W_regularizer='l2')(conv2_1)
	bn2 = BatchNormalization(mode=0, axis=1)(conv2_2)
	pool2 = MaxPooling2D(pool_size=(2,2), strides=(2,2))(bn2)
	drop2 = Dropout(0.5)(pool2)
	# 3 conv
	conv3_1 = Convolution2D(256, 3, 3, border_mode='same', activation='relu', W_regularizer='l2')(drop2)
	conv3_2 = Convolution2D(256, 3, 3, border_mode='same', activation='relu', W_regularizer='l2')(conv3_1)
	conv3_3 = Convolution2D(256, 3, 3, border_mode='same', activation='relu', W_regularizer='l2')(conv3_2)
	bn3 = BatchNormalization(mode=0, axis=1)(conv3_3)
	pool3 = MaxPooling2D(pool_size=(2,2), strides=(2,2))(bn3)
	drop3 = Dropout(0.5)(pool3)
	# # 4 conv
	# conv4_1 = Convolution2D(512, 3, 3, border_mode='same', activation='relu')(drop3)
	# conv4_2 = Convolution2D(512, 3, 3, border_mode='same', activation='relu')(conv4_1)
	# conv4_3 = Convolution2D(512, 3, 3, border_mode='same', activation='relu')(conv4_2)
	# bn4 = BatchNormalization(mode=0, axis=1)(conv4_3)
	# pool4 = MaxPooling2D(pool_size=(2,2), strides=(2,2))(bn4)
	# drop4 = Dropout(0.5)(pool4)
	# # 5 conv
	# conv5_1 = Convolution2D(512, 3, 3, border_mode='same', activation='relu')(drop4)
	# conv5_2 = Convolution2D(512, 3, 3, border_mode='same', activation='relu')(conv5_1)
	# conv5_3 = Convolution2D(512, 3, 3, border_mode='same', activation='relu')(conv5_2)
	# bn5 = BatchNormalization(mode=0, axis=1)(conv5_3)
	# pool5 = MaxPooling2D(pool_size=(2,2), strides=(2,2))(bn5)
	# drop5 = Dropout(0.5)(pool5)
	# flaten
	flat = Flatten()(drop3)
	# 1 dense
	dense1 = Dense(4096, activation='relu', W_regularizer='l2')(flat)
	bn6 = BatchNormalization(mode=0, axis=1)(dense1)
	drop6 = Dropout(0.5)(bn6)
	# 2 dense
	dense2 = Dense(4096, activation='relu', W_regularizer='l2')(drop6)
	bn7 = BatchNormalization(mode=0, axis=1)(dense2)
	drop7 = Dropout(0.5)(bn7)
	# output
	out = range(output_size)
	# out[0] = Dense(output_size, activation='softmax')(drop7)
	for i in range(output_size):
		out[i] = Dense(nb_classes, activation='softmax')(drop7)

	model = Model(input=[inputs], output=out)
	model.summary()
	model.compile(loss='categorical_crossentropy',
				  optimizer='adam',
				  metrics=['accuracy'],
				  )

	return model