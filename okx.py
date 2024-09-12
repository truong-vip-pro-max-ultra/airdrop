import requests
while True:
	url='https://www.okx.com/priapi/v1/affiliate/game/racer/assess?t=0'
	headers = {
		# 'cookie': 'amp_56bf9d=aa9ba8ce-eade-466c-b053-aa4759ac02a9...1i7jcjsnn.1i7jcum9t.s.0.s; _monitor_extras={"deviceId":"3rXSapnYMqd-uiCnJ8gGaO","eventId":33,"sequenceNumber":33}; ok-ses-id=+TnXti1GxYNIWqwSmspuFZidCsndT/VHFCbv9pvOzgCyU778XeZJZYqj9rLB+pkcx6j0rLtNbIuqYakUORRimhvtSSwjQX5wRYY4GgwLjbiG5NKRBS+kaJQWmfDp/spb; _ga_G0EKWWQGTZ=GS1.1.1726153880.2.1.1726154219.43.0.0; _ga=GA1.2.1594421589.1726105252; _gid=GA1.2.1108047769.1726105252; ok_prefer_currency=%7B%22currencyId%22%3A0%2C%22isDefault%22%3A1%2C%22isPremium%22%3Afalse%2C%22isoCode%22%3A%22USD%22%2C%22precision%22%3A2%2C%22symbol%22%3A%22%24%22%2C%22usdToThisRate%22%3A1%2C%22usdToThisRatePremium%22%3A1%2C%22displayName%22%3A%22USD%22%7D; ok_prefer_udColor=0; ok_prefer_udTimeZone=0; okg.currentMedia=sm; traceId=2140361538950030012; __cf_bm=mK.3oa6YFotrd9H89tZnjdgG.GNaDvgQu.bxrwGU3cQ-1726153879-1.0.1.1-nLE.R04kNMPtmAuJN6oqW9JxVQ7CPZx4j5aSxNnKInC2ANL5eGymnNIDI8z0JHCkdTythcaD8Cm.24GkNSADLw; fingerprint_id=aa9ba8ce-eade-466c-b053-aa4759ac02a9; locale=en_US; devId=aa9ba8ce-eade-466c-b053-aa4759ac02a9; browserVersionLevel=default.289611072994; ok-exp-time=1726104840450; ok_site_info===QfxojI5RXa05WZiwiIMFkQPx0Rfh1SPJiOiUGZvNmIsIiTWJiOi42bpdWZyJye',
		'X-Telegram-Init-Data': 'user=%7B%22id%22%3A6514165305%2C%22first_name%22%3A%22Xuan%22%2C%22last_name%22%3A%22Dieu%22%2C%22username%22%3A%22xuandieu22%22%2C%22language_code%22%3A%22vi%22%2C%22allows_write_to_pm%22%3Atrue%7D&chat_instance=1944922022095358963&chat_type=private&start_param=linkCode_96869955&auth_date=1726153894&hash=3006cab6df6bc7a1127d5263377fdaa2ff796d8074a3c39ba32e4e84c4de1433'
		# 'X-Telegram-Init-Data': 'user=%7B%22id%22%3A6492262535%2C%22first_name%22%3A%22%E2%80%9CHow%20to%20hack%E2%80%9D%22%2C%22last_name%22%3A%22I%20don%E2%80%99t%20know%22%2C%22username%22%3A%22idontknowhowtohack%22%2C%22language_code%22%3A%22en%22%7D&chat_instance=-2784148336546465547&chat_type=sender&auth_date=1726155327&hash=7882a2cebe4a303262265f500a98f276502189767a9b1922cd81c2b56acb4f57'
	}
	payload = {
		'predict': 1
	}
	p = requests.post(url,headers=headers,json=payload)
	print(p.text)