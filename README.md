# mineshare

提供查询虚拟币历史数据的网站： http://www.mineshare.cn , 即将上线。

安装mineshare
pip install mineshare


交易数据接口
============


Ticker信息
获得虚拟币的当前市场价格。
--------------------------

参数说明：
businessType：业务类型代码

参数	说明
swap-btc-cny	比特币对人民币现货合约
swap-eth-cny	以太坊对人民币现货合约
swap-etc-cny	以太经典对人民币现货合约
swap-ltc-cny	莱特币对人民币现货合约

调用方法：
import mineshare as ms
ms.get_coin_ticker('swap-btc-cny')

结果显示：

       buy           date     high     last      low     sell        vol
0  29000.1  1503986635719  29517.9  29052.8  28157.9  29099.9  1792.8017

其他：
ms.get_coin_ticker('swap-eth-cny')  获得以太坊对人民币现货合约的当前市场价格
ms.get_coin_ticker('swap-etc-cny')  获得以太经典对人民币现货合约的当前市场价格
ms.get_coin_ticker('swap-ltc-cny')  获得莱特币对人民币现货合约的当前市场价格

深度信息
--------------------------
获得虚拟币的市场深度信息

参数说明：
businessType：业务类型代码

swap-btc-cny	比特币对人民币现货合约
swap-eth-cny	以太坊对人民币现货合约
swap-etc-cny	以太经典对人民币现货合约
swap-ltc-cny	莱特币对人民币现货合约
size：需要获取的深度数量，非必填，默认买卖盘各50条。

返回值说明：
price：成交价格
amount：成交金额(元)

调用方法：
import mineshare as ms
ms.get_coin_depth('swap-btc-cny')

结果显示：
   amount_asks  price_asks  amount_bids  price_bids
0     0.023812     29396.5     0.068962     29001.3
1     0.010222     29348.4     0.451755     28998.0
2     0.010228     29330.4     0.220712     28997.0
3     0.283081     29320.2     0.010352     28978.7
4    17.508539     29305.7     0.010369     28932.0
5     0.095557     29301.9     0.640138     28900.0
6     0.010242     29290.5     0.377306     28889.0
7     4.997489     29274.7     5.955982     28761.0
8     0.041152     29160.2     1.439960     28750.8
9     0.068631     29141.4     4.121587     28726.8

返回值说明：
asks为卖盘，bids为买盘，以上数据以价格降序排列。
amount_asks：卖盘成交金额(元)
price_asks: 卖盘成交价格
amount_bids: 买盘成交金额(元)
price_bids: 买盘成交价格

其他：

import mineshare as ms
ms.get_coin_depth('swap-eth-cny')
ms.get_coin_depth('swap-etc-cny')
ms.get_coin_depth('swap-ltc-cny')