
import cv2

##face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")

img = cv2.imread('Youssef_OUSSAID.jpeg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    
    cv2.rectangle(img, (x, y), (x + w, y +h), (225, 0, 0), 2)

cv2.imshow('img' , img)

cv2.waitKey()


