from fbprophet import Prophet
import pandas as pd
import requests
import json
import time
import datetime


def json_api_three_month():
	# api of 3 months/per day
	data = requests.get("https://api.ofx.com/PublicSite.ApiService/SpotRateHistory/3month/USD/INR?DecimalPlaces=2&ReportingInterval=daily&format=%27json%27")

	# api of all time and per day
	#data = requests.get("https://api.ofx.com/PublicSite.ApiService/SpotRateHistory/allTime/USD/INR?DecimalPlaces=6&ReportingInterval=daily&format=%27json%27")
	data = json.loads(data.text)
	return data

def printdate(date12):

	date = json_api_three_month()

	flag = 0
	date1 = []#{"CurrentInterbankRate":68.8255,"CurrentInverseInterbankRate":0.014529,"Average":47.217329,"HistoricalPoints":[]}
	for a in date['HistoricalPoints']:

		time1 = time.strftime("%d-%m-%Y", time.gmtime(a['PointInTime'] / 1000))
		#time2 = time.strftime("%a %d %b %Y", time.gmtime(a['PointInTime'] / 1000))
		if date12 == time1 or flag == 1:
			#print(time2," -- ",a['InterbankRate'])
			#a['PointInTime'] =  time2
			date1.append(a)
			flag = 1	
		else:
			#del a
			pass
	return json.dumps(date1)

def fcast_pridict(start_time, max_waiting_time):
	#max_waiting_time = 20
	data = printdate(start_time)
	# print(data)
	df = pd.read_json(str(data), orient='records')
	frame = df.apply(pd.Series)
	data =  frame#pd.concat([df, frame], axis=1).drop(['HistoricalPoints'], axis=1)

	series = data[['PointInTime', 'InterbankRate']]
	series.columns = ['ds', 'y']	
	series['ds'] = series['ds']/1000
	series['ds'] = list(map(int, series['ds']))
	series['ds'] = pd.to_datetime(series['ds'], unit='s')

	m = Prophet(daily_seasonality=True)
	m.fit(series)
	future = m.make_future_dataframe(periods=max_waiting_time)

	forecast = m.predict(future)
	forecast = forecast[['ds', 'yhat']]

	res = forecast[-max_waiting_time:].loc[forecast[-max_waiting_time:]['yhat'].idxmax()]
	return res

#print(fcast_pridict("25-07-2019", 10))	

