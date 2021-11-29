# pulls top 6 Indices from marketwatch into lists to be used in
# insert_index_data
from bs4 import BeautifulSoup
import requests
import time
import datetime

source = requests.get('https://www.marketwatch.com/investing/index/spx').text

soup = BeautifulSoup(source, 'lxml')

title = soup.title.text
print(title)

alldata = soup.find('div', class_='element element--markets desktop')
table = alldata.find('div', class_='markets__table')
prices = table.find('td', class_='table__cell price')


ticker_list = []
i = 0
for ticker in soup.find_all('td', class_='table__cell symbol'):
    # print(ticker.a.text)
    ticker_list.insert(i, ticker.a.text)
    i = i + 1

print('Full List Ticker:', ticker_list)

index_price_list = []
j = 0
index_price_final = 0
str = ''

for prices in soup.find_all('td', class_='table__cell price'):
    for index_price in prices.find_all('bg-quote'):
        print(index_price.text)
        # print(float(index_price.text))
        str = index_price.text
        str = str.replace(',', '')
        index_price_final = float(str)
        index_price_list.insert(j, index_price_final)
        j = j + 1

print('Full List Index Price:', index_price_list)
# print(len(ticker_list))

ts = []
k = 0
num_tickers = len(ticker_list)

print(num_tickers)
# ts store timestamp of current time
ct = datetime.datetime.now()
print("current time:-", ct)
#ts1 = ct.timestamp()
#print("timestamp:-", ts1)

for k in range(num_tickers):
    print(k)
    print(ct)
    ts.insert(k, ct)

index_data = ticker_list + index_price_list + ts
print('Final index_data', index_data)


def get_list():
    return index_data
