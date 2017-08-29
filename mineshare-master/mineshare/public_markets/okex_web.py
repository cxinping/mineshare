# -*- coding: utf-8 -*-

import requests
import pandas as pd     
from bs4 import BeautifulSoup

"""	
 查询平均汇率和历史汇率
 https://www.okex.com/futures-btc-index.html
"""	
def get_coin_exchange_rate( contract_type:str ):
	btc_url = 'https://www.okex.com/futures-btc-index.html'
	ltc_url =  'https://www.okex.com/futures-ltc-index.html'
	
	if( contract_type == 'btc_usd'):
		url = btc_url
	elif( contract_type == 'ltc_usd'):
		url = ltc_url		
	else:
		return None
		
	headers = { 
			   'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0' ,           
			   }

	response = requests.post(url , headers=headers )	
	return parse_exchage_rate_web( response.text )

def parse_exchage_rate_web(html):
	soup = BeautifulSoup( html , "lxml" )
	averageRateDiv = soup.find_all( 'div', class_ ='futureMarkBody' )[1] 
	d1 = []
	d2 = []
	d3 = []

	for tr in averageRateDiv.findAll('tr'): 
		tds = tr.findAll('td') 
			#print(td.getText() )
		#print(  len( tds ) )
		if(len( tds ) > 0  ):
			d1.append( tds[0].getText() )
			d2.append( tds[1].getText() )
			d3.append( tds[2].getText() )

	dt = pd.DataFrame( {
		'date' : d1,
		'exchangeRate' : d2,
		'twoWeekAverage' : d3
	} )
	return dt 

"""	
查询BTC/LTC 合约持仓排行榜
  
https://www.okex.com/future/futureTop.do?type=0&symbol=0
 
"""	
 
def get_future_top( contract_type:str ):
	btc_url =  'https://www.okex.com/future/futureTop.do?type=0&symbol=0'
	ltc_url =  'https://www.okex.com/future/futureTop.do?type=0&symbol=1'
	
	if( contract_type == 'btc_usd'):
		url = btc_url
	elif( contract_type == 'ltc_usd'):
		url = ltc_url		
	else:
		return None
		
	headers = { 
			   'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0' ,           
			   }

	response = requests.post(url , headers=headers )
		
	return parse_future_top(  response.text )

def parse_future_top(html):
	soup = BeautifulSoup( html , "lxml" )
	divs = soup.find_all( 'div', class_ ='futureIndexTable' )[0] 	

	date_list = []
	openInterest1 = [] 	
	openInterest2 = [] 	
	openInterest3 = [] 	
	openInterest4 = [] 	
	openInterest5 = [] 	
	openInterest6 = [] 	
	topNum = []
	
	for idx, tr in enumerate(soup.find_all('tr')):
		if idx == 0:		
			ths = tr.find_all('th')
			#print( 	ths[0].string )
			date_list.append( ths[0].string )
			date_list.append( ths[1].string )
			date_list.append( ths[2].string )
			date_list.append( ths[3].string )	
			date_list.append( ths[4].string )
			date_list.append( ths[5].string )	
		elif idx >=2:
			#print("======== idx=%s", idx )
			topNum.append( idx -1  )
			tds = tr.find_all('td')
			openInterest1.append( tds[1].string.strip())
			openInterest2.append( tds[3].string.strip())
			openInterest3.append( tds[5].string.strip())		
			openInterest4.append( tds[7].string.strip())
			openInterest5.append( tds[9].string.strip())		
			openInterest6.append( tds[11].string.strip())
			
			tds = tr.find_all('td')			
		
	data1={'date':date_list[0],'openInterest':openInterest1,'topNum':topNum}
	df1 = pd.DataFrame(data1)

	data2={'date':date_list[1],'openInterest':openInterest2,'topNum':topNum}
	df2 = pd.DataFrame(data2)

	data3={'date':date_list[2],'openInterest':openInterest3,'topNum':topNum}
	df3 = pd.DataFrame(data3)

	data4 ={'date':date_list[3],'openInterest':openInterest4,'topNum':topNum}
	df4 = pd.DataFrame(data4)

	data5 ={'date':date_list[4],'openInterest':openInterest5,'topNum':topNum}
	df5 = pd.DataFrame(data5)

	data6 ={'date':date_list[5],'openInterest':openInterest6,'topNum':topNum}
	df6 = pd.DataFrame(data6)
	
	df = df1.append(df2).append(df3).append(df4).append(df5).append(df6)      
	#print( df  )	
	return df
	
"""		
	查询总持仓量
	
	date 日期
	Holding 持仓量
	Ranking 排名
	
"""	
		
	
if __name__ == '__main__':
	#data= get_coin_exchange_rate('btc_usd')
	data = get_future_top('btc_usd')
	
	#print( data )
	
	