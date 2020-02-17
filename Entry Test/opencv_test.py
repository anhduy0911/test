import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('data/image.png')
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

figure = plt.figure(figsize=(8,6))
figure.add_subplot(2,3,1)
plt.imshow(img)
plt.title('original')

h,w,c = img.shape
croped = img[0:int(w/2),0:int(h/2)]
figure.add_subplot(2,3,2)
plt.imshow(croped)
plt.title('croped')

rot = cv.rotate(img,cv.ROTATE_90_CLOCKWISE)
figure.add_subplot(2,3,3)
plt.imshow(rot)
plt.title('Rotate 90')

resized = cv.resize(img,(int(w/2),int(h/2)))
figure.add_subplot(2,3,4)
plt.imshow(resized)
plt.title('Resized Img')

gaussianblured = cv.GaussianBlur(img,(5,5),0)
figure.add_subplot(2,3,5)
plt.imshow(gaussianblured)
plt.title('Gaussian Blur-ed')

edgedetected = cv.Canny(img,150,300) #using canny's edge detection algorithm
figure.add_subplot(2,3,6)
plt.imshow(edgedetected)
plt.title('Edge detected')

plt.savefig('opencv_test.png')

plt.show()



