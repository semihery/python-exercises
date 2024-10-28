import requests
import time

dataStartTime = 1704110400000
dataLastTime = 1704110400000
currentTime = 1729087900000
# currentTime = int(round(time.time() * 1000))
# print(currentTime)

base_url = "https://api.binance.com"
endpoint = "/api/v3/klines"
params = {
    "symbol": "TONUSDT",
    "interval": "1m",  # Interval (e.g., 1m, 5m, 1h, 1d)
    "limit": 1000,  # Number of data points to retrieve
    "startTime": 0,  # Start time in UNIX timestamp (optional)
    # "endTime": 0  # End time in UNIX timestamp (optional)
}

while dataLastTime < currentTime:
    avgPriceHistory = []
    params["startTime"] = dataLastTime
    response = requests.get(base_url + endpoint, params=params)
    data = response.json()
    for i in data:
        avgPriceHistory.append((float(i[2])+float(i[3]))/2)
        
    dataLastTime = data[-1][6]
    with open("ton_1704110400000_1729087900000.txt", "a") as file:
        for value in avgPriceHistory:
            file.write(f"{value}\n")