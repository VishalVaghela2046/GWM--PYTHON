import os
import math
import random
import smtplib

digits = "0123456789"
OTP = ""

for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]

otp = OTP + " is your OTP"
message = otp

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("varun.simbeez@gmail.com", "ciaggfssdetyvmgl")
server.sendmail('varun.simbeez@gmail.com','vishalvaghela3969@gmail.com',message)
server.quit()

a = input("Enter your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")