import requests
import os
from twilio.rest import Client
import json

with open("data.json", "r") as file:
    data = json.load(file)
    #print(data) """
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = os.environ.get("API_KEY")
FUNCTION = "TIME_SERIES_DAILY"
INTERVAL = "1min"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
news_parameters = {
       "q": COMPANY_NAME,
       "from": "2025-02-29",
       "sortBy": "popularity",
       "apiKey": NEWS_API_KEY
}

parameters = {
    "function": FUNCTION,
    "symbol": STOCK_NAME,
    #"interval": INTERVAL,
    "apikey": API_KEY

}
"""response = requests.get(STOCK_ENDPOINT, params=parameters)
print(response.status_code)
response.raise_for_status()
data = response.json()
print(data) """


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]


prices = [float(value["4. close"]) for (key, value) in data["Time Series (Daily)"].items()] #retrieving the information from the json
#print(data["Time Series (Daily)"]["2025-02-28"]["4. close"])
#print(data["Time Series (Daily)"]["2025-02-27"]["4. close"])

#TODO 2. - Get the day before yesterday's closing stock price
#already done in todo 1

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(prices[0] - prices[1])
print(difference)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
p_diff = round(((prices[0] - prices[1]) / prices[0]) * 100, 2)
print(p_diff)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if p_diff >= 3 or p_diff <= -3:
    r2 = requests.get(NEWS_ENDPOINT, params=news_parameters)
    #print(r2.status_code)
    r2.raise_for_status()
    data = r2.json()
    top3 = [(article["title"], article["description"]) for article in data["articles"][0:3]]
    #top3_2 = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in data["articles"][0:3]] #another way to solve this part
    #print(top3_2)
    #print(top3)
    #print(top3[0][0])
    if p_diff >= 3:
        check = f" {STOCK_NAME} 🔺 {p_diff}%. \n HEADLINE: {top3[0][0]} \n BRIEF: {top3[0][1]} "
        print(check)
        """message = client.messages.create(
            body=f" {STOCK_NAME} 🔺 {p_diff}%. \n HEADLINE: {str(top3[0][0])}",
            from_="+16612470305",
            to="+573188625128",
        ) """
        """print(message.body)
        message = client.messages.create(
            body=f" BRIEF: {str(top3[0][1])} ",
            from_="+16612470305",
            to="+573188625128",
        )
        print(message.body) """

    elif p_diff <= -3:
        check = f" {STOCK_NAME} 🔺 {p_diff}%. \n HEADLINE: {top3[0][0]} \n BRIEF: {top3[0][1]} "
        #print(check)
        """message = client.messages.create(
            body=f" {STOCK_NAME} 🔺 {p_diff}%. \n HEADLINE: {str(top3[0][0])}",
            from_="+16612470305",
            to="+573188625128",
        )
        print(message.body)
        message = client.messages.create(
            body=f" BRIEF: {str(top3[0][1])} ",
            from_="+16612470305",
            to="+573188625128",
        )
        print(message.body) """

        
    """message = client.messages.create(
    body="Hay pronóstico de lluvia para las próximas 24 horas.",
    from_="+16612470305",
    to="+573188625128",
    ) """

else:
    pass

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.






#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    #

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 
#STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

