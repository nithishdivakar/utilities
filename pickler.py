#!/usr/bin/env python
'''
A small script to convert dataset to pickle format file
'''
__author__ = "Nithish Divakar"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["", ""]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Nithish Divakar"
__email__ = "nithish.divakar@gmail.com"
__status__ = "Testing"

try:
	import cPickle as pickle
except:
	import pickle

import numpy
import os
from PIL import Image


# modify these 3 things to suit ur need
test_dir_path  = "BSDS300/images/test"
train_dir_path = "BSDS300/images/test"
op_file_name   = "BSDS.pkl"


# modify this funciton to do some processing
# on images immedately after they are read
# should return a list even if it is just one image
# an example would be to convert each image to a numpy array
# or extract patches in each image
def transform_image(im): # transform image immediately after reading
	lis = []
	lis.append( im.convert('LA')) # Ex: convert everything to grayscale
	return lis

def path_sanitiser(path):
	if path.endswith("/"):
		return path
	else:
		return path+"/"


def read_images(path):
	images = os.listdir(path)
	IMG = []
	for img_name in images:
		im = Image.open(test_dir_path+img_name)
		im_list = transform_image(im) # function to be applied to each image
		for i in im_list:
			IMG.append(i)
	return IMG


def main():
	global test_dir_path,train_dir_path
	train_dir_path = path_sanitiser(train_dir_path)
	test_dir_path  = path_sanitiser(test_dir_path)
	test_images	= read_images(train_dir_path)
	train_set	  = read_images(train_dir_path)
	test_set	   = read_images(test_dir_path)
	pickle.dump((train_set , test_set ),open(op_file_name,"wb"))
	print("Done !!")


if __name__ == "__main__":
	main()
