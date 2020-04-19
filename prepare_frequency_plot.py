# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:38:31 2020

@author: Meet
"""

import glob
from tqdm import tqdm
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

dataset_path = "./PASCAL/VOC2012_trainval/"
files_12 = glob.glob(dataset_path + "/Annotations/*.xml")

dataset_path = "./PASCAL/VOC2007_trainval/"
files_07 = glob.glob(dataset_path + "/Annotations/*.xml")

combined_files = []
combined_files.extend(files_12)
combined_files.extend(files_07)

print(len(combined_files))

class_dist = dict()

for f in tqdm(combined_files):
    tree = ET.parse(f)
    root = tree.getroot()
    
    for item in root.findall("object"):
        objName = item.find("name").text        
        xmin = int(float(item.find("bndbox").find("xmin").text))     # In the original range of image
        ymin = int(float(item.find("bndbox").find("ymin").text))     # In the original range of image
        xmax = int(float(item.find("bndbox").find("xmax").text))     # In the original range of image
        ymax = int(float(item.find("bndbox").find("ymax").text))     # In the original range of image

        if objName not in list(class_dist.keys()):
            class_dist[objName] = 1
        else:
            class_dist[objName] += 1

print(class_dist)

# ===================== Plot frequency distribution ===================== #
plt.figure(figsize=(10, 10))
plt.bar(list(class_dist.keys()), list(class_dist.values()))
plt.xlabel("Class names")
plt.ylabel("Frequency")
plt.xticks(rotation=90)
plt.title("Frequency distribution of VOC 07+12 trainval dataset", fontdict={'fontsize':20})
plt.savefig("voc_07+12.png")
plt.plot()
# ======================================================================= #

with open('freq_dist.txt', 'w') as f:
    for cls_name, freq in class_dist.items():
        f.write(cls_name + " " + str(freq) + "\n")
        

