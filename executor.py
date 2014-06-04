#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import csv
import urllib2
import time
from functools import wraps

summaryData = {} # Keep a list of necessary data for each agent/branch, the value is a list which contains [<agent name>,<buy num>,<sell number>,<buy cost>,<sell cost>]

# alignment: http://docs.python.org/2/library/string.html#formatspec
# http://stackoverflow.com/questions/10623727/python-spacing-and-aligning-strings
printDataFormat = " {0:>10}  | {1:>10}  | {2:>10}  | {3:>10}  | {4:>10}  | {5:>10} | {6:<15}"
# print out columns: 'Sum','Total Buy','Buy Cost','Total Sell','Sell Cost','Avg Cost','Agent'


def registerNum(agent_name,buy_num,sell_num,cost):
    name = agent_name.split()  # format: '<number> <name>'
    name = name[0] # Use number as identifier is good enough
    
    global summaryData

    buy_num = float(buy_num)
    sell_num = float(sell_num)
    cost = float(cost)
    if summaryData.get(name,None)==None: # this agent name appears for the first time
       if buy_num>0 and sell_num>0: # then the cost listed on excel is both sell cost and buy cost
          summaryData[name] = (agent_name, buy_num, sell_num, cost, cost)
       elif buy_num>0:  # the cost is for buy cost
          summaryData[name] = (agent_name, buy_num, sell_num, cost, 0)
       else: # the cost is for sell cost
          summaryData[name] = (agent_name, buy_num, sell_num, 0, cost)   
    else: # do calculation to combine with previous data of this agent_name

       tmpData = summaryData[name] 

       buyNum = tmpData[1]
       buyCost = tmpData[3]
       sellNum = tmpData[2]
       sellCost = tmpData[4]
       
       if buy_num>0:
          newBuyTotal = buy_num*cost
          buyTotal = buyNum*buyCost + newBuyTotal
          buyNum+=buy_num
          buyCost = buyTotal/buyNum
       
       if sell_num>0:
          newSellTotal = sell_num*cost
          sellTotal = sellNum*sellCost + newSellTotal
          sellNum+=sell_num
          sellCost = sellTotal/sellNum
       
       summaryData[name] = (agent_name, buyNum, sellNum, buyCost, sellCost )


def printHeader():
     print printDataFormat.format('Sum','Total Buy','Buy Cost','Total Sell','Sell Cost','Avg Cost','Agent')


def printResult(agentName):
     list = summaryData[agentName] 

     # ('116f  \xa4\xe9\xb2\xb1\xb4_\xbf\xb3', 130000.0, 0.0, 0, 40.88346153846154, 0)
     agentName = list[0]
     buy = list[1]
     sell = list[2]
     buy = buy/1000
     sell = sell/1000
     sum = buy-sell

     buyCost = list[3]
     sellCost = list[4]
     avgCost = (buyCost*buy + sellCost*sell) / (buy+sell) # calculate the average cost
     
     
     sum = round(sum,2)
     buy = round(buy,2)
     sell = round(sell,2)
     buyCost = round(buyCost,2)
     sellCost = round(sellCost,2)
     avgCost = round(avgCost,2)
    
     # alignment: http://docs.python.org/2/library/string.html#formatspec
     # http://stackoverflow.com/questions/10623727/python-spacing-and-aligning-strings
     #print list
     #print 'sum:'+ str(sum) 
     #print 'agent:' + agentName
     #print str(sum) + ' ' + str(buy) + ' ' + str(buyCost) + ' ' + str(sell) + ' ' + str(sellCost) + ' ' + str(avgCost) + ' ' + str(agentName)
     print printDataFormat.format(sum, buy, buyCost, sell, sellCost, avgCost, agentName)
     

def retry(ExceptionToCheck, tries=4, delay=3, backoff=2, logger=None):
    """Retry calling the decorated function using an exponential backoff.

    http://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
    original from: http://wiki.python.org/moin/PythonDecoratorLibrary#Retry

    :param ExceptionToCheck: the exception to check. may be a tuple of
        exceptions to check
    :type ExceptionToCheck: Exception or tuple
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param backoff: backoff multiplier e.g. value of 2 will double the delay
        each retry
    :type backoff: int
    :param logger: logger to use. If None, print
    :type logger: logging.Logger instance
    """
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck, e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print msg
			print args
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry
    

@retry(Exception,tries=3)
def collectOTCData(stockId,date):
	top_n = "100000" # default as a big number to get all the rows
	url = 'http://www.gretai.org.tw/ch/stock/aftertrading/broker_trading/download_BRKRBSCSV.php?curstk='+stockId+'&fromw=0&numbern=10000&stk_date='+date
	response = urllib2.urlopen(url)
	return response


#main function here
def execute(stockId, date):

		if stockId is None: # or date==None:
   			#print 'some error message' 
   			return

                global summaryData
	        summaryData = {}

		try:
			response = collectOTCData(stockId,date) 
		except Exception, e:
			print e
			print 'Cannot get data for ' + str(stockId)
			return

		cr = csv.reader(response)
		    
		''' Expected format example in each row:
		['1823', '1020  合庫', '124.50', '0', '2,000', '', '1824', '1020  合庫', '127.50', '0', '110']
		'''    
		for row in cr:
  		        x=0

  		        if len(row)>10: # 11 columns in total
    		            name1 = row[1]
    		            buy1 = row[3]
    		            buy1 = buy1.replace(",","")
    		            name2 = row[7]
    		            buy2 = row[9]
    		            buy2 = buy2.replace(",","")
    
    		            sell1 = row[4]
    	 	            sell1 = sell1.replace(",","")
    		            sell2 = row[10]
    		            sell2 = sell2.replace(",","")
    
    		            cost1 = row[2]
    		            cost2 = row[8]

    		            try: # in order to skip the beginning few lines of header
				''' header format example:
				['券商買賣證券成交價量資訊']
				['證券代碼', '3293']
				['序號','券商','價格','買進股數','賣出股數','','序號','券商','價格','買進股數','賣出股數']
				'''
       			        str(int(buy1))
       			        str(int(buy2))
       		    	        str(int(sell1))
       			        str(int(sell2))
    		            except ValueError:
       			        continue
    
    		            registerNum(name1,buy1,sell1,cost1)
    		            registerNum(name2,buy2,sell2,cost2)

		if len(summaryData)<1:
    			print 'Found no result for ' + str(stockId) + ' on ' + str(date) 
                	return
                
		rankAll = {}

		# Calculate and sort according to buy/sell number  
		for key,value in summaryData.iteritems():
    		    diff = float(value[1])-float(value[2]) # buy number - sell number
    		    rankAll[key] = diff

		rankAll = sorted(rankAll.items(), key=lambda x:x[1], reverse=True)
                
		printHeader()
		for item in rankAll:
     				printResult(item[0])




