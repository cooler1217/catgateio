#encoding=utf-8
'''
Created on 2018-8-10

@author: cooler
'''

import sys,os
import hashlib
import requests
import json
import time
import hmac
import urllib
		

class  GateIO(object):
    """docstring for  GateIO"""
    def __init__(self,apiKey,secretKey):
        super( GateIO, self).__init__()
        self.data_url = "data.gateio.io"
        self.api_url = "api.gateio.io"
        self.apiKey = apiKey
        self.secretKey = secretKey
        self.timeout = 30

    # python2.*版本
    def _getSign(self,params):
        bSecretKey = bytes(self.secretKey)
        sign = ''
        for key in params.keys():
            value = str(params[key])
            sign += key + '=' + value + '&'
        bSign = bytes(sign[:-1])
        mySign = hmac.new(bSecretKey, bSign, hashlib.sha512).hexdigest()
        return mySign

    #所有交易对
    def pairs(self):
        url = "https://{0}/api2/1/pairs".format(self.data_url)
        data = {}
        headers = {
            "Content-Type" : 'application/json;'
        }
        r = requests.get(url, data=data,params=data, headers=headers,timeout=self.timeout)
        results = r.json()
        return results

    #市场订单参数
    def marketinfo(self):
        url = "https://{0}/api2/1/marketinfo".format(self.data_url)
        data = {}
        headers = {
            "Content-Type" : 'application/json;'
        }
        r = requests.get(url, data=data,params=data, headers=headers,timeout=self.timeout)
        results = r.json()
        return results
    #交易市场详细行情
    def marketlist(self):
        url = "https://{0}/api2/1/marketlist".format(self.data_url)
        data = {}
        headers = {
            "Content-Type" : 'application/json;'
        }
        r = requests.get(url, data=data,params=data, headers=headers,timeout=self.timeout)
        results = r.json()
        return results

    #所有交易行情
    def tickers(self):
        url = "https://{0}/api2/1/tickers".format(self.data_url)
        data = {}
        headers = {
            "Content-Type" : 'application/json;'
        }
        r = requests.get(url, data=data,params=data, headers=headers,timeout=self.timeout)
        results = r.json()
        return results

    # 所有交易对市场深度
    def orderBooks(self):
        url = "https://{0}/api2/1/orderBooks".format(self.data_url)
        data = {}
        headers = {
            "Content-Type" : 'application/json;'
        }
        r = requests.get(url, data=data,params=data, headers=headers,timeout=self.timeout)
        results = r.json()
        return results

    #单项交易行情
    def ticker(self, param):
        url = "https://{0}/api2/1/ticker/{1}".format(self.data_url,param)
        data = {}
        headers = {
            "Content-Type" : 'application/json;'
        }
        r = requests.get(url, data=data,params=data, headers=headers,timeout=self.timeout)
        results = r.json()
        return results

    # 单项交易对市场深度
    def orderBook(self, param):
        url = "https://{0}/api2/1/orderBook/{1}".format(self.data_url,param)
        data = {}
        headers = {
            "Content-Type" : 'application/json;'
        }
        r = requests.get(url, data=data,params=data, headers=headers,timeout=self.timeout)
        results = r.json()
        return results

    # 历史成交记录
    def tradeHistory(self, param):
        url = "https://{0}/api2/1/tradeHistory/{1}".format(self.data_url,param)
        data = {}
        headers = {
            "Content-Type" : 'application/json;'
        }
        r = requests.get(url, data=data,params=data, headers=headers,timeout=self.timeout)
        results = r.json()
        return results
        # 

    #获取帐号资金余额
    def balances(self):
        url = "https://{0}/api2/1/private/balances".format(self.api_url)
        params = {}
        headers = {
            "Content-type" : "application/x-www-form-urlencoded",
            "KEY":self.apiKey,
            "SIGN":self._getSign(params)
        }
        r = requests.post(url, data=params, headers=headers,timeout=self.timeout)
        results = r.json()
        return results

    # 获取充值地址
    def depositAddres(self,param):
        url = "https://{0}/api2/1/private/depositAddress".format(self.api_url)
        params = {
        	"currency":param
        }
        headers = {
            "Content-type" : "application/x-www-form-urlencoded",
            "KEY":self.apiKey,
            "SIGN":self._getSign(params)
        }
        r = requests.post(url, data=params, headers=headers,timeout=self.timeout)
        results = r.json()
        return results

    # 获取充值提现历史
    def depositsWithdrawals(self, start,end):
        url = "https://{0}/api2/1/private/depositsWithdrawals".format(self.api_url)
        params = {'start': start,'end':end}
        headers = {
            "Content-type" : "application/x-www-form-urlencoded",
            "KEY":self.apiKey,
            "SIGN":self._getSign(params)
        }
        r = requests.post(url, data=params, headers=headers,timeout=self.timeout)
        results = r.json()
        return results

    # 买入
    def buy(self, currencyPair,rate, amount):
        url = "https://{0}/api2/1/private/buy".format(self.api_url)
        params = {
        	'currencyPair': currencyPair,
        	'rate':rate,
        	'amount':amount,
        }
        headers = {
            "Content-type" : "application/x-www-form-urlencoded",
            "KEY":self.apiKey,
            "SIGN":self._getSign(params)
        }
        r = requests.post(url, data=params, headers=headers,timeout=self.timeout)
        results = r.json()
        return results

    # 卖出
    def sell(self, currencyPair, rate, amount):
        url = "https://{0}/api2/1/private/sell".format(self.api_url)
        params = {
        	'currencyPair': currencyPair,
        	'rate':rate,
        	'amount':amount,
        }
        headers = {
            "Content-type" : "application/x-www-form-urlencoded",
            "KEY":self.apiKey,
            "SIGN":self._getSign(params)
        }
        r = requests.post(url, data=params, headers=headers,timeout=self.timeout)
        results = r.json()
        return results

    # 取消订单
    def cancelOrder(self, orderNumber, currencyPair):
        url = "https://{0}/api2/1/private/cancelOrder".format(self.api_url)
        params = {
        	'currencyPair': currencyPair,
        	'orderNumber':orderNumber,
        }
        headers = {
            "Content-type" : "application/x-www-form-urlencoded",
            "KEY":self.apiKey,
            "SIGN":self._getSign(params)
        }
        r = requests.post(url, data=params, headers=headers,timeout=self.timeout)
        results = r.json()
        return results

    # 取消所有订单
    def cancelAllOrders(self, ctype, currencyPair):
        url = "https://{0}/api2/1/private/cancelAllOrders".format(self.api_url)
        params = {
        	'currencyPair': currencyPair,
        	'type':ctype,
        }
        headers = {
            "Content-type" : "application/x-www-form-urlencoded",
            "KEY":self.apiKey,
            "SIGN":self._getSign(params)
        }
        r = requests.post(url, data=params, headers=headers,timeout=self.timeout)
        results = r.json()
        return results

    # 获取下单状态
    def getOrder(self, orderNumber, currencyPair):
        url = "https://{0}/api2/1/private/getOrder".format(self.api_url)
        params = {
        	'currencyPair': currencyPair,
        	'orderNumber':orderNumber,
        }
        headers = {
            "Content-type" : "application/x-www-form-urlencoded",
            "KEY":self.apiKey,
            "SIGN":self._getSign(params)
        }
        r = requests.post(url, data=params, headers=headers,timeout=self.timeout)
        results = r.json()
        return results

    # 获取我的当前挂单列表
    def openOrders(self):
        url = "https://{0}/api2/1/private/openOrders".format(self.api_url)
        params = {}
        headers = {
            "Content-type" : "application/x-www-form-urlencoded",
            "KEY":self.apiKey,
            "SIGN":self._getSign(params)
        }
        r = requests.post(url, data=params, headers=headers,timeout=self.timeout)
        results = r.json()
        return results

    # 获取我的24小时内成交记录
    def mytradeHistory(self, currencyPair, orderNumber):
        url = "https://{0}/api2/1/private/tradeHistory".format(self.api_url)
        params = {
        	'currencyPair': currencyPair,
        	'orderNumber':orderNumber,
        }
        headers = {
            "Content-type" : "application/x-www-form-urlencoded",
            "KEY":self.apiKey,
            "SIGN":self._getSign(params)
        }
        r = requests.post(url, data=params, headers=headers,timeout=self.timeout)
        results = r.json()
        return results


if __name__ == '__main__':
    apiKey = ""
    secretKey = ""
    gt = GateIO(apiKey,secretKey)
    # print gt.pairs()
    # print gt.marketinfo()
    # print gt.marketlist()
    # print gt.tickers()
    # print gt.orderBooks()
    # param = "eth_usdt"
    # print gt.ticker(param)
    # print gt.orderBook(param)
    # print gt.tradeHistory(param)
    # 交易相关操作 psot
    # 账户查询
    # print(gt.balances())
    # 获取账户充值地址
    # currency = "eth"
    # print(gt.depositAddres(currency))
    # 交易历史
    # start = int(time.mktime(time.strptime('2018-07-01 00:00:00',"%Y-%m-%d %H:%M:%S")))
    # end = int(time.mktime(time.strptime('2018-08-10 00:00:00',"%Y-%m-%d %H:%M:%S")))
    # print(gt.depositsWithdrawals(start,end))
    # 买入交易
    # buy_currencyPair = "eth_usdt"
    # buy_rate = '0.0000001'
    # buy_amount = '1'
    # print(gt.buy(buy_currencyPair,buy_rate, buy_amount))
    # 卖出交易
    # sell_currencyPair = "eth_usdt"
    # sell_rate = '100000'
    # sell_amount = '0.001'
    # print(gt.sell(sell_currencyPair,sell_rate, sell_amount))
    # print(gt.openOrders())
    # 取消挂单交易
    # orderNumber=1199379170
    # cancle_currencyPair = "eth_usdt"
    # print(gt.cancelOrder(orderNumber,cancle_currencyPair))
    # 取消所有挂单交易
    # ctype=0 #下单类型(0:卖出,1:买入,-1:不限制)
    # cancle_currencyPair = "eth_usdt"
    # print(gt.cancelAllOrders(ctype,cancle_currencyPair))
    # 查询交易状况
    # orderNumber=1199379170
    # cancle_currencyPair = "eth_usdt"
    # print(gt.getOrder(orderNumber,cancle_currencyPair))
    # 获取我的24小时内成交记录
    # orderNumber=1199379170
    # currencyPair = "eth_usdt"
    # print(gt.mytradeHistory(currencyPair,orderNumber))





    
