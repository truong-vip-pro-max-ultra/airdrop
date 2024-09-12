import requests
import random
import string

headers = {}

def random_string(length=12):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))
def login(uid):
	url = 'https://tgapp-api.matchain.io/api/tgapp/v1/user/login'
	payload = {
	    "uid": uid,
	    "first_name": random_string(6),
	    "last_name": random_string(7),
	    "username": random_string(8),
	    "tg_login_params": "user=%7B%22id%22%3A7091151155%2C%22first_name%22%3A%22Giang%22%2C%22last_name%22%3A%22Ling%22%2C%22username%22%3A%22truonggiang20012004%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&chat_instance=6979535304877042017&chat_type=sender&auth_date=1726070718&hash=ad7c68f75f96ca7139fc9d0f07aff872c0ffbbb2ad7f601105541fe8345f3040"
	}
	resp = requests.post(url,json=payload,verify=False).json()
	print(resp)
	if 'data' in resp:
		return resp['data']['token']
	return ''
def play():
	while True:
		url = 'https://tgapp-api.matchain.io/api/tgapp/v1/game/play'
		resp = requests.get(url, headers=headers, verify=False).json()['data']
		print(resp)
		game_id = resp['game_id']
		game_count = resp['game_count']
		if game_id == '':
			break
		print(game_id)
		url = 'https://tgapp-api.matchain.io/api/tgapp/v1/game/claim'
		payload = {
		    "game_id": game_id,
		    "point": 220
		}
		resp = requests.post(url,json=payload,headers=headers, verify=False).text
		print(resp)
		if game_count == 0:
			break
def add_task(uid):
	url = 'https://tgapp-api.matchain.io/api/tgapp/v1/daily/task/purchase'
	payload = {"uid": uid, "type": "game"}
	resp = requests.post(url,json=payload,headers=headers,verify=False)
	print(resp.text)
def claim_farming(uid):
	url = 'https://tgapp-api.matchain.io/api/tgapp/v1/point/reward/claim'
	payload = {"uid":uid}
	resp = requests.post(url,json=payload,headers=headers,verify=False)
	print(resp.text)
	url = 'https://tgapp-api.matchain.io/api/tgapp/v1/point/reward/farming'
	resp = requests.post(url,json=payload,headers=headers,verify=False)
	print(resp.text)
def main(uid):
	global headers
	token = login(uid)
	headers = {
		'Authorization': token
	}
	print(token)
	play()
	add_task(uid)
	play()
	claim_farming(uid)
uid = 6514165305
# uid = 6100799736
main(uid)
