import smtplib

for i in range (0,10):
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login("seu_email", "sua_senha")

	server.sendmail(
		"seu_email",
		"emai_destinatário",
		"corpo_do_email")
	server.quit()
