import time
import requests
from dotenv import load_dotenv
import os


load_dotenv(override=True)
API_KEY = os.getenv("API_KEY")

# For getting latest updates
# response = requests.get(base_url)
# response = response.json()
# latest_id = response['result'][-1]['update_id']
# parameters = {
#     'offset': latest_id
# }
# resp = requests.get(base_url, params=parameters)
# print(resp.text)


# Sending message
# texts = ['Nice to meet you', "I am a bot", "Hello there"]
# 
# for text in texts:
#     parameters = {
#     'chat_id': '368096415',
#     'text': text
#     }
#     response = requests.get(base_url, params=parameters)
#     print(response.text)
#     time.sleep(3)

# Sending photo and document
base_url = f'https://api.telegram.org/bot{API_KEY}/sendDocument'
parameters = {
    'chat_id': '368096415',
    'caption': 'Here is a document for you'
}
file = {
    'document': open(r'C:\Users\AH CHUN\Documents\TBot\my-first-tgbot\bot.py', 'rb')
}
response = requests.post(base_url, params=parameters, files=file)
print(response.text)