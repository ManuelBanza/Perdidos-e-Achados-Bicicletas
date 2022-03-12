import requests
import time
import pandas as pd
from requests.exceptions import ConnectionError
from datetime import datetime
from datetime import date
import itertools

# Criar lista com os dias
days = pd.date_range(end = pd.datetime.today(), periods=5, freq='D').strftime('%d-%m-%Y').tolist()


### Página 0

# Criar loop que pesquise cada dia

df = pd.DataFrame()

try:
    for day in days:
        headers = {
            'Host': 'perdidoseachados.mai.gov.pt',
            'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0',
            'Accept': 'application/xml, text/xml, */*; q=0.01',
            'Accept-Language': 'en-GB,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Length': '114',
            'Origin': 'https://perdidoseachados.mai.gov.pt',
            'Connection': 'keep-alive',
            'Referer': 'https://perdidoseachados.mai.gov.pt/SIISPA2013/default.aspx',
            #'Cookie': 'ASP.NET_SessionId=y0ckpfnetdfng3upp4brvgyf; InfoSG=!vyDw9VeOX/lxLBoCoPu/tYv6QITGdZXrKcGSt6QMhdwBScK5ny/LGmetQNVC8qD5e/moZPlYkudkrg==; TS014826ac=01a7b7ad1014347acf0fe02101804320a7976283532448013620fb046fc184b069b325ea2312b33257a185232689ea0fc730b09b87875e60f93d82d7175e78788f36369a74f09639291ca84166ddd4c3651ee24951; TS8ac0f2f4027=0884e346f6ab2000a920071de937e72c9a99a36f3437a7f3ac15d15df1c51ba2ad0827a8feb80dc10830b12beb113000f499d8d8b927e5f6bc3127fe1f931aa32ca4e88563d5d2e849fc611102c9f093fc768cdca01f7a7ec0a07f2512a64a51; TS01fb1014=01a86827a79ad70709ac28e968d8ae2b3094628295751d2fad587da8a8117e728680a7dcf0bf09e00cfa2d11f95433ffbafcdd8ac4; TS1efd216b027=083771d179ab2000b21e0bdfdd56aef0630f3dd0eb6d3cf1618a30cf62c0365b5639dc2c6840eef608301740fa11300060dac51116233b7924aefe83eb9069f84513fb40f623f91505dab0ebe24978f6ff65340a117f1e06c9a510960d9bff8b',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'}

        url = 'https://perdidoseachados.mai.gov.pt/SIISPA2013/search.aspx'
        payload = {
            "txtSearch": "a",
            "date": "{}".format(day),
            "groupId": "1",
            "typeDesc": "OBJECTOS PESSOAIS",
            "subTypeDesc": "BICICLETA",
            "pi": "0",
            "localDesc": "",
            "searchMode": ""
        }

        time.sleep(0.1)
        r = requests.post(url, data=payload, headers=headers)
        result = pd.read_xml(r.content, xpath=".//ROW")
        df = df.append(result)
except:
    pass


df.drop_duplicates(subset='NR_REGISTO', keep="first", inplace=True)


# Get today date now to file name when export to csv or excel with encoding utf8
from datetime import datetime
df.to_csv(datetime.now().strftime('data_sources/data_transformed/perdidoseachados_bicicletas-%Y-%m-%d-%H-%M-%S.csv'), encoding='utf8')
