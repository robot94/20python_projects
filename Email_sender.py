#This is an Email sender application

from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'oussaidyoussef94@gmail.com'
email_password = 'jdlxuegnvwsuouvp'

email_reciver = 'oussaid-youssef@outlook.fr'

subject = 'Your Devops Jurny'

body = """

Hello Youssef, 

I am contacting you today to check on you and to ensure you that you will be a Cloud and Devops Engineer Inchaa lah
Please be aware that to achive your goal you will need to learn the folowing subjects:

    - Linux Administration : RHCSA and RHCE
    - Cloud infrastructure : AWS, Azure, GCP
    - Programing language :  Python, NodeJS
    - Containers : Docker and kubernetes
    - CI/CD
    - Configuration Management: Ansible, Terraform, Chef
    - Networking : CCNA and CCNP
    - Web Servers: Apache Tomcat and Nginex

I wich you all the luk in your Jurny

Best regards,
Youssef from the future

"""

em = EmailMessage()
em['From'] = email_sender
em['TO'] = email_reciver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())