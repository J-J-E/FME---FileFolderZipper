#-------------------------------------------------------------------------------
# Name:        quickZip.py
# Purpose: This module contains two functions for zipping directories and individual files
#
# Author:      John Ehlen
#
# Created:     10/09/2020
# Copyright:   (c) John Ehlen 2020
#-------------------------------------------------------------------------------

import os, zipfile

#Function to zip directory and maintain folder structure
def zipd(path):
    with zipfile.ZipFile(path+".zip", 'w', zipfile.ZIP_DEFLATED) as ziph:
        length = len(path)
        for root, dirs, files in os.walk(path):
            folder = root[length:]  # path without "parent"
            for file in files:
                ziph.write(os.path.join(root, file), os.path.join(folder, file))

#Functin to zip individual file
def zipF(path):
    ext = os.path.splitext(path)[1]
    basename = os.path.basename(path)
    zipf = path.replace(ext, ".zip")
    print(basename)
    with zipfile.ZipFile(zipf, 'w') as ziph:
        ziph.write(path, arcname=basename)
