import cv2, os
# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
os.system('cls')
video_capture = cv2.VideoCapture(0)


while True:
    # Read the image
    otro, image = video_capture.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30),
        #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    #print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Cara encontrada", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
