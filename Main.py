import requests

api_key = 'YOUR API'
symbol = 'TSLA'

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()['Time Series (Daily)']
    latest_date = list(data.keys())[0]
    latest_close_price = float(data[latest_date]['4. close'])
    prev_date = list(data.keys())[1]
    prev_close_price = float(data[prev_date]['4. close'])
    if latest_close_price > prev_close_price:
        print(f'{symbol} stock is trending upwards.')
    else:
        print(f'{symbol} stock is not trending upwards.')
else:
    print(f'Request failed with status code {response.status_code}')
