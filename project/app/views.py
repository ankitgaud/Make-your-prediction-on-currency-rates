import os
import json
import time
import requests
import pandas as pd 
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .json_api import json_api, json_api_three_month
from .search_node import printdate, Current_value_of_dollar
from .set_result import fcast_pridict
# Create your views here.

def Home(request):
	data = json_api()
	for a in data["HistoricalPoints"]:
		time1 = time.strftime("%a %d %b %Y", time.gmtime(a["PointInTime"] / 1000.0))
		
		a["PointInTime_UTC"] = time1
		a["RevInterbankRate"] = "%.5f"%(1/a["InterbankRate"])


	return render(request, "home.html", {"context":data["HistoricalPoints"]})

def make_pridiction(request):
	data = json_api_three_month()
	for a in data["HistoricalPoints"]:
		time1 = time.strftime("%a %d %b %Y", time.gmtime(a["PointInTime"] / 1000.0))
	
		a["PointInTime_UTC"] = time1
		a["RevInterbankRate"] = "%.5f"%(1/a["InterbankRate"])
		context = {"context":data["HistoricalPoints"]}
	return render(request, "Input_page.html", context)

def pridict(request):#, Base_currency, Target_currency, Amount, Max_wait_time, start_date):
	if request.method == 'GET':
		Base_currency = request.GET.get('Base_currency')
		Target_currency = request.GET.get('Target_currency')
		Amount = request.GET.get('Amount')
		Max_wait_time = request.GET.get('Max_wait_time')
		start_date = request.GET.get('start_date')
		
		objdate = datetime.strptime(str(start_date), '%Y-%m-%d')
		date12 = datetime.strftime(objdate, '%d-%m-%Y')		
		
		set_result1 = {'ds': None, 'yhat': None}

		if Base_currency == 'INR' and Target_currency == 'USD':
			set_result1 = fcast_pridict(date12, int(Max_wait_time))
			set_result1 = dict(set_result1)
			set_result1['ds'] = set_result1['ds'].strftime("%d/%m/%Y")
			dollar_value = Current_value_of_dollar()
			Amount = (float(Amount))/dollar_value
			#set_result1['yhat'] = str(Amount)
			set_result1['yhat'] = str("%.3f"%((set_result1['yhat'] /dollar_value)*Amount))+" $"
		elif Base_currency == 'USD' and Target_currency == 'INR':
			set_result1 = fcast_pridict(date12, int(Max_wait_time))
			set_result1 = dict(set_result1)
			set_result1['ds'] = set_result1['ds'].strftime("%d/%m/%Y")
			Amount = float(Amount)			
			set_result1['yhat'] = str("%.3f"%(set_result1['yhat'] * Amount))+" $"
		else:
			set_result1['ds']="something went wrong"
			set_result1['yhat']="something went wrong"	
				
		print(type(set_result1))

		return HttpResponse("Date : "+set_result1['ds']+"<br> Amount : "+set_result1['yhat'])



