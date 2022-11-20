from flask import Flask
from flask_mail import Mail, Message
   
app = Flask(__name__)
mail = Mail(app) # instantiate the mail class
   
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '510919205023@smartinternz.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
   
# message object mapped to a particular URL ‘/’
@app.route("/Email")
def index():
   send = msg
   msg = Message(
                'Hello',
                sender ='510919205023@smartinternz.com',
                recipients = ['']
               )
   msg.body = 'This mail is for...'
   mail.send(msg)
   send = (msg)
   return 'send'

   
if __name__ == '__main__':
   app.run(debug = True)