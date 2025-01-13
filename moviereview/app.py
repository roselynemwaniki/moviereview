from flask import Flask 
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'johndoe@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-password'

mail = Mail(app)

@app.route('/')
def send_email():
    msg = Message('Hello', sender='johndoe@gmail.com', recipients=['roselynemwaniki@gmail.com'])
    msg.body = 'This is a test email'
    mail.send(msg)
    return 'Email sent'

if __name__ == '__main__':
    app.run(debug=True)


    


