
# import the necessary packages

import numpy as np
import cv2
import os
import shutil
from urllib import request as rq
from PIL import Image


# getting all images paths

def GetPath():
    recognizer = recType
    i=0
    imagesPaths = os.listdir('media/facesSet/')
    faces = []
    Ids = []
    while i < len(imagesPaths):
        imagePath = 'media/facesSet/'+imagesPaths[i]
        faceImg = Image.open(imagePath).convert('L')
        faceArray = np.array(faceImg,'uint8')
        faces.append(faceArray)
        Id = int(os.path.split(imagePath)[-1].split('_')[1])
        print(Id)
        Ids.append(Id)
        i=i+1

    return faces , Ids

# Machine learining  function [ training function ]
def train():
	recognizer = recType
	faces , Ids = GetPath()
	recognizer.train(faces,np.array(Ids))

    # saving all faces featues in yml file format 
	recognizer.save('media/yml/machineLearning.yml')

