import requests

message = input('Enter a Message: ')
number = input('Enter the phone number: ')


payload = {'number': number, 'message': message}
r = requests.post("http://textbelt.com/text", data=payload)
if r.json()['success']:
    print('Success!')
else:
    print('Error!')