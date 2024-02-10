import requests
from datetime import datetime
import time
import logging
import os.path
from colorama import Fore

# print (os.path.abspath(logging.__file__))
from_date=input('Enter Start Date in yyyy/mm/dd format')
end_date=input('Enter End Date in yyyy/mm/dd format')
symbol=input("Write Your Stock Symbol")
d= datetime.strptime(from_date, '%Y/%m/%d')
de=datetime.strptime(end_date,'%Y/%m/%d')
epoch=int(time.mktime(d.timetuple()))
epoche=int(time.mktime(de.timetuple()))
# str(epoch).split('.')
print(epoch)
print(epoche)

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 
url=f"https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={epoch}&period2={epoche}&interval=1d&events=history&includeAdjustedClose=true"
request= requests.get(url=url,headers=headers).content
print(request)
with open(f'{symbol}from{from_date}to{end_date}','wb')as file:
    file.write(request)

