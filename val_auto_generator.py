"""
Generate validation files from training folders
"""

import glob
import os
import random
import shutil

if __name__ == "__main__":
    parent_path = os.path.join(os.getcwd(),"species")
    path2meta = os.path.join(parent_path, 'meta')
    RATIO_VAL = 0.1
    
    print("Process starts.")

    """Find the classes of dataset"""
    path2classes = sorted(glob.glob(os.path.join(parent_path,'train',"*")))
    classes = [os.path.basename(i) for i in path2classes]
    
    print(f"classes: {classes}")

    """Create meta for validation dataset"""
    txt = open(os.path.join(path2meta,'val.txt'), 'w') 

    for idx, path2class in enumerate(path2classes):
        images = glob.glob(os.path.join(path2class,"*"))
        num_sample = len(images)
        val_images = random.sample(images, int(num_sample*RATIO_VAL))
        for val_image in val_images:
            f_name = os.path.basename(val_image)
            file2save = os.path.join(parent_path,'val',f_name)
            shutil.move(val_image, file2save)
            txt.write(f"{f_name} {idx}")
            txt.write("\n")

    txt.close()

    print("Process is done.")
