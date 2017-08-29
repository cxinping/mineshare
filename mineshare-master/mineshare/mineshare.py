# -*- coding: utf-8 -*-


import util.TimeUtil as time
from public_markets.market import ( get_coin_ticker, get_coin_depth, get_coint_trades,get_coin_kline, get_coin_publicinfo )

def mul(a, b):
	return a * b

if __name__ == '__main__':
	#print( get_coin_ticker()  )
	#print( get_coin_ticker())
	#print( type( get_coin_ticker() )  )  
	#print( get_coin_depth() )
	data = get_coint_trades()
	#data = get_coin_kline('swap-btc-cny' ,  '1min' , 20)
	#data = get_coin_publicinfo('swap-btc-cny'  )
    
	#data = get_coin_ticker('swap-eth-cny')
	#data = get_coin_depth( )	
	print( data )
	
	
	
	
	
	
	
	