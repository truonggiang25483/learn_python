###Simple Email Client###
#Import#
import smtplib
import getpass

#Base#
send = "True"
ss = "True"
repeats = 1
while send == "True":
    #Your email#
    m_email = input("Please input the your email:\n")
    m_pwd = getpass.getpass("Please input your password:\n")
    m_server = "smtp.gmail.com"
    m_port = 587
    
    #Recepient email#
    r_emails = input("Please input a list of comma seperated emails:\n")
    r_emails = r_emails.replace(" ","").split(",")

    #Message#
    subject = input("Input your message subject:\n")
    subject = "Subject: " + subject
    main_body = input("Input your main message (New Line = '\\n'):\n")

    message = subject + "\n \n" + main_body

    #Sending the Email#
    while ss == "True" or repeats == 5:
        try:
            smtpObj = smtplib.SMTP(m_server,m_port)
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(m_email, m_pwd)
            smtpObj.sendmail(m_email, r_emails, message)
            smtpObj.close()
            print("Mail Sent Successfully!")
            ss = "False"
        except:
            print("Sending Failed!")
            repeats = repeats + 1

        if input("Send another Email?\n") == "yes":
            send = "True"
            ss = "True"
            repeats = 1
        else:
              send = "False"
              ss = "False"
