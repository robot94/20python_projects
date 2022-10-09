import requests


resp = requests.post('https://textbelt.com/text', {
  'phone': '+212642801225',
  'message': 'Hello Youssef',
  'key': 'textbelt',
})

#print(resp.json())