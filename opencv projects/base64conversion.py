import cv2
import base64
img=cv2.imread(r"C:\Users\HP\Pictures\Saved Pictures\profile pic.jpg")# r is used to avoid unicodeescape error
print(type(img))
cv2.imshow("window",img)
cv2.waitKey(0)
transmitted_data=print(base64.b64encode(img))
#encoding the image
print(transmitted_data)
# decoding the image
print(base64.b64decode(transmitted_data))

