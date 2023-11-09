# face detection in photo
import cv2

# reading image
img=cv2.imread("C:\\Users\\HP\\Pictures\\Saved Pictures\\profile pic.jpg",1)

# face cascade
face_cascade=cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')

# face detection function
def detect_face(img):
    face_img=img.copy()
    face_rects=face_cascade.detectMultiScale(face_img,scaleFactor=1.3,minNeighbors=3)
    for(a,b,c,d) in face_rects:
        cv2.rectangle(face_img,(a,b),(a+c,b+d),(0,0,255),2)
    return face_img
# face detection apply
face_img=detect_face(img)

# result
cv2.imshow('original image',img)
cv2.imshow('detectedface',face_img)
cv2.waitKey(0)
cv2.destroyAllWindows()