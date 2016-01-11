from PIL import Image
import numpy
from skimage.util import shape as skshape
import padding 
from itertools import product


def patch_dimen(patch_radius):
	if len(patch_radius)==1:
		patch_shape = (2*patch_radius+1,2*patch_radius+1)
	else:
		patch_shape = (2*patch_radius[0]+1,2*patch_radius[1]+1)
	return patch_shape

def convert(source_format,target_format,input_datum,**kwargs):
	method_dicnry={
		'patch-image': convert_patch_image,
		'image-patch': convert_image_patch,
	}
	# ToDO: check error
	return method_dicnry[source_format+"-"+target_format](input_datum,**kwargs)



def convert_image_patch(input_datum,patch_radius,stride=(1,1),pad=True):
	img = numpy.array(input_datum)
	if pad == True:
		img = padding.pad_symmetric(img,patch_radius)
	patch_shape = patch_dimen(patch_radius)
	patches = skshape.view_as_windows(img,window_shape = patch_shape,step = stride)
	patches = numpy.concatenate(patches,axis = 0)
	return patches

def convert_patch_image(input_datum,image_size,stride=(1,1),pad=True):
	patches = input_datum
	patch_shape = patches[0].shape
	if pad == True:
		outpt_shape = (image_size[0] + patch_shape[0]-1, image_size[1] + patch_shape[1]-1)
	else:
		outpt_shape = image_size

	image = numpy.zeros(outpt_shape)
	weigh = numpy.zeros(outpt_shape)
	k = 0
	for coord in product( xrange(0,outpt_shape[1]-patch_shape[1]+1,stride[1]), xrange(0,outpt_shape[0]-patch_shape[0]+1,stride[0])):
		#print k," ",
		image[coord[0]:coord[0]+patch_shape[0],coord[1]:coord[1]+patch_shape[1]] += patches[k]
		weigh[coord[0]:coord[0]+patch_shape[0],coord[1]:coord[1]+patch_shape[1]] += 1.0
		k    = k+1
	image = image/weigh
	if pad == True:
		image = image[
		       ((patch_shape[0]-1)/2):((patch_shape[0]-1)/2) + image_size[0],
		       ((patch_shape[1]-1)/2):((patch_shape[1]-1)/2) + image_size[1]
		]
	return image
	
