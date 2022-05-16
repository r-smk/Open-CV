import numpy as np
import cv2 as cv


haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy')

people = ['ben_afflek', 'elton_john',
          'jerry_seinfeld', 'madonna', 'mindy_kaling']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(
    r'D:\workshops\Open-CV\Faces\val\elton_john\httpafilesbiographycomimageuploadcfillcssrgbdprgfacehqwMTEODAOTcxNjcMjczMjkzjpg.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    # Predict the label of the face
    label, confidence = face_recognizer.predict(faces_roi)

    print(f'Label = {people[label]} with confidence {confidence}')

    cv.putText(img, str(people[label]), (20, 20),
               cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), 2)

    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow('Face', img)

cv.waitKey(0)
