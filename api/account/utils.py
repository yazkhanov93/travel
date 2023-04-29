import requests
import random
from account.models import CustomUser


def send_otp(username):
    otp = random.randint(1000, 9999)
    user = CustomUser.objects.get(username=username)
    user.otp = otp
    apikey = kz35cd136b7165dd5795029af1191ace1ed868584437d7d548f4d4a232bfc761644da0
    user.save()
    reqUrl = "https://api.mobizon.kz/service/message/sendsmsmessage?recipient={username}&text={otp}&apiKey={apikey}"
    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)"
    }
    payload = ""
    # response = requests.request(
        # "POST", reqUrl, data=payload,  headers=headersList)
    print(otp)


def password_reset_otp(otp, username):
    apikey = kz35cd136b7165dd5795029af1191ace1ed868584437d7d548f4d4a232bfc761644da0
    reqUrl = "https://api.mobizon.kz/service/message/sendsmsmessage?recipient={username}&text={otp}&apiKey={apikey}"
    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)"
    }
    payload = ""
    # response = requests.request(
        # "POST", reqUrl, data=payload,  headers=headersList)
    print(otp)

