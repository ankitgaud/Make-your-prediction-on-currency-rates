
<h1 style="text-align: center;"><u>MAKE PREDICTION FOR FUTURE BASED ON HISTORICAL CURRENCY EXCHANGE RATES</u></h1>
<h3><u>Implementation Details:</u></h3>
<ul>
  <li><b>Languages:</b> Python, Javascript</li>
  <li><b>Frameworks/library:</b> Django, fbprophet, pandas, json, requests, ajax, jquery, bootstrap</li>
</ul>
<br>
<h3><u>Tasks Completed:</u></h3>
<ul>
  <li>Print currency conversion rate more than the last 20 years with help of open-source api.</li>
  <li>We can make predict for future date after the analysis historical currency exchange rates.</li>
  <li>Input for prediction are :
  	<ul>
  		<li>Base currency</li>
  		<li>Target currency</li>
  		<li>start time(past date for analysis historical exchange rate) </li>
  		<li>waiting time(days after you can withdrawl your money)</li>
  		<li>Amount</li>	
  	</ul>
  </li>
  <li>Currency rates update daily</li>
  <li>Use bootstrap to make responsive web pages.</li>
  <li>I used time series forcast to predict for the future date.</li>
</ul>
<br>
<h3><u>Installation:</u></h3>
<ul>
  <li>Use pip or conda to install all above python-libraries</li>
  <li>Run python File: python manage.py runserver port_name(default-8000)</li>
  <li>Access on localhost:8000 or (port_name)/</li>
  <li>Make sure internet connection</li>
</ul>
<h3><u>Functions:</u></h3>
<p>(for Django developer is not hard to understand)</p>
<ul><b>In app/view.py</b>
	<li><u>Home()</u> - It renders home page and sends the dictionary file of rate conversion records.</li>
	<li><u>make_pridiction()</u> - It renders the second page where users can make prediction.</li>
	<li><u>pridict()</u> - When User enters required enteries and he clicks predict button then this <br>function would be call and give responses as a result.</li>
</ul>

<h3><u>Challenging part</u></h3>
<ul>
	<li>I got json file from open-source api.</li>
	<li>This file provides data of last more than 20 years.</li>
	<li>Prediction is not easy because data(json file) updates daily.</li>
	<li>Users can select any date for prediction. But we have large historical data and <br>I used 90 days data for prediction. If, User select last 50 days then data of last<br> 50 days would be selected from dataset and train. Data would be trained for every different date.</li>
</ul>

