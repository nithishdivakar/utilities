from PIL import Image
import numpy as np
import skimage.util as skutil

def pad_zeros(img,dim):
	img = np.array(img)
	return skutil.pad(img,pad_width = dim,mode='constant',constant_values=0.0)

def pad_symmetric(img,dim):
	img = np.array(img)
	return skutil.pad(img,pad_width = dim,mode='symmetric')
