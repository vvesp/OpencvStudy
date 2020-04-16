import cv2
img = cv2.imread(".\\Img\\pengins.jpg",0) #color ton img
img_1 = cv2.imread(".\\Img\\pengin.jpg",0) #gray ton img

print(img) #노멛 배열모양 확인
print(img.shape) #노멛 배열모양 확인
print(img_1.shape)