import requests
import json
from dotenv import load_dotenv
import os
import time

load_dotenv()

url = os.getenv('url')
API_KEY = os.getenv('API_KEY')

headers = {
    "Content-Type": "application/json-rpc",
    "Authorization": f"Bearer {API_KEY}"
}

check = requests.get(url, headers=headers)

SW_AC1_OPQ = { 
    "jsonrpc": "2.0",
    "method": "item.get",
    "params": {
        "output": ["name","lastvalue"],
        "filter": {
            "host": ["SW CORE - LJI"]
        }   
    },
    "id":1
}

def request():
    try:
        if check.status_code == 200:
            response = requests.get(url, headers=headers, data=json.dumps(SW_AC1_OPQ))
            dados_json = response.json()

        else:
            print(f'Não foi possivel estabelecer conexão, codigo {check.status_code}')
            

        arquivo_json = 'jsons/lji/core_lji.json'
        with open(arquivo_json, 'w') as arquivo_opq_ac1:
            json.dump(dados_json,arquivo_opq_ac1,indent=2)
    except:
        print("Não foi possivel realizar a requisição")
        

while True:
    request()
    time.sleep(60)