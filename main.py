import requests
para = {
  "prompt":"write a code for request library in python and also write in functions"
}
req = requests.post(url='https://q1ldcp2pw8.execute-api.us-east-1.amazonaws.com/dev', json=para)

print(req.text)
