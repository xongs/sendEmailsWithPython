from setuptools import setup, find_packages

setup(
    name='Xongs-SendEmail-Module',
    version='1.0.0',
    author='João Carlos C. Zacchello',
    author_email='joao.zacchello@gmail.com',
    description='SendEmail is a Python module that provides a simple way to send emails using the SMTP protocol. It allows you to send emails with plain text and HTML content.',
    long_description="""# SendEmail
                    
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
    )```
         
Make sure to replace sender@example.com with the actual sender email address and sender_password with the sender's password.
For more information and detailed usage instructions, please refer to the GitHub repository.""",
    url='https://github.com/xongs/sendEmailsWithPython',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='send email email module SMTP protocol plain text email HTML email email sending email library Python email email with attachments email authentication email server pip package GitHub repository',
    python_requires='>=2.4',
    install_requires=[
        'email>=3.10.10',
        'smtplib>=8.8.4',
    ],
)