# -*- coding: utf-8 -*-



import time

def get_now():
	return time.strftime('%Y-%m-%d %H:%M:%S')

def int2time(timestamp):
	datearr = datetime.datetime.utcfromtimestamp(timestamp)
	timestr = datearr.strftime("%Y-%m-%d %H:%M:%S")
	return timestr
	
def getTimeStamp():
	return int(time.time() )
		
def getCurrentTime():
	return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	
def converTimeStamp( timestamp):
	x = time.localtime( timestamp )
	return time.strftime('%Y-%m-%d %H:%M:%S',x)    

if __name__ == '__main__':
	date = converTimeStamp( 1502173450.9882445 )
	print( date )
    
	#timestamp = getTimeStamp()
	#print( (timestamp) )
	#curTime = getCurrentTime()
	#print( curTime )    
    
    
    