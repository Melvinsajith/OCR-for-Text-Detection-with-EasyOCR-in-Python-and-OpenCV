import numpy as np 

import cv2
import easyocr

reader = easyocr.Reader(["en"])



ocr_results = reader.readtext("C:\\Users\\USER\\Pictures\\cv_pro\\ocr\\car_plate2.png")

print(ocr_results)


top_left = ocr_results[0][0][0]
bottom_right = ocr_results[0][0][2]

text =ocr_results[0][1]

print(text)

img =cv2.imread("C:\\Users\\USER\\Pictures\\cv_pro\\ocr\\car_plate2.png")

img = cv2.rectangle(img, top_left,bottom_right,(0,0,255),5)
img = cv2.putText(img,text,top_left,cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)

cv2.imshow("img",img)

cv2.waitKey(0)