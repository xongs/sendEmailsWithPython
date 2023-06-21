# SendEmail
                    
SendEmail is a Python library that provides a simple way to send emails using the SMTP protocol. It allows you to send emails with both plain text and HTML content.

## Features
# - Sends emails using the SMTP protocol.
- Supports both plain text and HTML content.
- Securely authenticates with the email server.
- Handles exceptions that may occur during the email sending process.

## Possíveis erros
Estou trabalhando para melhorar o código, deixando-o mais rápido, mas por enquanto ainda tem alguns erros:
Quando você loga uma conta ('sender_email' & 'sender_password'), ela tem um limite de aproximadamente 15 usos (15 emails), por conta do limite de emails em um curto período do outlook;
Preste atenção em erros de digitação no 'sender_email' e 'sender_password', caso ocorrra um erro de digitação, a função não vai conseguir efetuar a autenticação/login;
Caso nenhum dos erros acima se encaixe no seu problema, pode ser por conta do servidor do outlook.

## Futuras melhoras:
Caso não queira usar sua conta do outlook, estou trabalhando para que seja possível criar um "tempmail" com o user que você quiser, isso dentro da função.

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
