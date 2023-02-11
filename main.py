import smtplib
import datetime as dt

# Global variables

GMAIL = 'smtp.gmail.com'
EMAIL = 'EMAIL'
PASSWORD = 'PASSWORD'
recipient_email = 'RECIPIENT EMAIL'
TITLE = 'Your Weekly Motivation!'
quote = ''

# Get the current day

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
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
i = 0
while not_used:
    if quotes[i] not in quotes_sent:
        quote = quotes[i]
        not_used = False
    else:
        i += 1

# Save the used quote to the used file

with open('./quotes_sent.txt', 'a') as file3:
    file3.write(quote)

# Create the message

message = f'Subject: {TITLE}\n\n{quote}'

# Send the message only on Fridays

if weekdays[current_day] == 'Friday':
    with smtplib.SMTP(GMAIL) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=recipient_email,
                            msg=message)


