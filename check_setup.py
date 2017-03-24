import numpy as np
import scipy as sp
import matplotlib as mpl
import skimage
import sklearn
import dask
import tensorflow as tf
import keras
import notebook as nb

for module in (np, sp, mpl, nb, skimage, sklearn, dask, tf, keras):
    print(module.__name__.ljust(11), module.__version__)

