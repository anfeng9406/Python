"""Train tickets query from CLI.

Usage:
  test.py [-dgktz] <from> <to> <date>

Options:
  -h --help    Show this screen.
  -d            动车
  -g            高铁
  -k            快速
  -t            特快
  -z            直达

Example:
  test.py -gd 北京 上海 2017-11-01
"""

from docopt import docopt
import requests
import stations
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

canshu = docopt(__doc__)
start = stations.get_telecode(canshu['<from>'])
stop = stations.get_telecode(canshu['<to>'])

url = (
    'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.'
    'train_date={}&'
    'leftTicketDTO.from_station={}&'
    'leftTicketDTO.to_station={}&'
    'purpose_codes=ADULT'
).format(canshu['<date>'],start,stop)

s = requests.get(url,verify=False).json()
data = s['data']['result']
for i in data:
    print(i.split('|')[3],i.split('|')[8],i.split('|')[9],i.split('|')[13])




