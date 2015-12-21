from PIL import Image
import numpy as np
from skimage.util import shape as skshape
import skimage.util as skutil
from skimage.measure import structural_similarity

	
def psnr(img1,img2,normalised = True):
	if normalised ==True:
		MAX = 1.0
	else:
		MAX = 255.0;
	MSE = mse(img1,img2)
	if MSE == 0.0:
		return np.inf
	return 20*np.log10(MAX/np.sqrt(MSE))

def mse(img1,img2):
	img1 = np.array(img1)
	img2 = np.array(img2)
	err  = np.sum((img1.astype("float") - img2.astype("float"))**2)
	err /= float(img1.shape[0] * img1.shape[1])
	return err

def ssim(img1,img2):
	img1 = np.array(img1)
	img2 = np.array(img2)
	return structural_similarity(img1,img2)



def pad_zeros(img,dim):
	img = np.array(img)
	return skutil.pad(img,pad_width = dim,mode='constant',constant_values=0.0)

def pad_symmetric(img,dim):
	img = np.array(img)
	return skutil.pad(img,pad_width = dim,mode='symmetric')


def extract_patches(img,patch_shape,stride):
	img = np.array(img)
	patches = skshape.view_as_windows(img, window_shape=patch_shape,step = stride)
	print patches.shape
	pat = np.concatenate(patches,axis = 0)
	return pat

def explode_patches(img,patch_shape,stride):
	'''all rectangles are written as height x width'''
	img = np.array(img)
	patches = skshape.view_as_windows(img, window_shape=patch_shape,step = stride)
	pat = []
	for x in xrange(patches.shape[0]):
		pat.append(np.hstack(patches[x]))
	pat = np.vstack(pat)
	return pat
