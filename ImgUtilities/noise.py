from PIL import Image
import numpy as np


def add_gaussian_noise(img, sigma):
	img = np.array(img)
	return img + np.random.normal(0.0,sigma,img.shape)
