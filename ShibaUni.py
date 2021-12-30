"""Checks Resy for reservations and alerts on those reservations."""

from requests_html import HTMLSession
import datetime
import argparse
import smtplib, ssl


# Create the parser
parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, required=True)
parser.add_argument('--seats', type=int, required=True)
parser.add_argument('--range', type=int, required=True)
parser.add_argument('--want', type=str, required=True)

# Parse the argument
args = parser.parse_args()

# For Notification Email
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = ""  # Enter your bot's address
password = "" #input("Type your password and press enter: ")
receiver_email = ""  # Enter alert receiver address
message = """\
Subject: Woof, New Rezo!

Hello! \n"""
alert = False

# Restaurant Name, Seats, Date Range
restaurant = args.name
num_seats = args.seats
range = args.range
want = args.want
start_date = datetime.date.today()
end_date = start_date + datetime.timedelta(days=range)
delta = datetime.timedelta(days=1)

data = []

message += f'The following reservation for {restaurant} at {want} is available for dates: \n'
while start_date <= end_date:
    date_formatted = start_date.strftime("%Y-%m-%d")

    #create the session
    session = HTMLSession()

    #define our URL
    url = f'https://resy.com/cities/ny/{restaurant}?date={date_formatted}&seats={num_seats}'

    #use the session to get the data
    r = session.get(url)

    #Render the page, up the number on scrolldown to page down multiple times on a page
    r.html.render(sleep=1, keep_page=True, scrolldown=1)
    page = r.html.text
    start = page.index("Selected Date")
    end = page.index("Need to Know")
    rezo_info = page[start:end]
    if want in rezo_info:
        message += start_date.strftime("%B %d, %Y")
        message += "\n "
        alert = True
    start_date += delta

if alert:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    alert = False
