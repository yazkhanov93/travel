import requests
import random
from account.models import CustomUser

# SMS API 
url = "https://mobizon.kz"

def send_otp(username):# will send otp verification code when user register
    otp = random.randint(1000, 9999)
    user = CustomUser.objects.get(username=username)
    user.otp = otp
    apikey = ""
    user.save()
    reqUrl = "https://api.mobizon.kz/service/message/sendsmsmessage?recipient={username}&text={otp}&apiKey={apikey}"
    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)"
    }
    payload = ""
    response = requests.request(
        "POST", reqUrl, data=payload,  headers=headersList)



def password_reset_otp(otp, username): #send otp verification code when user wants reset password
    apikey = ""
    reqUrl = "https://api.mobizon.kz/service/message/sendsmsmessage?recipient={username}&text={otp}&apiKey={apikey}"
    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)"
    }
    payload = ""
    response = requests.request(
        "POST", reqUrl, data=payload,  headers=headersList)

