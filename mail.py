import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Use your App Password here
    server.login('cpboys11@gmail.com', 'msrd webk ezdi eiwu')

    server.sendmail('cpboys11@gmail.com', 'technicalnazwa@gmail.com', 'this is a fake mail')
    print('Mail sent successfully')

except Exception as e:
    print('An error occurred:', str(e))

finally:
    server.quit()
