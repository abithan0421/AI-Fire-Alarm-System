# AI-Based Fire Detection and Alarm System using YOLOv8

## Overview

The AI-Based Fire Detection and Alarm System is a real-time computer vision application that detects fire from live surveillance camera feeds using the **Ultralytics YOLOv8** object detection model. The system continuously monitors video streams, identifies fire with high confidence, tracks detected objects across frames, and immediately initiates emergency actions such as visual alerts, alarm activation, and email notifications.

Designed for deployment in shopping malls, office buildings, warehouses, hospitals, schools, and other public facilities, the system aims to provide rapid fire detection and reduce response time during emergencies.

## Features

*  Real-time fire detection using a custom-trained **Ultralytics YOLOv8** model.
*  Live video processing from CCTV cameras, webcams, or video files using **OpenCV (cv2)**.
*  Fire object localization with bounding boxes, class labels, and confidence scores.
*  Object tracking to maintain consistent identification of detected fire across consecutive video frames.
*  Automatic alarm activation using **Pygame** audio playback when fire is detected.
*  Instant email notifications sent to predefined recipients using Python's **smtplib** and **EmailMessage** modules.
*  Continuous frame-by-frame monitoring for real-time surveillance.
*  Live visualization with annotated detection results displayed on screen.
*  Confidence threshold filtering to reduce false alarms.
*  Supports multiple input sources including webcams, IP cameras, CCTV streams, and prerecorded videos.
*  Modular architecture, allowing easy integration with IoT devices, fire alarm systems, or smart building automation.

## Technologies Used

* **Python**
* **Ultralytics YOLOv8**
* **OpenCV (cv2)** – Video capture, image processing, and visualization
* **Pygame** – Alarm sound playback
* **SMTP (smtplib)** – Automated email notifications
* **EmailMessage** – Email composition
* **Ultralytics Object Tracking** – Persistent tracking of detected fire objects
* **Google Colab** – Model training

## System Workflow

1. Capture video frames from a surveillance camera.
2. Process each frame using the trained YOLOv8 model.
3. Detect and track fire objects in real time.
4. Display bounding boxes, labels, and confidence scores.
5. Trigger an audible alarm using Pygame when fire is detected.
6. Automatically send an email alert to the configured recipient(s).
7. Continue monitoring until the application is stopped.

## Applications

* Shopping malls
* Commercial buildings
* Warehouses
* Manufacturing industries
* Hospitals
* Educational institutions
* Smart buildings
* Public transportation terminals
* Residential apartment complexes

## Future Enhancements

* SMS and mobile push notifications
* Integration with IoT fire alarm hardware
* Smoke detection alongside fire detection
* Multi-camera surveillance support
* Emergency service notification
* Incident logging and analytics dashboard
* Cloud-based monitoring and reporting
* Web and mobile application integration
