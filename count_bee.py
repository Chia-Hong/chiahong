import cv2
import numpy as np


def displayIMG(img,windowName):
    cv2.namedWindow(windowName,cv2.WINDOW_AUTOSIZE)   
    cv2.imshow(windowName,img)


img = cv2.imread('D:/vscode/picture/0830.jpeg')
# displayIMG(img , 'bee')

# size = img.shape
# print(size)
point1 = (380, 0)    #左上角座標
point2 = (770, 433)  #右下角座標
img1 = img[point1[1]: point2[1], point1[0]: point2[0]]
displayIMG(img1 , 'bee_cut')

# gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# ret,out1=cv2.threshold(gray,70,255,cv2.THRESH_BINARY_INV)
# displayIMG(out1 , 'gray')
b,g,r=cv2.split(img1)

# displayIMG(b , 'b')
displayIMG(g , 'g')
# displayIMG(r , 'r')

ret,out=cv2.threshold(g,70,255,cv2.THRESH_BINARY_INV)
displayIMG(out, 'g2')

# k=np.ones((9,9),np.uint8)
# erosion=cv2.erode(out,k,iterations=1)
# displayIMG(erosion,'e')
# k1=np.ones((7,7),np.uint8)
# dilation = cv2.dilate(erosion,k1,iterations = 1)
# displayIMG(dilation,'d')

# blurred = cv2.GaussianBlur(dilation, (9, 9), 0)   #使用高斯模糊
# edged = cv2.Canny(blurred, 30, 600)        #canny邊緣檢測、調正參數
# (cnts,_) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# clone = img1.copy() 
# clone1 = img1.copy() 
# for i, contour in enumerate(cnts):
#     if cv2.contourArea(contour) < 50:
#         continue
#     (x, y, w, h) = cv2.boundingRect(contour)
#     (a, b), radius = cv2.minEnclosingCircle(contour)
#     centeroid = (int(a), int(b))
#     radius = int(radius)
#     c = cv2.drawContours(clone, contour, -1, (0, 0 , 255), 2)
#     rec = cv2.rectangle(clone1, (x, y), (x + w, y + h), (0, 0, 255), 2)
# displayIMG(rec , 'final_image')
# displayIMG(c , 'final_image1')
# print(len(cnts))

k=np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(out,cv2.MORPH_OPEN,k,iterations = 2)

#確定背景區域
k2=np.ones((3,3),np.uint8)
sure_bg = cv2.dilate(opening,k2,iterations = 3)

#確定前景區域
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,3)
a = cv2.normalize(dist_transform, dist_transform, 0, 1.0, cv2.NORM_MINMAX)
ret1,sure_fg = cv2.threshold(a, 0.5*dist_transform.max(),255,0)

#查找未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

#標記標籤
ret2,markers1 = cv2.connectedComponents(sure_fg)
markers = markers1+1
markers[unknown==255] = 0

markers3 = cv2.watershed(img1,markers)
img1[markers3 == -1]=[0,0,255]

displayIMG(dist_transform , 'dist_transform')


displayIMG(img1 , 'final_image')



k = cv2.waitKey(0)

