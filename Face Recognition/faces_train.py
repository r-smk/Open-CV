from cProfile import label
import cv2 as cv
import os
import numpy as np

people = ['ben_afflek', 'elton_john',
          'jerry_seinfeld', 'madonna', 'mindy_kaling']

DIR = r'D:\workshops\Open-CV\Faces\train'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for image in os.listdir(path):
            img_path = os.path.join(path, image)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print("Training complete ------------")


features = np.array(features, dtype='object')
labels = np.array(labels)

faces_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and labels list
faces_recognizer.train(features, labels)
print("Recognizer trained ------------")

faces_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
