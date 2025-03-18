import cv2
import time
from twilio.rest import Client

# Load the cascade
face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')

# Twilio API Settings
# this code for
account_sid = '<account_sid>'
auth_token = '<auth_token>'
twilio_number = '<twilio_number>'
mynumber = '<your_number>'  # your number
client = Client(account_sid,auth_token,)

total_count = 0
t = 1 * 60
def sms_alert():
 message = client.messages.create(
 body=f"{count} students are in the classRoom and total of {total_count} in the class till now",
 from_=twilio_number,
 to=mynumber
 )
 print(message.sid)
 time.sleep(t)

# To capture video from webcam.
cap = cv2.VideoCapture(0)
# To use a video file as input
# cap = cv2.VideoCapture(r"C:\Users\Admin\Downloads\Office - 69952.mp4")
while True:
 # Read the frame
 _, img = cap.read()
 count = 0
 # Convert to grayscale
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 # Detect the faces
 faces = face_cascade.detectMultiScale(gray, 1.1, 4)
 font = cv2.FONT_HERSHEY_SIMPLEX
 # Draw the rectangle around each face
 for (x, y, w, h) in faces:
  cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
  count += 1
 #sms_alert()
 cv2.putText(img, f'{count}', (50, 50), font, 1, (0, 255, 255),2, cv2.LINE_4)
 # Display
 cv2.imshow('img', img)
 sms_alert()
 # Stop if escape key is pressed
 k = cv2.waitKey(30) & 0xff
 if k == 'Q':
  break
# Release the VideoCapture object
cap.release()
