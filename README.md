# SendEmail
                    
SendEmail is a Python library that provides a simple way to send emails using the SMTP protocol. It allows you to send emails with both plain text and HTML content.

## Features
# - Sends emails using the SMTP protocol.
- Supports both plain text and HTML content.
- Securely authenticates with the email server.
- Handles exceptions that may occur during the email sending process.

## Possible errors
I'm working to improve the code, making it faster, but for now, there are still some errors:
When you log in with an account ('sender_email' & 'sender_password'), it has a limit of approximately 15 uses (15 emails) due to the email limit in a short period on Outlook;
Pay attention to typing errors in 'sender_email' and 'sender_password'; if there is a typing error, the function won't be able to authenticate/login;
If none of the above errors apply to your problem, it may be due to the Outlook server

## Futuras melhoras:
If you don't want to use your Outlook account, I'm working on making it possible to create a "tempmail" with the username of your choice within the function.

## Usage
Here is an example of how to use SendEmail:

```python
from sendEmail import SendEmail

sendEmail_satisfied = {
    "sender": {
        "sender_email": "sender@OUTLOOK.com",
        "sender_password": "sender_password"
        },
        "recipient_email": "recipient@example.com",
        "subject": "Test email",
        "message": "Hello, this is a test email."
        }
        
SendEmail(
    sendEmail['sender']['sender_email'],
    sendEmail['sender']['sender_password'],
    sendEmail['recipient_email'],
    sendEmail['subject'],
    sendEmail['message']
    )
```
         
Make sure to replace sender@example.com with the actual sender email address and sender_password with the sender's password.
For more information and detailed usage instructions, please refer to the GitHub repository.
