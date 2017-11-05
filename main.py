import cv2
import numpy as np

cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
rec = cv2.VideoWriter("output.avi", fourcc,17 , (640, 480))
flag = False
font = cv2.FONT_HERSHEY_SIMPLEX
while 1:
    b, img = cam.read()
    if b:
        cv2.putText(img,"c-Capture  s-Save  q- Quit",(100,50),cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(100,100,100))

    key1 = cv2.waitKey(1) & 0XFF
    if key1 == ord('c'):
        flag = True
    if flag:
        cv2.putText(img, "Recording", (50, 100), cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(100, 100, 100))
        rec.write(img)
    if key1 == ord('s'):
        flag = False
    if not flag:
        rec.release()

    if key1 == ord('q'):
        rec.release()
        break
    cv2.imshow("ViewPort", img)

cv2.destroyAllWindows()























# import cv2
# import numpy as np
#
# cam = cv2.VideoCapture(0)
#
# while True:
#     b, img = cam.read()
#     if b:
#         cv2.imshow("Window",img)
#     else:
#         print("The camera is not working!")
#         break
#     key = cv2.waitKey(1)&0xFF
#     if key==ord('q'):
#         break
#     elif key==ord('c'):
#         cv2.im
# cv2.destroyAllWindows()
# cam.release()
#
# cv2.VideoWriter()