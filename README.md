
TWSE data collecting 台股每日券商買賣資料排名  
===============================

抓取每日個股券商買賣張數及價位，並按照買超數量排名
* 資料來源 證券櫃檯買賣中心 (http://www.gretai.org.tw/ch/)。
* 資料來源 台灣證券交易所 (http://www.twse.com.tw)。



Basics
-----------------------------

* Authors: Paul Lo
* Version: 1.0.0 of 2014/06/03
* Python Version: Python 2.7 
* Docs: TBA


Requires
-----------------------------

python 2.7


Report Issue or get involved
-----------------------------

- Github: https://github.com/paullo0106/stocktw/
- Issues: https://github.com/paullo0106/stocktw/issues/


Web Demo
-----------------------------

TBD


Quick Start
-----------------------------

* Specify stock id and date (R.O.C calendar in 7 numbers) as arguments:

example:
        ```python stock.py 3293 1030603```        

* Specify stock id and date (4 numbers for month and year) as arguments

example:
        ```python stock.py 3293 0603```


* specify stock id as the only one argument (the current date will be automatically applied)

example:
        ```python stock.py 3293```
    


# Output example

:: 以3293 0603為例  (後半段省略, 完整請見example_output.txt)

        Sum  |  Total Buy  |   Buy Cost  | Total Sell  |  Sell Cost  |   Avg Cost | Agent          
       96.0  |       96.0  |     135.84  |        0.0  |        0.0  |     135.84 | 5858  統一嘉義 
       95.0  |      331.0  |     135.99  |      236.0  |     133.02  |     134.76 | 9692  富邦嘉義 
      62.98  |       63.0  |     133.39  |       0.02  |      136.0  |     133.39 | 9659  富邦高雄 
       35.0  |       35.0  |      133.0  |        0.0  |        0.0  |      133.0 | 918W  群益金鼎忠孝 
       30.0  |       30.0  |      133.0  |        0.0  |        0.0  |      133.0 | 5690  豐興     
       23.0  |       30.0  |      133.0  |        7.0  |      133.0  |      133.0 | 9658  富邦建國 
       20.0  |       20.0  |      134.0  |        0.0  |        0.0  |      134.0 | 5600  永興   
       20.0  |       20.0  |      133.0  |        0.0  |        0.0  |      133.0 | 921S  凱基上新莊 
       19.0  |       19.0  |      133.0  |        0.0  |        0.0  |      133.0 | 8882  國泰台中 
       19.0  |       20.0  |      133.0  |        1.0  |      136.0  |     133.14 | 9852  元大大松山
       18.0  |       18.0  |      133.0  |        0.0  |        0.0  |      133.0 | 8880  國泰 
       16.0  |       16.0  |      133.0  |        0.0  |        0.0  |      133.0 | 9652  富邦世貿 
       16.0  |       16.0  |      133.5  |        0.0  |        0.0  |      133.5 | 1090  台灣工銀   
       15.0  |       15.0  |      133.0  |        0.0  |        0.0  |      133.0 | 6465  大昌桃園 
       14.0  |       14.0  |      133.0  |        0.0  |        0.0  |      133.0 | 585E  統一新營 
      (...omitted)



Change Logs
-----------------------------

### 1.0.0 2014/06/03

- Add python code with basic functions (only OTC stocks is available in this version)
