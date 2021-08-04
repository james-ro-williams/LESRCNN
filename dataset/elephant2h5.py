import os
import glob
import h5py
import scipy.misc as misc
import numpy as np

import imageio

dataset_dir_train= "/content/elephants/train/"
dataset_type = "train"

f = h5py.File("elephant_{}.h5".format(dataset_type), "w") #create a file with '.h5'
dt = h5py.special_dtype(vlen=np.dtype('uint8'))

for subdir in ["HR", "2x", "3x", "4x"]:
    im_paths = glob.glob(dataset_dir_train+subdir+'/*jpg')
        
    im_paths.sort()
    grp = f.create_group(subdir) #create a subgroup

    for i, path in enumerate(im_paths):
        im = imageio.imread(path)
        print(path)
        grp.create_dataset(str(i), data=im) #create_dataset