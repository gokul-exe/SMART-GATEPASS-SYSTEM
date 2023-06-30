import smtplib
from email.message import EmailMessage
def mail(message):
        # SMTP server configuration
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        # Email credentials
        sender_email = 'tamilinsta28@gmail.com'
        sender_password = 'fsmupokaesgojmns'
        recipient_email = 'gokulsubramanian241@gmail.com'

        # Email content
        subject = "THIS IS A AUTOMATED MESSAGE FROM -GATEPASS SYSTEM🧭"
        #message = "This mail is to inform that "+user_name+" of "+dept+ " Gone Out Of the College Through Gate-1"

        # Create an instance of EmailMessage
        msg = EmailMessage()

        # Set the subject and message
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg.set_content(message)

        # Add the image attachment
        '''image_path = r'images/'+image_num+'.png'
        with open(image_path, 'rb') as f:
            image_data = f.read()
            image_name = image_path.split('/')[-1]  # Extract the image file name from the path
            msg.add_attachment(image_data, maintype='image', subtype='png', filename=image_name)'''

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        try:
             # Login to the email account
            server.login(sender_email, sender_password)

            # Send the email
            server.send_message(msg)

             # Close the connection
            server.quit()

            #print('Email sent successfully!')
        except smtplib.SMTPAuthenticationError:
                print('Authentication failed. Please check your email credentials.')
        except Exception as e:
                print(f'An error occurred while sending the email: {e}')


if __name__=="__main__":
    mail()
