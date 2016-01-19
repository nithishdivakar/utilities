import numpy


def normalize(image,maxim_value=255.0):
    image = numpy.asarray(image,dtype='float32')
    image = image / maxim_value  # range between +0.0 : +1.0
    image = image - 0.5          # range between -0.5 : +0.5
    image = image / 0.2          # range between -2.5 : +2.5
    # mean 0.0 SD 1.0
    return image

def denormalize(image,maxim_value = 255.0):
    image = numpy.asarray(image,dtype='float32')
    image = image * 0.2
    image = image + 0.5
    image = image * maxim_value
    return image
