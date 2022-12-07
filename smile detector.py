import cv2

#face classifiers
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')


#grab webcam feed
webcam = cv2.VideoCapture(0)

#show the current frame
while True:

    #read the current frame from the webcam
    successful_frame_read, frame = webcam.read()

    #if error , abort
    if not successful_frame_read:
        break

    #change to grayscale
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect faces first
    faces = face_detector.detectMultiScale(frame_grayscale)

    # run face detection within, each of those faces
    for(x, y, w, h) in faces:

        #draw a rectangle around the face
        cv2.rectangle(frame , (x,y), (x+w, y+h), (100, 200, 50), 4)


        #get the sub frame using slicing in array
        the_face = frame[y:y+h, x:x+w]

        # change to grayscale
        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

        smiles = smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.7, minNeighbors=20)

        #Find all smile in the faces:
        for (x_ ,y_ ,w_, h_) in smiles:

            #draw rectangle around the smile
            cv2.rectangle(the_face, (x_,y_), (x_+w_, y_+h_), (50, 50, 200),4)

        #label this face as smiling
        #if len(smiles)> 0:
           # cv2.putText(frame, 'smiling', (x, y+h+40), fontScale=3,fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))



    #show the current frame
    cv2.imshow('why so serious?',  frame)

    #Display
    cv2.waitKey(1)


#cleanup
webcam.release()
cv2.destroyAllWindows()
