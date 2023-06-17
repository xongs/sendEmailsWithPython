# SendEmail
                    
SendEmail is a Python library that provides a simple way to send emails using the SMTP protocol. It allows you to send emails with both plain text and HTML content.

## Features
# - Sends emails using the SMTP protocol.
- Supports both plain text and HTML content.
- Securely authenticates with the email server.
- Handles exceptions that may occur during the email sending process.

## Installation
You can install SendEmail using pip:
pip install SendEmail

## Usage
Here is an example of how to use SendEmail:

```python
from sendEmail import SendEmail

sendEmail = {
    "sender": {
        "sender_email": "sender@example.com",
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
