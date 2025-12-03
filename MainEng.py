from src.DataEng.DataEng import DataEng

obj = DataEng()
data_inicio = '01/01/2000'#a data que eu quero para o inicio do estudo 
data_final = '01/10/2025' #a data que eu quero para o final do estudo 
obj.load(code=433, start_date=data_inicio, end_date=data_final)
obj.feature_eng() # faz a transformaçao de colunas 
obj.to_parquet(name='IPCA_Janeiro_2000_a_outubro_2025') # exporta para parquet 