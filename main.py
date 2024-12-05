import requests
from twilio.rest import Client
from datetime import datetime
import pytz
import os

# US TIME ZONE
US_timezone = pytz.timezone("US/Eastern")
date_now = datetime.now(US_timezone)

#REAL TIME DATE OF US
formatted_month = date_now.strftime("%Y-%m-%d")
formatted_month_text = date_now.strftime("%B %d, %Y")

stock_key = os.getenv("STOCK_KEY")
news_key = os.getenv("NEWS_KEY")


news_url = "https://newsapi.org/v2/everything"

news_params = {
    "q": "IBM Stock",
    "sortBy": "publishedAt",
    "language": "en",
    "apiKey": news_key
}


# STOCK API
response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo")
response.raise_for_status()
stock = response.json()



# NEWS API
response = requests.get(news_url, news_params)
response.raise_for_status()
news = response.json()

test = "2024-12-02"
test_news = "2024-12-01"

def get_stock(news):
    content = news['articles'][0]['content']
    sentences = content.split('. ')
    get_published_at = (news["articles"][0]["publishedAt"])
    news_date_only = get_published_at.split('T')[0]
    if test_news == news_date_only:
        return f"Source: {news['articles'][1]['source']['name']}\n\n {news['articles'][1]['title']}\n\n {'. '.join(sentences[:3]) + '.'}\n"
    else:
        return "There's no news as of now!"


stock_news = get_stock(news)



# -- PRINT THE NEWS FORMATTED DATE --
get_published_at = (news["articles"][0]["publishedAt"])
news_date_only = get_published_at.split('T')[0]


get_published_at1 = (news["articles"][1]["publishedAt"])
news_date_only1 = get_published_at1.split('T')[0]


name = news["articles"][0]["source"]["name"]
title = news["articles"][0]["title"]
content = news["articles"][0]["content"]


#get data1 index 0 of time series
first_date = list(stock["Time Series (Daily)"].keys())[0]
first_data = stock["Time Series (Daily)"][first_date]
save_data_high_first = (first_data["4. close"])


#get data2 index 1 of time series
second_date = list(stock["Time Series (Daily)"].keys())[1]
second_data = stock["Time Series (Daily)"][second_date]
save_data_high_second = (second_data["4. close"])

percentage_change = ((float(save_data_high_first) - float(save_data_high_second)) / float(save_data_high_second)) * 100

CONTENT_IF_INCREASE = f"IBM (International Business Machines) stock price increase from {save_data_high_first} to {save_data_high_second} 📈"
INCREASE_PERCENT = f"Percentage increase: {percentage_change:.2f}%"

CONTENT_IF_DECREASE = f"IBM (International Business Machines) stock price decrease from {save_data_high_second} to {save_data_high_first} 📉"
DECREASE_PERCENT = f"Percentage decrease: {percentage_change:.2f}%"

def send_text_in_increase():
    try:
        body_increase = f"Date: {formatted_month_text}\n\n {CONTENT_IF_INCREASE} {INCREASE_PERCENT}\n\n {stock_news}"
        account_sid = os.getenv("ACCOUNT_SID")
        auth_token = os.getenv("AUTH_TOKEN")
        twilio_pn = os.getenv("TWILIO_PN")
        sample_number = os.getenv("SAMPLE_NUMBER")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body = body_increase,
            from_= twilio_pn,
            to = sample_number
        )
        print(f"send text with increase sent: {message.sid}")
    except Exception:
        print("No message sent!")


def send_text_in_decrease():
    try:
        body_increase = f"Date: {formatted_month_text}\n\n {CONTENT_IF_DECREASE} {DECREASE_PERCENT}\n\n {stock_news}"
        account_sid = os.getenv("ACCOUNT_SID")
        auth_token = os.getenv("AUTH_TOKEN")
        twilio_pn = os.getenv("TWILIO_PN")
        sample_number = os.getenv("SAMPLE_NUMBER")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body = body_increase,
            from_= twilio_pn,
            to = sample_number
        )
        print(f"send text with decrease sent: {message.sid}")
    except Exception as error :
        print(f"No message sent! error: {error}")

def send_text_no_changes():
    try:
        body_increase = f"No price changes as of {formatted_month_text}"
        account_sid = os.getenv("ACCOUNT_SID")
        auth_token = os.getenv("AUTH_TOKEN")
        twilio_pn = os.getenv("TWILIO_PN")
        sample_number = os.getenv("SAMPLE_NUMBER")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body = body_increase,
            from_= twilio_pn,
            to = sample_number
        )
        print(f"send text with no changes sent: {message.sid}")
    except Exception as error :
        print(f"No message sent! error: {error}")

print(stock["Time Series (Daily)"])
print(formatted_month)


if test in stock["Time Series (Daily)"]:
    if save_data_high_first > save_data_high_second:
        send_text_in_increase()
    elif save_data_high_first < save_data_high_second:
        send_text_in_decrease()
    else:
        print("Price stock value stayed the same")
elif test not in stock["Time Series (Daily)"]:
    send_text_no_changes()









