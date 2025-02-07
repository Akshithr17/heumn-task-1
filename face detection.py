#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import required libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt
import time 
get_ipython().magic('matplotlib inline')


def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')

#load test iamge
test1 = cv2.imread('data/test1.jpg')

#convert the test image to gray image as opencv face detector expects gray images
gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)

 
plt.imshow(gray_img, cmap='gray')


faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5);

#print the number of faces found
print('Faces found: ', len(faces))

#go over list of faces and draw them as rectangles on original colored img
for (x, y, w, h) in faces:
    cv2.rectangle(test1, (x, y), (x+w, y+h), (0, 255, 0), 2)


plt.imshow(convertToRGB(test1))



def detect_faces(f_cascade, colored_img, scaleFactor = 1.1):
    img_copy = np.copy(colored_img)
    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

    #let's detect multiscale (some images may be closer to camera than others) images
    faces = f_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=5);

    #go over list of faces and draw them as rectangles on original colored img
    for (x, y, w, h) in faces:
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return img_copy


# Now let's try this function on another test image. 

#load another image
test2 = cv2.imread('data/test3.jpg')

#call our function to detect faces
faces_detected_img = detect_faces(haar_face_cascade, test2)

#conver image to RGB and show image
plt.imshow(convertToRGB(faces_detected_img))


test2 = cv2.imread('data/test4.jpg')

#call our function to detect faces
faces_detected_img = detect_faces(haar_face_cascade, test2)

#conver image to RGB and show image
plt.imshow(convertToRGB(faces_detected_img))


test2 = cv2.imread('data/test4.jpg')

#call our function to detect faces
faces_detected_img = detect_faces(haar_face_cascade, test2, scaleFactor=1.2)

#conver image to RGB and show image
plt.imshow(convertToRGB(faces_detected_img))


lbp_face_cascade = cv2.CascadeClassifier('data/lbpcascade_frontalface.xml')

#load test image
test2 = cv2.imread('data/test2.jpg')
#call our function to detect faces
faces_detected_img = detect_faces(lbp_face_cascade, test2)

#conver image to RGB and show image
plt.imshow(convertToRGB(faces_detected_img))


# Let's try it on another test image. 

# In[12]:

#load test image
test2 = cv2.imread('data/test3.jpg')
#call our function to detect faces
faces_detected_img = detect_faces(lbp_face_cascade, test2)

#conver image to RGB and show image
plt.imshow(convertToRGB(faces_detected_img))


haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')
#load cascade classifier training file for lbpcascade
lbp_face_cascade = cv2.CascadeClassifier('data/lbpcascade_frontalface.xml')

#load test image1
test1 = cv2.imread('data/test5.jpg')
#load test image2
test2 = cv2.imread('data/test6.jpg')


# ### Test-1

#------------HAAR-----------
#note time before detection
t1 = time.time()

#call our function to detect faces
haar_detected_img = detect_faces(haar_face_cascade, test1)

#note time after detection
t2 = time.time()
#calculate time difference
dt1 = t2 - t1
#print the time differene

#------------LBP-----------
#note time before detection
t1 = time.time()

lbp_detected_img = detect_faces(lbp_face_cascade, test1)

#note time after detection
t2 = time.time()
#calculate time difference
dt2 = t2 - t1

f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

#show Haar image
ax1.set_title('Haar Detection time: ' + str(round(dt1, 3)) + ' secs')
ax1.imshow(convertToRGB(haar_detected_img))

#show LBP image
ax2.set_title('LBP Detection time: ' + str(round(dt2, 3)) + ' secs')
ax2.imshow(convertToRGB(lbp_detected_img))


t1 = time.time()

#call our function to detect faces
haar_detected_img = detect_faces(haar_face_cascade, test2)

#note time after detection
t2 = time.time()
#calculate time difference
dt1 = t2 - t1
#print the time differene

#------------LBP-----------
#note time before detection
t1 = time.time()

lbp_detected_img = detect_faces(lbp_face_cascade, test2)

#note time after detection
t2 = time.time()
#calculate time difference
dt2 = t2 - t1

f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

#show Haar image
ax1.set_title('Haar Detection time: ' + str(round(dt1, 3)) + ' secs')
ax1.imshow(convertToRGB(haar_detected_img))

#show LBP image
ax2.set_title('LBP Detection time: ' + str(round(dt2, 3)) + ' secs')
ax2.imshow(convertToRGB(lbp_detected_img))


# In[ ]:


import numpy as np
import cv2
import matplotlib.pyplot as plt
import time



def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')

# load test iamge
test1 = cv2.imread('data/test1.jpg')

# convert the test image to gray image as opencv face detector expects gray images
gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)

plt.imshow(gray_img, cmap='gray')

faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

# print the number of faces found
print('Faces found: ', len(faces))

for (x, y, w, h) in faces:
    cv2.rectangle(test1, (x, y), (x + w, y + h), (0, 255, 0), 2)

plt.imshow(convertToRGB(test1))


def detect_faces(f_cascade, colored_img, scaleFactor=1.1):
    img_copy = np.copy(colored_img)
    # convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

    # let's detect multiscale (some images may be closer to camera than others) images
    faces = f_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=5);

    # go over list of faces and draw them as rectangles on original colored img
    for (x, y, w, h) in faces:
        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return img_copy


test2 = cv2.imread('data/test3.jpg')


faces_detected_img = detect_faces(haar_face_cascade, test2)

# convert image to RGB and show image
plt.imshow(convertToRGB(faces_detected_img))

test2 = cv2.imread('data/test4.jpg')

# call our function to detect faces
faces_detected_img = detect_faces(haar_face_cascade, test2)

# convert image to RGB and show image
plt.imshow(convertToRGB(faces_detected_img))


test2 = cv2.imread('data/test4.jpg')

# call our function to detect faces
faces_detected_img = detect_faces(haar_face_cascade, test2, scaleFactor=1.2)

# convert image to RGB and show image
plt.imshow(convertToRGB(faces_detected_img))


lbp_face_cascade = cv2.CascadeClassifier('data/lbpcascade_frontalface.xml')

# load test image
test2 = cv2.imread('data/test2.jpg')
# call our function to detect faces
faces_detected_img = detect_faces(lbp_face_cascade, test2)

# convert image to RGB and show image
plt.imshow(convertToRGB(faces_detected_img))

# Let's try it on another test image.

# In[12]:

# load test image
test2 = cv2.imread('data/test3.jpg')
# call our function to detect faces
faces_detected_img = detect_faces(lbp_face_cascade, test2)

# convert image to RGB and show image
plt.imshow(convertToRGB(faces_detected_img))


haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')
# load cascade classifier training file for lbpcascade
lbp_face_cascade = cv2.CascadeClassifier('data/lbpcascade_frontalface.xml')

# load test image1
test1 = cv2.imread('data/test5.jpg')
# load test image2
test2 = cv2.imread('data/test6.jpg')

t1 = time.time()

# call our function to detect faces
haar_detected_img = detect_faces(haar_face_cascade, test1)

# note time after detection
t2 = time.time()
# calculate time difference
dt1 = t2 - t1
# print the time difference

# ------------LBP-----------
# note time before detection
t1 = time.time()

lbp_detected_img = detect_faces(lbp_face_cascade, test1)

# note time after detection
t2 = time.time()
# calculate time difference
dt2 = t2 - t1

f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# show Haar image
ax1.set_title('Haar Detection time: ' + str(round(dt1, 3)) + ' secs')
ax1.imshow(convertToRGB(haar_detected_img))

# show LBP image
ax2.set_title('LBP Detection time: ' + str(round(dt2, 3)) + ' secs')
ax2.imshow(convertToRGB(lbp_detected_img))

t1 = time.time()

# call our function to detect faces
haar_detected_img = detect_faces(haar_face_cascade, test2)

# note time after detection
t2 = time.time()
# calculate time difference
dt1 = t2 - t1

t1 = time.time()

lbp_detected_img = detect_faces(lbp_face_cascade, test2)

# note time after detection
t2 = time.time()
# calculate time difference
dt2 = t2 - t1
# print the time difference
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# show Haar image
ax1.set_title('Haar Detection time: ' + str(round(dt1, 3)) + ' secs')
ax1.imshow(convertToRGB(haar_detected_img))

# show LBP image
ax2.set_title('LBP Detection time: ' + str(round(dt2, 3)) + ' secs')
ax2.imshow(convertToRGB(lbp_detected_img))

