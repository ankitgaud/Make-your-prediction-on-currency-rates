import json
import requests
import time

def json_api():
	
	# api of 3 months/per day
	#data = requests.get("https://api.ofx.com/PublicSite.ApiService/SpotRateHistory/3month/USD/INR?DecimalPlaces=2&ReportingInterval=daily&format=%27json%27")

	# api of all time and per day
	data = requests.get("https://api.ofx.com/PublicSite.ApiService/SpotRateHistory/allTime/USD/INR?DecimalPlaces=6&ReportingInterval=daily&format=%27json%27")
	data = json.loads(data.text)
	return data

#time1 = time.strftime("%a %d %b %Y", time.gmtime(time / 1000.0))	

def json_api_three_month():
	# api of 3 months/per day
	data = requests.get("https://api.ofx.com/PublicSite.ApiService/SpotRateHistory/3month/USD/INR?DecimalPlaces=2&ReportingInterval=daily&format=%27json%27")

	# api of all time and per day
	#data = requests.get("https://api.ofx.com/PublicSite.ApiService/SpotRateHistory/allTime/USD/INR?DecimalPlaces=6&ReportingInterval=daily&format=%27json%27")
	data = json.loads(data.text)
	return data	

#print(json_api_three_month())	