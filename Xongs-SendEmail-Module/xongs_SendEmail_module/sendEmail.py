def SendEmail(sender_email, sender_password, recipient_email, subject, message):
    """Send an email using the SMTP protocol.

    Parameters:
    - sender_email (str): The sender's email address.
    - sender_password (str): The sender's email account password.
    - recipient_email (str): The recipient's email address.
    - subject (str): The email subject.
    - message (str): The email body.

    Raises:
    - smtplib.SMTPException: If an error occurs while sending the email.

    Returns:
    - None: This function doesn't return any value.
    """
    
    # necessary modules
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib
    
    # create a multipart message object
    msg = MIMEMultipart('alternative')
    msg['From'] = str(sender_email)
    msg['To'] = str(recipient_email)
    msg['Subject'] = str(subject)
    
    # create both plain and html versions of the email
    text = 'This is a sample plain text'
    html = f'<html><body><h2>{str(message)}</h2></body></html>'
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)
    
    # smtp server settings
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587
    
    try:
        # create a secured SSL/TLS connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        
        # login to your outlook email
        server.login(str(sender_email), str(sender_password))
        
        # send email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        
        print("The email was sent successfully!") 
        
    except smtplib.SMTPException as e:
        print(f"An error occurred while sending the email: {str(e)}") 
        
    finally:
        # close the connection
        server.quit() 
