
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

# face recognition

def RecognizeFace():
    
	url = ip
	try:
		rec = recType
        
        # loading the yml file [ the faces features database ]
		rec.read('media/yml/machineLearning.yml')



		while(True):
			
			imgResp = rq.urlopen(url)
			imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
			img1= cv2.imdecode(imgNp,-1)
            
            # loading xml haarcascade file 
			face_cascade = cv2.CascadeClassifier('media/xml/face_map.xml')
			img = img1
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			faces = face_cascade.detectMultiScale(gray, 1.3, 5)
			
			for (x,y,w,h) in faces:
				cv2.rectangle(img,(x,y),(x+w,y+h),(61,63,193),2) 
				idFace,conf=rec.predict(gray[y:y+h,x:x+w])
				print(rec.predict(gray[y:y+h,x:x+w]))
				faceInfo = models.FaceInfo.objects.filter(id=idFace)
				idFrontface = faceInfo[0].Nom

				# the we are used the LBPH so the conf 'var' is the difference bitwen the histograme in the .yml file and the histograme of faces taken in realtime
                #  Attention : conf = 0 means faces are sames
				if conf < 70:
					idFrontface = faceInfo[0].Nom
				else:
					idFrontface = "?????"	
				#cv2.putText(img, str(idFrontface), (x,y+h), fontface, fontscale, fontcolor)
				cv2.putText(img, str(idFrontface), (x-30,y+h-90), 2, 1, (99, 30, 233),2)
			img = cv2.resize(img, (960, 540)) 
			cv2.imshow('Recognize',img)
			if cv2.waitKey(1) == ord('q'):
				cv2.destroyAllWindows()
				break
	except:
		cv2.destroyAllWindows()


