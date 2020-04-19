# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:26:43 2020

@author: Meet
"""

import cv2
import glob
import xml.etree.ElementTree as ET

dataset_path = "./PASCAL/VOC2012_trainval/"

files = glob.glob(dataset_path + "/Annotations/*.xml")
base_path = dataset_path + "/JPEGImages/"

f = files[42]

tree = ET.parse(f)
root = tree.getroot()
filename = root.find("filename").text

img = cv2.imread(base_path + filename)
h, w, _ = img.shape

for item in root.findall("object"):
    objName = item.find("name").text        
    xmin = int(float(item.find("bndbox").find("xmin").text))     # In the original range of image
    ymin = int(float(item.find("bndbox").find("ymin").text))     # In the original range of image
    xmax = int(float(item.find("bndbox").find("xmax").text))     # In the original range of image
    ymax = int(float(item.find("bndbox").find("ymax").text))     # In the original range of image

    print("+"*30)
    print("Class name: ", objName)
    print("Coordinates (x1, y1, x2, y2): {}, {}, {}, {}".format(xmin, ymin, xmax, ymax))

    string = "Class: " + objName

    char_size_w = len(string) * 9
    cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 175, 0), 2)
    cv2.rectangle(img, (xmin, ymin), (xmin + char_size_w, ymin - 20), (0, 175, 0), -2)
    cv2.putText(img, string, (xmin, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()


