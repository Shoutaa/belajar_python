from cvzone.FaceDetectionModule import FaceDetector
import cv2

img = cv2.imread('image.jpg')
detector = FaceDetector()
img, bboxs = detector.findFaces(img, draw=False)

if bboxs:
    for bbox in bboxs:
        x, y, w, h=bbox ['bbox']
        face_img = img[y:y+h, x:x+w]
        blurred_face = cv2.GaussianBlur(face_img, (71, 71), 0)
        img[y:y+h, x:x+w] = blurred_face

cv2.imshow("image",  img)
cv2.waitKey(0)
cv2.destroyAllWindows()        
