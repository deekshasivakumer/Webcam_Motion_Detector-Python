import cv2, time

first_frame=None

video=cv2.VideoCapture(0)

while True:
    a=a+1
    check, frame = video.read()


    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2GaussianBlur(gray,(21,21),0)

     
    if first_frame id None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)

    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    #to smooth out the white areas in the threshold frame
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)

    key=cv2.waitKey(1)
    print(gray)
    print(delta_frame)

    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows
