import cv2


capture = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = capture.read()
    if not ret:
        print("Fail")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8, minSize=(50, 50))

    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        face = gray[y:y+h, x:x+w]        

        
        eyes = eyes_cascade.detectMultiScale(face, scaleFactor=1.2, minNeighbors=12, minSize=(30, 30))
        
        for (x2, y2, w2, h2) in eyes:
            center = (x + x2 + w2//2, y + y2 + h2//2)
            cv2.circle(frame, center, 5, (0, 0, 255), 2)


    cv2.putText(frame, str(len(faces)), (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('Face Detector', frame)

    # cv2.imshow("Face", face) # Hatalı / Sadece tek yüz


    if cv2.waitKey(10)== ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
print("Quit")