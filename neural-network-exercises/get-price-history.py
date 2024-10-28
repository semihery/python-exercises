import requests

base_url = "https://api.binance.com"
endpoint = "/api/v3/klines"
params = {
    "symbol": "TONUSDT",
    "interval": "1m",  # Interval (e.g., 1m, 5m, 1h, 1d)
    "limit": 1000,  # Number of data points to retrieve
    #"startTime": 1725391587067,  # Start time in UNIX timestamp (optional)
    #"endTime": 1725392587067  # End time in UNIX timestamp (optional)
}

response = requests.get(base_url + endpoint, params=params)
data = response.json()
# print(data)

avgPriceHistory = []
for i in data:
    avgPriceHistory.append((float(i[2])+float(i[3]))/2)

print(avgPriceHistory)