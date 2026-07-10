import cv2
import pygame
import math
from ultralytics import YOLO

pygame.mixer.init()
pygame.mixer.music.load("audio.mp3") 


cap = cv2.VideoCapture(0)
model = YOLO('fire.pt')


classnames = ['fire']
alarm_playing = False  

def play_alarm():
    global alarm_playing
    if not alarm_playing: 
        pygame.mixer.music.play(-1)  
        alarm_playing = True

def stop_alarm():
    global alarm_playing
    if alarm_playing: 
        pygame.mixer.music.stop()
        alarm_playing = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    result = model(frame, stream=True)

    fire_detected = False 

    # Checking detected objects
    for info in result:
        boxes = info.boxes
        for box in boxes:
            confidence = math.ceil(box.conf[0] * 100)
            Class = int(box.cls[0])

            if confidence > 50 and classnames[Class] == "fire":
                fire_detected = True
                break 

    if fire_detected:
        print("Fire detected!")
        play_alarm() 
    else:
        print("No fire detected.")
        stop_alarm()  

   
    cv2.imshow('Fire Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()