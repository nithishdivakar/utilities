from PIL import Image
import numpy as np
from skimage.util import shape as skshape

	
def deconvolve_patches(img,patch_shape,stride):
	img = np.array(img)
	patches = skshape.view_as_windows(img, window_shape=patch_shape,step = stride)
	return patches

def list_patches(img,patch_shape,stride):
	patches = deconvolve_patches(img,patch_shape,stride)
	pat = np.concatenate(patches,axis = 0)
	return pat

def explode_patches(img,patch_shape,stride):
	'''all rectangles are written as height x width'''
	patches = deconvolve_patches(img,patch_shape,stride)
	pat = []
	for x in xrange(patches.shape[0]):
		pat.append(np.hstack(patches[x]))
	pat = np.vstack(pat)
	return pat

def list_to_deconvolve(patches_train,shape):
	k = 0;
	pat_shape = patches_train[0].shape
	img_deconvolve = np.zeros((shape[0],shape[1],pat_shape[0],pat_shape[1]))
	for x in xrange(shape[0]):
		img_deconvolve[x,:] = patches_train[k:k+shape[1]]
		k = k+shape[0]
	return img_deconvolve

def deconvolve_to_explode(patches_deconv):
	pat = []
	for x in xrange(patches_deconv.shape[0]):
		pat.append(np.hstack(patches_deconv[x]))
	pat = np.vstack(pat)
	return pat

def list_to_explode(patches_train,shape):
	return deconvolve_to_explode(
	      list_to_deconvolve(patches_train,shape)
	)


def deconvolve_to_img(patches_deconv):
	imgsize = (patches_deconv.shape[0]+patches_deconv.shape[2],patches_deconv.shape[1]+patches_deconv.shape[3])
	W =np.zeros(imgsize)
	I =np.zeros(imgsize)
	for x in xrange(patches_deconv.shape[0]):
		for y in xrange(patches_deconv.shape[1]):
			I[x:x+11,y:y+11] += patches_deconv[x,y]
			W[x:x+11,y:y+11] += 1.0 
	I = I/W
	return I
