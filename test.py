import ImgUtilities as imgutil
from PIL import Image
import numpy as np

lena_gray = Image.open("testimg/lena_gray.jpg")
lena_color = Image.open("testimg/lena_color.gif")


#print imgutil.mse(lena_gray,lena_gray)
#print imgutil.psnr(lena_gray,lena_gray)
#print imgutil.ssim(lena_gray,lena_gray)

I = imgutil.extract_patches(lena_gray,(5,10),(1,2))


print I.shape
I = np.hstack(I[0:508])
#lena_gray.show()
Image.fromarray(I).show()
