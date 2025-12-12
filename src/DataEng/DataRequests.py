import requests
def DataRequest(code:int, start:str,limit:str):
    url =  f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados?formato=json&dataInicial={start}&dataFinal={limit}'
    response = requests.get(url=url)
    if response.status_code != 200:
        print(f'erro de requisiçao:{response.status_code} ')
        return None
    json = response.json()
    return json
test = DataRequest(code=433, start='01/01/2000',limit='01/01/2025')
print(test)