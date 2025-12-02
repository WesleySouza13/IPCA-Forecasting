from src.DataEng.DataEng import DataEng

obj = DataEng()
data_inicio = '01/01/2000' #a data que eu quero para o inicio do estudo 
obj.load(code=433, start_date=data_inicio)
obj.feature_eng() # faz a transformaçao de colunas 
obj.to_parquet(name='IPCA') # exporta para parquet 