from flask import Flask 
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] ='roselyne.mwaniki@student.moringaschool.com'
app.config['MAIL_PASSWORD'] = 'iibv tdcd pmlk vqhm'
app.config['MAIL_DEFAULT_SENDER'] = 'roselyne.mwaniki@student.moringaschool.com'

mail = Mail(app)


@app.route("/")
def send_email():
    msg = Message(subject='Hello from the other side!', recipients=['christineroselyne636@gmail.com'])
    msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works."
    mail.send(msg)
    return "Message sent!"


if __name__ == '__main__':
    app.run(debug=True)    
