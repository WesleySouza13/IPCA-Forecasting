# %%
import pandas as pd 
import os 
from sklearn.linear_model import LinearRegression
import numpy as np
data_path = os.path.join('data', 'serie_IPCA_Janeiro_2000_a_outubro_2025.parquet')
df = pd.read_parquet(data_path)
print(df)
# %% 
df['dias'] = (df['data'] - df['data'].min()).dt.days

X = df[['dias']]
y = df['valor']
model = LinearRegression().fit(X, y)
dias_futuros = np.array([9142, 9143, 9144]).reshape(-1,1)
pred = model.predict(dias_futuros)
# %%
data_futura = [df['data'].min() + pd.Timedelta(days=int(d)) for d in dias_futuros.flatten()]

for data, valor in zip(data_futura, pred):
    print(data, '->', valor)
# %%

# %%
display(df)
#
# %%
