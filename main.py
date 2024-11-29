import requests
import random
import hashlib

down = float(input('Enter download speed (or press enter to use random): ') or random.randint(1000, 5000)) * 1000
up = float(input('Enter upload speed (or press enter to use random): ') or random.randint(1000, 5000)) * 1000
ping = int(input('Enter ping (or press enter to use random): ') or random.randint(0, 20))
server = int(input('Enter server ID (or press enter to use default): ') or 6601)
accuracy = 8

headers = {
    'POST /api/api.php HTTP/1.1': '',
    'Host': 'www.speedtest.net',
    'User-Agent': 'Speedtest',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.speedtest.net',
    'Referer': 'https://www.speedtest.net',
    'Connection': 'Close'
}

post_data = {
    'startmode': 'recommendedselect',
    'recommendedserverid': server,
    'serverid': server,
    'promo': '',
    'upload': up,
    'download': down,
    'ping': ping,
    'accuracy': accuracy,
    'hash': hashlib.md5(f"{ping}-{up}-{down}-297aae72".encode('utf-8')).hexdigest()
}

response = requests.post('https://www.speedtest.net/api/api.php', headers=headers, data=post_data)

data = response.text
for chunk in data.split('&'):
    params = chunk.split("=")
    if len(params) > 1 and requests.utils.unquote(params[0]) == 'resultid':
        result_id = requests.utils.unquote(params[1])
        print(f'<a href="https://speedtest.net/result/{result_id}"><img src="https://speedtest.net/result/{result_id}.png" alt=""/></a>')
        break
