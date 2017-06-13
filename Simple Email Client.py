###Simple Email Client###
#Import#
import smtplib

#Your email#
m_email = input("Please input the Senders Email:\n")
m_server = input("Please input the mail server (For example: 'mail.google.com'):\n")

#Recepient email#
r_emails = input("Please input a list of comma seperated emails:\n")
r_emails = r_emails.replace(" ","").split(",")

#Message#
subject = input("Input your message subject:\n")
subject = "Subject: " + subject
main_body = input("Input your main message (New Line = '\\n'):\n")

message = subject + "\n \n" + main_body

#Test Print#
print("Sender: " + m_email)
print("Server: " + m_server)
print("Recipient(s): "r_emails)
print("Message: " + message)
