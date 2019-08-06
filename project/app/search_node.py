import json
import requests
import time
import datetime



def json_api_three_month():
	# api of 3 months/per day
	data = requests.get("https://api.ofx.com/PublicSite.ApiService/SpotRateHistory/3month/USD/INR?DecimalPlaces=2&ReportingInterval=daily&format=%27json%27")

	data = json.loads(data.text)
	return data

def printdate(date12):

	date = json_api_three_month()

	flag = 0
	date1 = []
	for a in date['HistoricalPoints']:

		time1 = time.strftime("%d-%m-%Y", time.gmtime(a['PointInTime'] / 1000))
		if date12 == time1 or flag == 1:

			date1.append(a)
			flag = 1	
		else:
			pass
	return json.dumps(date1)	

def Current_value_of_dollar():
	data = requests.get("https://api.ofx.com/PublicSite.ApiService/SpotRateHistory/3month/USD/INR?DecimalPlaces=2&ReportingInterval=daily&format=%27json%27")

	data = json.loads(data.text)
	n = len(data['HistoricalPoints'])
	return data['HistoricalPoints'][n-1]['InterbankRate']			


