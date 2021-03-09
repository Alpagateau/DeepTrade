import numpy as np
from numpy import random as rng
import pygame
import sys
from pygame.locals import *
import matplotlib.pyplot as plt
import tensorflow as tf


model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])


model.load_weights("training_1/cp.ckpt")

pygame.init()

ScreenSize = (280,280)
Screen = pygame.display.set_mode(ScreenSize)

Input = np.zeros((28,28))

IsActive = True
while IsActive == True:
	Screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			x,y = pos
			x /= 10
			y /= 10
			x = int(np.floor(x))
			y = int(np.floor(y))
			Input[x][y] = 1
	for i in range(28):
		for j in range(28):
			pygame.draw.rect(Screen, (int(Input[i,j] * 255), int(Input[i,j] * 255), int(Input[i,j] * 255)), [i*10, j*10, 10,10])
	v = model.predict(Input.reshape((1, 28,28)))
	print(np.argmax(v))
	pygame.display.update()