#!/usr/bin/python3

# импорт нужных модулей для работы с почтой
import smtplib
import sys


def mail(to, subject, text):
    # инициализируем наши данные
    gmail_user = "user@gmail.com"
    gmail_pwd = "password"
    msg = "Subject: %s\r\nFrom: %s\r\nTo: %s\r\n\r\n" % (subject, gmail_user, to)
    msg += text

    # инициализируем smtp сервер и отправляем письмо
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg)
    mailServer.quit()

if __name__ == '__main__':
    mail(sys.argv[1], sys.argv[2], sys.argv[3])
