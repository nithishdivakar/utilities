import numpy as np


def entropy(signal):
    '''
       copied and modified from https://www.hdm-stuttgart.de/~maucher/Python/MMCodecs/html/basicFunctions.html
    '''
    signal = signal.reshape(signal.size)
    '''
    function returns entropy of a signal
    signal must be a 1-D numpy array
    '''
    lensig=signal.size
    symset=list(set(signal))
    numsym=len(symset)
    propab=[np.size(signal[signal==i])/(1.0*lensig) for i in symset]
    ent=np.sum([p*np.log2(1.0/p) for p in propab])
    return ent
