import smtplib
 
server = smtplib.SMTP('smtp-mail.outlook.com', 587)
server.starttls()
server.login("z5110198@ad.unsw.edu.au", "61135debaDeep2018")

msg = "YOUR MESSAGE!"
server.sendmail("z5110198@unsw.edu.au", "z5110198@unsw.edu.au", msg)
server.quit()
