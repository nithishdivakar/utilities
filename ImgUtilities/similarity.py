from PIL import Image
import numpy as np
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

