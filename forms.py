from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField
 
class ContactForm(Form):
  name = TextField("your name")
  email = TextField("your email")
  subject = TextField("New Record")
  message = TextAreaField("The new message")
  submit = SubmitField("Send")
