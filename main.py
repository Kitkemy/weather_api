import requests
import sys
import pprint
from datetime import datetime
api_key = sys.argv[1]
if len(sys.argv) >= 3:
    date = sys.argv[2]
else:
    date = datetime.today().date()
      
r = requests.get(f'http://api.weatherapi.com/v1/history.json?key={api_key}&q=Cracow&dt={date}')

print(r.status_code)
pprint.pprint(r.json())