from distutils.core import setup
import sys

if sys.version_info < (3,):
    print("coinshare requires Python version >= 3.0")
    sys.exit(1)
	
setup( 
	name='mineshare',
	version='0.0.5',
	url='http://www.cnblogs.com/wangshuo1/',
	license='',
	keywords='Virtual currency data',	
	author='xinping',
	author_email='xpws2006@163.com',
	description='A utility for crawling historical data of Virtual currency'	,
	packages=['mineshare' , 'mineshare.data' ,  'mineshare.public_markets' ,  'mineshare.util'  ]
) 