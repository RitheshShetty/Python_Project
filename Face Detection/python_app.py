import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('Test.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (225, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey()

cv2.imwrite("face_detected.jpg")


'''
To Run the code, open cmd and navigate to this python file path and run 'python python_app.py'
'''