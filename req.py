import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-18&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=QDK&purpose_codes=ADULT'

s = requests.get(url,verify=False).json()

data = s['data']['result']

for i in data:
    print(i.split('|'))

