# %% 
import pandas as pd 
import os
import matplotlib.pyplot as plt 
import seaborn as sns
# %% 
data_path = os.path.join('..', 'data', 'serie_IPCA_Janeiro_2000_a_outubro_2025.parquet')
df = pd.read_parquet(data_path)
display(df)
# %%
plt.figure(figsize=(10,5))
plt.title('indice nacional de preços ao consumidor amplo (IPCA)')
plt.plot(df['valor'], label='IPCA', color='red')
plt.legend()
# %%
