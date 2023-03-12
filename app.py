import cv2
cap = cv2.VideoCapture(1)    # 0 use default web camera   1 for secondary camera


###################################
nPlateCascade = cv2.CascadeClassifier("resources/haarcascade_licence_plate_rus_16stages.xml")
minArea = 500
color = (255,0,255)
count = 0
#####################################

cap.set(3,640)       # width id no 3 as 640
cap.set(4,480)       # height id no 4 as 480
cap.set(10,100)      # brightness id no 10 as 100
while True:
    success, img  = cap.read()

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray,1.1,4)         #imgGray , scale factor, minimum neighbour
    #creating the bounding box
    for (x,y,w,h) in numberPlates:
        area = w*h
        if area>minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgRoi)




    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("resources/Scanned/NoPlate_"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)

        count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break