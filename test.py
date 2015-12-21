from PIL import Image
import numpy as np

#from ImgUtilities.error import mse
#from ImgUtilities.error import psnr
#from ImgUtilities.error import ssim

from ImgUtilities import similarity_measures as E

lena_gray = Image.open("testimg/lena_gray.jpg")
lena_color = Image.open("testimg/lena_color.gif")


print E.mse(lena_gray,lena_gray)
print E.psnr(lena_gray,lena_gray)
print E.ssim(lena_gray,lena_gray)

