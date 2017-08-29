# -*- coding: utf-8 -*-

from okex_sdk import ApiClient
import okex_web as okexWeb
import pandas as pd 


"""
    获取OKEX合约行情数据 
    BTC https://www.okex.com/api/v1/future_ticker.do?symbol=btc_usd&contract_type=this_week
    LTC https://www.okex.com/api/v1/future_ticker.do?symbol=ltc_usd&contract_type=this_week
    
Parameters
------
  symbol:string  虚拟币代码
             btc_usd:比特币    
             ltc_usd :莱特币 

  contract_type:string 合约类型
           this_week:当周   
           next_week:下周   
           quarter:季度     
             
return
-------
  返回值说明：
	buy:买一价
	contract_id:合约ID
	high:最高价
	last:最新成交价
	low:最低价
	sell:卖一价
	unit_amount:合约面值
	vol:成交量(最近的24小时)
  
  
  返回值类型：DataFrame
      
       buy  coin_vol  contract_id        date  day_high  day_low    high   last      low     sell  unit_amount      vol  
0  4328.74         0  20170818012  1502784477         0        0  4477.9   4329.6  4102.64  4328.85          100  3050050  
      

	  
	  """
def get_future_ticker( symbol = 'btc_usd' , contract_type ='this_week'):
	client = ApiClient()
	ticker = client.get_future_ticker(symbol ,contract_type )

	df = pd.DataFrame({
		'date' :  [ ticker['date'] ],
		'buy' :  [ ticker['ticker']['buy'] ],
		'coin_vol' :  [ ticker['ticker']['coin_vol'] ],
		'contract_id' :  [ ticker['ticker']['contract_id'] ],
		'day_high' :  [ ticker['ticker']['day_high'] ],
		'day_low' :  [ ticker['ticker']['day_low'] ],
		'high' :  [ ticker['ticker']['high'] ],
		'last' :  [ ticker['ticker']['last'] ],
		'low' :  [ ticker['ticker']['low'] ],
		'sell' :  [ ticker['ticker']['sell'] ],
		'day_high' :  [ ticker['ticker']['day_high'] ],
		'unit_amount' :  [ ticker['ticker']['unit_amount'] ],
		'vol' :  [ ticker['ticker']['vol'] ],		
		})
	
	return df	
				
		
"""
     获取OKEX合约深度信息 
   
Parameters
------
  symbol:string  虚拟币代码
             btc_usd:比特币    
             ltc_usd :莱特币 

  contract_type:string 合约类型
           this_week:当周   
           next_week:下周   
           quarter:季度     
             
return
-------
  返回值说明：
      price ：价格
      amount ：数量，单位：张
    
  返回值类型：DataFrame
	  
"""	
def get_future_depth( symbol = 'btc_usd' , contract_type ='this_week' , size=5 ):
	client = ApiClient()
	result = client.get_future_depth(symbol ,contract_type,size )
	df_asks = pd.DataFrame(result['asks'], columns=['asks_price', 'asks_amount'] )
	df_bids = pd.DataFrame(result['bids'], columns=['bids_price' , 'bids_amount'] )
	df_merge = pd.merge(df_asks, df_bids,left_index=True, right_index=True )	 	
	
	return df_merge

			
"""
     获取OKEX合约指数信息
   
Parameters
------
  symbol:string  虚拟币代码
             btc_usd:比特币    
             ltc_usd :莱特币 
             
return
-------
  返回值说明：
     future_index: 指数
    
  返回值类型：DataFrame
	  
"""	
def get_future_index( symbol = 'btc_usd'  ):
	client = ApiClient()
	result = client.get_future_index(symbol   )

	df = pd.DataFrame({
	'future_index' :  [ result['future_index'] ],
	})
		
	return df

"""
      获取交割预估价
   
Parameters
------
  symbol:string  虚拟币代码
             btc_usd:比特币    
             ltc_usd :莱特币 
             
return
-------
  返回值说明：
     forecast_price:交割预估价  注意：交割预估价只有交割前三小时返回
    
  返回值类型：DataFrame
	  
"""		
def get_future_estimated_price( symbol = 'btc_usd'  ):
	client = ApiClient()
	result = client.get_future_estimated_price(symbol   )
	df = pd.DataFrame({
		'forecast_price' :  [ result['forecast_price'] ],
	})
	
	return df

	"""
       获取OKEX合约交易记录信息
   
Parameters
------
  symbol:string  虚拟币代码
             btc_usd:比特币    
             ltc_usd :莱特币 
    contract_type
		合约类型: this_week:当周   next_week:下周   quarter:季度          
return
-------
  返回值说明：
     
    
  返回值类型：DataFrame
	  
"""		
def get_future_hold_amount( symbol = 'btc_usd' , contract_type ='this_week' ):
	client = ApiClient()
	result = client.get_future_hold_amount(symbol ,contract_type  )
 
	df = pd.DataFrame({
		'contract_name' : [result[0]['contract_name'] ] ,
		'amount' : [result[0]['amount'] ] ,
	})
 
	
	return df
	
if __name__ == '__main__':
	data = get_future_ticker('btc_usd' ,  'this_week')
	#data = get_future_depth('btc_usd' ,  'this_week'  )
	#data = get_future_index('btc_usd'  ) 
	#data = get_future_estimated_price('btc_usd'  ) 	
	#data = get_future_hold_amount('btc_usd' , 'this_week' )
	#data = okexWeb.get_coin_exchange_rate('ltc_usd')
	#data = okexWeb.get_future_top('ltc_usd')
	print(data)


	