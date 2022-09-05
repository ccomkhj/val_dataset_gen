"""
Return the generation process using meta data
"""

import glob
import os
import shutil

if __name__ == "__main__":
    parent_path = os.path.join(os.getcwd(),"species")
    path2meta = os.path.join(parent_path, 'meta', 'val.txt')

    """Find the classes of dataset"""
    path2classes = sorted(glob.glob(os.path.join(parent_path,'train',"*")))
    classes = [os.path.basename(i) for i in path2classes]

    print("Process starts.")
    print(f"classes: {classes}")

    with open(path2meta, 'r') as f:
        for line in f.readlines():
            f_name, idx = line.strip().split(' ')
            file2move = os.path.join(parent_path, 'val', f_name)
            file2save = os.path.join(parent_path, 'train', classes[int(idx)], f_name)

            shutil.move(file2move, file2save)

    print("Process is complete.")
