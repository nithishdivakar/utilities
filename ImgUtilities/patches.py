from PIL import Image
import numpy as np
from skimage.util import shape as skshape

	
def deconvolve_patches(img,patch_shape,stride):
	img = np.array(img)
	patches = skshape.view_as_windows(img, window_shape=patch_shape,step = stride)
	return patches

def extract_patches(img,patch_shape,stride):
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
