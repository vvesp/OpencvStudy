import cv2
img = cv2.imread(".\\Img\\pengins.jpg",0) #color ton img
img_1 = cv2.imread(".\\Img\\pengin.jpg",1) #gray ton img

# print(img.shape) #배열모양 확인
# print(img_1.shape)

# resized_img = cv2.resize(img_1,(450,650)) #1.리사이즈
resized_img = cv2.resize(img_1,(int(img_1.shape[1]/3),int(img_1.shape[0]/3))) #2.리사이즈 1:3 줄임
cv2.imshow("peng", resized_img) #리사이즈 display img
# cv2.imshow("pengins", img) #display img

cv2.waitKey(0) # 사용자가 키를 누를때까지 기다림
# cv2.waitKey(2000) #2000밀리언초 기다림
cv2.destroyAllWindows() #종료