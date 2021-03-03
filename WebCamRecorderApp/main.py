import cv2
import time


vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('video.mp4', vid_cod, 20.0, (640, 480))
video=cv2.VideoCapture(0)

a=1

while True:
	a += 1
	check, frame = video.read()

	print(check)
	print(frame)

	#color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
	cv2.imshow("Capturing", frame)
	output.write(frame)

	key=cv2.waitKey(1)

	if key==ord('q'):
		break


print(a)
video.release()
output.release()
cv2.destroyAllWindows()