import cv2
import pygame
import math
from ultralytics import YOLO
from email.message import EmailMessage
import smtplib
from helpers import get_email_config

email_config = get_email_config()
SMTP_SERVER = email_config["SMTP_SERVER"]
SMTP_PORT = email_config["SMTP_PORT"]
SENDER_EMAIL = email_config["SENDER_EMAIL"]
SENDER_PASSWORD = email_config["SENDER_PASSWORD"]
RECIPIENT_EMAIL = email_config["RECIPIENT_EMAIL"]

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

def send_notification():
    print("Sending notification: Fire detected!")
    subject = "Fire Alert!"
    body = "Fire has been detected by the AI Fire Alarm system. Please take immediate action"
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg.set_content(body)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)

        print("Notification email sent successfully!")

    except Exception as e:
        print(f"Failed to send notification. Error: {e}")


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    result = model(frame, stream=True)

    fire_detected = False 

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
        send_notification()
    else:
        print("No fire detected.")
        stop_alarm()  

   
    cv2.imshow('Fire Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()