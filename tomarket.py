import requests
def login():
	url = 'https://api-web.tomarket.ai/tomarket-game/v1/user/login'
	payload = {
	  "init_data": "query_id=AAE5RkYEAwAAADlGRgSxtHgW&user=%7B%22id%22%3A6514165305%2C%22first_name%22%3A%22Xuan%22%2C%22last_name%22%3A%22Dieu%22%2C%22username%22%3A%22xuandieu22%22%2C%22language_code%22%3A%22vi%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1726162728&hash=b4a90a6150dfca4ca8a8943f0d3a8795475526f481947cdefcdd844c5088dd50",
	}
	resp = requests.post(url,json=payload)
	try:
		return resp.json()['data']['access_token']
	except:
		return ''
def play(token):
	game_id='59bcd12e-04e2-404c-a172-311a0084587d'
	while True:
		headers = {
			'Authorization': token
		}
		url='https://api-web.tomarket.ai/tomarket-game/v1/user/balance'
		resp = requests.post(url,headers=headers)
		print(resp.text)
		try:
			if resp.json()['data']['play_passes'] == 0:
				break
		except:
			pass

		url='https://api-web.tomarket.ai/tomarket-game/v1/game/play'
		payload = {
		  "game_id": game_id,
		}
		resp = requests.post(url,headers=headers,json=payload)
		print(resp.text)

		while True:
			url='https://api-web.tomarket.ai/tomarket-game/v1/game/claim'
			payload = {
			  "game_id": game_id,
			  "points": 600
			}
			resp = requests.post(url,headers=headers,json=payload)
			print(resp.text)
			try:
				if resp.json()['data']['points']:
					break
			except:
				pass
		# break
token = login()
print(token)
play(token)
