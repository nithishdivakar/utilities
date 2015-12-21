from PIL import Image
import numpy as np

#from ImgUtilities.error import mse
#from ImgUtilities.error import psnr
#from ImgUtilities.error import ssim

from ImgUtilities import similarity as E
from ImgUtilities import patches as P

lena_gray = Image.open("testimg/lena_gray.jpg")
lena_color = Image.open("testimg/lena_color.gif")

pat1 = P.list_patches(lena_gray,(11,11),1)
print pat1.shape
pat2 = P.deconvolve_patches(lena_gray,(11,11),1)
print pat2.shape
pat3 = P.list_to_deconvolve(pat1,(pat2.shape[0],pat2.shape[1]))
pat4 = P.list_to_explode(pat1,(pat2.shape[0],pat2.shape[1]))
pat5 = P.explode_patches(lena_gray,(11,11),1)

print pat2.shape
print pat3.shape

print np.array_equal(pat2,pat3)
print np.array_equal(pat4,pat5)


print E.mse(lena_gray,lena_gray)
print E.psnr(lena_gray,lena_gray)
print E.ssim(lena_gray,lena_gray)

