import smtplib
import datetime as dt
from random import choice

# Global variables

GMAIL = 'smtp.gmail.com'
EMAIL = 'EMAIL'
PASSWORD = 'PASSWORD'
recipient_email = 'RECIPIENT EMAIL'
TITLE = 'Your Weekly Motivation!'
quote = ''

# Get the current day

current_day = dt.datetime.now().weekday()

# Read quotes

with open('./quotes.txt', 'r') as file:
    quotes = file.readlines()

# Check sent quotes

try:
    with open('./quotes_sent.txt', 'r') as file2:
        quotes_sent = file2.readlines()
except FileNotFoundError:
    quotes_sent = []

# Choose the quote; if sent choose next quote in list

not_used = True
while not_used:
    quote = choice(quotes)
    if quotes not in quotes_sent:
        not_used = False

# Save the used quote to the used file

with open('./quotes_sent.txt', 'a') as file3:
    file3.write(quote)

# Create the message

message = f'Subject: {TITLE}\n\n{quote}'

# Send the message only on Fridays
# Mon: 0 - Sun: 6

if current_day == 4:
    with smtplib.SMTP(GMAIL) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=recipient_email,
                            msg=message)


