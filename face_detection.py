# import the necessary packages

import numpy as np
import cv2
import os
import shutil
from urllib import request as rq
from PIL import Image


# Fixing The camera ip address
# we assume that you use an external web cam
# you can use the application  names ipWebcam for andriod to use the phone cam

ip = 'http://192.168.43.1:8080/shot.jpg'


# Face Detection function

def FaceDetection():
    
	url = ip
	id=input("Plz Give The Face Id  :) : ")
	i=0
	fontface = cv2.FONT_HERSHEY_SIMPLEX
	fontscale = 1
	fontcolor = (160, 189, 10)

	while(True):
    	
		try:
            
			imgResp = rq.urlopen(url)
			imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
			img1= cv2.imdecode(imgNp,-1)
			face_cascade = cv2.CascadeClassifier('media/xml/face_map.xml')
			img = img1
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			faces = face_cascade.detectMultiScale(gray, 1.3, 5)
			'''cv2.putText(img, "Menu :", (2,30), 2, 0.7, fontcolor,1)
			cv2.putText(img, "Q = exit  ", (2,60), 2, 0.5, fontcolor,1)
			cv2.putText(img, "S = save  ", (2,90),2, 0.5, fontcolor,1)'''
			for (x,y,w,h) in faces:
				cv2.putText(img, str(i), (x+10,y+h-20), fontface, fontscale, (99, 30, 233),2)
				cv2.rectangle(img,(x,y),(x+w,y+h),(61,63,193),2) 
				if cv2.waitKey(1) == ord('s'):
					i+=1	
					tmp_name=str(id)+"_" + str(i) + ".jpg"
					cv2.imwrite('media/facesSet/face_'+tmp_name,gray[y:y+h,x:x+w])
					cv2.waitKey(30)
			img = cv2.resize(img, (960, 540)) 
			cv2.imshow('Detection',img)
			cv2.waitKey(1)
			if i > 20:
				cv2.destroyAllWindows()
				break
			if cv2.waitKey(1) == ord('q'):
				cv2.destroyAllWindows()
				break
		except:

			cv2.destroyAllWindows()

