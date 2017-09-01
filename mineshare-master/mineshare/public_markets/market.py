# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from .bitstar_sdk import ApiClient

import pandas as pd 
#import config as cf

def sayHello():
	print('---- market hello')

"""
    获取Ticker信息
Parameters
------
  businessType:string  业务类型代码
              swap-btc-cny　 比特币对人民币现货合约
              swap-eth-cny　 以太坊对人民币现货合约
              swap-etc-cny　 以太经典对人民币现货合约
              swap-ltc-cny　 莱特币对人民币现货合约
              
return
-------
  DataFrame
      {'date': 1502359905541, 'buy': 22406.4, 'high': 22698.4, 'last': 22406.8, 'low': 21541.1, 'sell': 22407, 'vol': 2197.9323000002814}
      
额外说明：
vol为数字货币的数量，data为long型
      
"""
def get_coin_ticker( businessType = 'swap-btc-cny' ):
	client = ApiClient( '',''  )
	ticker = client.get_ticker(businessType)
	
	df = pd.DataFrame({
		'date' :  [ ticker['date'] ],
		'buy' :   [ ticker['buy'] ],
		'high' :  [ ticker['high'] ],
		'last' :  [ ticker['last'] ],
		'low' :   [ ticker['low'] ],
		'sell' :  [ ticker['sell'] ],	
		'vol' :   [ ticker['vol'] ]	
	})
	
	#print(df )
	return df	
		
"""
    获取深度信息
Parameters
------
  businessType:string  业务类型代码
              swap-btc-cny　 比特币对人民币现货合约
              swap-eth-cny　 以太坊对人民币现货合约
              swap-etc-cny　 以太经典对人民币现货合约
              swap-ltc-cny　 莱特币对人民币现货合约
			  
  size：需要获取的深度数量，非必填，默认买卖盘各50条.  
  
return
-------
  DataFrame
    
	
      
额外说明：
asks为卖盘，bids为买盘，以上数据以价格降序排列
      
"""		
def get_coin_depth( businessType = 'swap-btc-cny', size=10 ):		
	client = ApiClient( '',''  )
	result = client.get_depth(businessType,size)		
	df_asks = pd.DataFrame(result['asks'])
	df_bids = pd.DataFrame(result['bids'])
	df_merge = pd.merge(df_asks, df_bids,left_index=True, right_index=True, suffixes=('_asks','_bids'))	 
	
	return df_merge
	
"""
    最新成交记录
Parameters
------
  businessType:string  业务类型代码
              swap-btc-cny　 比特币对人民币现货合约
              swap-eth-cny　 以太坊对人民币现货合约
              swap-etc-cny　 以太经典对人民币现货合约
              swap-ltc-cny　 莱特币对人民币现货合约
			  

return
-------
  DataFrame
    
	
      
额外说明：
Direction: 1买 2卖 , time为long型
      
"""			
def get_coint_trades( businessType = 'swap-btc-cny'  ):		
	client = ApiClient('','' )
	result = client.get_trades(businessType )		
	list = result['list']
	df = pd.DataFrame(list)  
	return df		

"""
    K线信息
Parameters
------
  businessType:string  业务类型代码
              swap-btc-cny　 比特币对人民币现货合约
              swap-eth-cny　 以太坊对人民币现货合约
              swap-etc-cny　 以太经典对人民币现货合约
              swap-ltc-cny　 莱特币对人民币现货合约

	ktype 表示K线类型
	　　1min：一分钟K线 ，
	　　5min：五分钟K线 ，
	　　15min：十五分钟K线 ，
	　　30min：三十分钟K线 ，
	　　1hour：一小时K线 ，
	　　2hour：二小时K线 ，
	　　4hour：四小时K线 ，
	　　12hour：十二小时K线 ，
	　　1day：每日K线，
	　　1week：每周K线，
	　　1month：每月K线
	
	size：需要获取的深度数量，非必填，默认300.
			  
return
-------
  DataFrame
          
"""			
def get_coin_kline( businessType = 'swap-btc-cny' ,kype = '1min' , size=10  ):	
	client = ApiClient('','' )
	result = client.get_kline(businessType,kype , size )		
	list = result['list']
	df = pd.DataFrame(list) 	
	return df		


"""
    其他公共信息
Parameters
------
  businessType:string  业务类型代码
              swap-btc-cny　 比特币对人民币现货合约
              swap-eth-cny　 以太坊对人民币现货合约
              swap-etc-cny　 以太经典对人民币现货合约
              swap-ltc-cny　 莱特币对人民币现货合约
			  

return
-------
  DataFrame
    

      
"""		
def get_coin_publicinfo( businessType = 'swap-btc-cny'  ):	
	client = ApiClient('','' )
	ticker = client.get_publicinfo(businessType )		
	df = pd.DataFrame({
		'standardprice' :  [ ticker['standardprice'] ],
		'storeIntrest-buy' :   [ ticker['storeIntrest-buy'] ],
		'storeIntrest-sell' :  [ ticker['storeIntrest-sell'] ],
		'actualprice' :  [ ticker['actualprice'] ],
		'highprice' :   [ ticker['highprice'] ],
		'lowprice' :  [ ticker['lowprice'] ],
	})
	
	#print(df )
	return df	
	