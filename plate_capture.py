import cv2

harcascade = "model/haarcascade_russian_plate_number.xml"

cam = cv2.VideoCapture(0)

cam.set(3, 640) # width
cam.set(4, 480) # height

min_area = 500
count = 0

while True:
    success, img = cam.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x,y,w,h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 2)
            cv2.putText(img, "Plat Nomor", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y+h, x:x+w]
            cv2.imshow("ROI", img_roi)

    cv2.imshow("Hasil", img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("plates/plat_ke_" + str(count) + ".jpg", img_roi)
        cv2.rectangle(img, (0,200), (640,300), (255,255,0), cv2.FILLED)
        cv2.putText(img, "Gambar Tersimpan", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 0, 255), 2)
        cv2.imshow("Results",img)
        cv2.waitKey(500)
        count += 1