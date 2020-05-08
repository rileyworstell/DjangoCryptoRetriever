from django.shortcuts import render
import requests
import json
from datetime import datetime
from .models import TopCurrencies


#https://www.alphavantage.co/support/#api-key
#F1MHJET6QCQIXARW
def home(request):
    print("home")
    if request.method == 'POST':
        try:
            ticker = request.POST['ticker']
            api_request = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=" + ticker + "&to_currency=USD&apikey=F1MHJET6QCQIXARW")
            api = json.loads(api_request.content)
            dataBlock = api['Realtime Currency Exchange Rate']
            code = dataBlock['1. From_Currency Code']
            price = dataBlock['5. Exchange Rate']
        except Exception as e:
            ticker = "BTC"
            dataBlock = "Error"
            code = ""
            price=""
        return render(request, 'home.html', {'dataBlock': dataBlock, 'code': code, 'price': price })
    else:
        return render(request, 'home.html', {'ticker': "Enter a Crypto Symbol"})
    

def about(request):
    return render(request, 'about.html', {})

def topCurrencies(request):
    currencies = TopCurrencies.objects.all()
    arr = []
    tickerArr = []
    for i in currencies:
        try:
            tickerArr.append(i.ticker)
            api_request = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=" + i.ticker + "&to_currency=USD&apikey=F1MHJET6QCQIXARW")
            api = json.loads(api_request.content)
            api = api['Realtime Currency Exchange Rate']
            api = api['5. Exchange Rate']
            arr.append(api)
        except Exception as e:
            continue
    print(tickerArr)
    print(arr)
    return render(request, 'topCurrencies.html', {'currencies': currencies,'arr':arr,'tickerArr':tickerArr})

