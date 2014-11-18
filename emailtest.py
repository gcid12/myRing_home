import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

#Next, log in to the server
server.login("rcid@myring.io", "$jaMAIcaSKA!66")

#Send the mail
msg = "\r\n".join([
  "From: rcid@myring.io",
  "To: gcid@myring.io",
  "Subject: Just a message from your Python friend",
  "",
  "Asi es michingon. Ya mandamos correos via python tambien"
  ])
#msg = "\nHello!" # The /n separates the message from the headers
server.sendmail("rcid@myring.io", "gcid@myring.io", msg)
server.quit()
