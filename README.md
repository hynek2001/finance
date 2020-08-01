#### install
```cmd
 pip install git+git://github.com/hynek2001/finance.git
```
#### Finance library
* mfin.yahoo  
  * getNasdaqStock
  ```python
  from mfin.yahoo import getNasdaqStock
  getNasdaqStock("AMZN")
  ```        
  * getNasdaqStocks  
  ```python
  from mfin.yahoo import getNasdaqStocks
  getNasdaqStocks(["AMZN","BA"])
  ```