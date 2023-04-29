import requests

r = requests.get(url="https://api.mobizon.kz", headers={"Content-Type": "application/json; charset=utf-8"}, params={
                  "apikey": "kz35cd136b7165dd5795029af1191ace1ed868584437d7d548f4d4a232bfc761644da0", "message":"123", "recipient":"99362859316"})
print(r.text, r.status_code)
