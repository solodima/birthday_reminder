import smtplib
import datetime as dt
import random
import pandas as pd

MY_EMAIL = 'your_mail'
MY_PASS = 'your_passwd'

now = dt.datetime.now()
day = now.day
month = now.month


def check_birthday(file_path):
    data = pd.read_csv(file_path)
    birthday_dict = data.to_dict(orient='records')
    for person in birthday_dict:
        if day == int(person['day']) and month == int(person['month']):
            send_a_birthday_card(person['name'], person['email'])


def send_a_birthday_card(person, email):
    random_template = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(random_template) as data:
        template = data.read()
        final_letter = template.replace('[NAME]', person)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject: Happy Birthday!\n\n{final_letter}")


check_birthday('birthdays.csv')
