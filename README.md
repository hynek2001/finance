#### install
```
pip install git+git://github.com/hynek2001/finance.git
```
#### Finance library
* mfin.yahoo  
  * getStock
  ```python
  from mfin.yahoo import getStock
  getStock("AMZN")
  ```        
  * getNasdaqStocks  
  ```python
  from mfin.yahoo import getStocks
  getStocks(["AMZN","BA"])
  ```