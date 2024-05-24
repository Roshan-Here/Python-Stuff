#use password from App password reff: https://myaccount.google.com/apppasswords
from email.message import EmailMessage
import smtplib

print("Welcome to Email Spam Center .....")
print("it can either use for good things/bad~~")
print("if you are using it for Spaming !! plz use non usable email bcoz that mail meight banned !!!~")
print("=====================================================================================")
def Inputym():
    email_sender = input("giv me sender email id~ ")
    email_pass = input("giv me your email pass ~ ")
    email_reciver = input("giv me email id to spam ~ ")
    spam_time = int(input("how many time do you wanna Spam???~~ "))
# email_sender = ""
# email_pass = ""
# email_reciver = ""
    msg = input("Body of spam content ?? ~ ")
    message = f""""
    {msg}
    """
    em = EmailMessage()
    em['subject'] = "Spam time"
    em.set_content(message)
    return email_sender,email_reciver,email_pass,em,spam_time

es , er ,ep, em ,sptime = Inputym()
def SendBulk(email_sender,email_reciver,email_pass,em):
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(email_sender,email_pass)
    s.sendmail(email_sender,email_reciver,em.as_string())
    s.quit()

for x in range(sptime):
    SendBulk(es,er,ep,em)
    print(f"spam {x+1}:sended")
print("Done~~~")
