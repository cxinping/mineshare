# -*- coding: utf-8 -*-

import decimal
import hashlib
import json
import requests

class ApiClient(object):
    # timeout in 5 seconds:
	timeout = 5
	api_url = 'http://www.okex.com'
	api_version = '/api/v1'

	def __init__(self ):
		pass

	# 获取OKEX合约行情数据 
	def get_future_ticker(self, symbol:str, contract_type:str):
		"""
		获取OKEX合约行情数据 
		https://www.okex.com/rest_api.html

		"""	
		uri = '/future_ticker.do?symbol=%s&contract_type=%s' % (symbol, contract_type )
		return self._doGet(uri)

	# 获取OKEX合约深度信息
	def get_future_depth(self, symbol:str, contract_type:str, size:int ):
		uri = '/future_depth.do?symbol=%s&contract_type=%s&size=%s&merge=0' % (symbol, contract_type, size )
		return self._doGet(uri)	
	
	#  获取OKEX合约指数信息
	def get_future_index(self, symbol:str  ):
		uri = '/future_index.do?symbol=%s' % (symbol  )
		return self._doGet(uri)		

	#   获取OKEX合约指数信息
	def get_future_estimated_price(self, symbol:str  ):
		uri = '/future_estimated_price.do?symbol=%s' % (symbol  )
		return self._doGet(uri)	

	#  获取当前可用合约总持仓量
	def get_future_hold_amount(self, symbol:str, contract_type:str  ):
		uri = '/future_hold_amount.do?symbol=%s&contract_type=%s' % (symbol, contract_type  )
		return self._doGet(uri)		
	
	
	
	def _call(self, uri):
		req_url = self.api_url + self.api_version + uri
		resp = requests.post(url=req_url, data=params, timeout=self.timeout)
		return self._parse(resp.text)

	def _parse(self, text):
		#result = json.loads(text, object_hook=_toDict)
		result = json.loads(text)
	
		if 'error' not in result:
			return result
		raise ApiError('%s' % (text))

	def _doGet(self, uri):
		req_url = self.api_url + self.api_version + uri
		print( req_url )
		response = requests.get(url=req_url  )	
		return self._parse(response.text)
		
class ApiError(BaseException):
    pass
