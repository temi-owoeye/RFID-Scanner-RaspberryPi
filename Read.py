#!/usr/bin/env python

import RPi.GPIO as GPIO  #GPIO has all functions needed to interact with GPIO pins
import smtplib
import threading # for making threads
from mfrc522 import SimpleMFRC522 #will enable communication with RFID RC522
from datetime import datetime
from time import sleep

today = datetime.today()
date = today.strftime("%b-%d-%Y--%H-%M-%S")

id = 0
text = ""

#for email updates 
SMTP_SERVER = 'smtp.gmail.com' #Email Server 
SMTP_PORT = 587 #Server Port 
GMAIL_USERNAME = #emial
GMAIL_PASSWORD = #password

def read():
    reader = SimpleMFRC522()
    
    try:
                
        global id
        global text
        
        #create thread instance 
        t = threading.Thread(target=display_waiting_text) #pass thread the function you want it to run with it's arguments
        t.start() #start the thread
        
        id, text = reader.read()
        t.join() #tell one thread to wait for another thread to finish
        
        print(id)
        print(text)
        
        #send email update
        sender = Emailer()
        sendTo = #email
        emailContent = "On " + str(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")) + " user " + str(text.split(" ")[0]) + " tried to access the system. Their ID number is: " + str(id) + " ."
        emailSubject = "System Accessed: " + date
        #Sends an email to the "snedTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.
        sender.sendmail(sendTo, emailSubject, emailContent)
    
    finally:
        id = 0
        text = ""
        GPIO.cleanup() #exit script
    
        
def display_waiting_text():
    global id
    global text
    while id == 0 and text == "":
        print("Waiting for card")
                
        print("Waiting for card.")
        sleep(0.5)
                
        print("Waiting for card..")
        sleep(0.5)
                
        print("Waiting for card...")
        sleep(0.5)
        
class Emailer:
    def sendmail(self, recipient,  subject, content):
        #Creating the headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " +subject, "To: " + recipient, "MIME-Version 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit
    
