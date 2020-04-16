import cv2,time

video = cv2.VideoCapture(0) #내부캠 : 0, 외장캠 : 1, 세번째 캠은 : 2

check, frame = video.read() #check:booltype 리턴 True 비디오캡처, frame 넘파이배열 첫이미지 캡처
time.sleep(3) # 초단위

cv2.imshow('Capturing',frame)
cv2.waitKey(0)

video.release()#밀리초

cv2.destroyAllWindows()
# print(check)
# print(frame)
