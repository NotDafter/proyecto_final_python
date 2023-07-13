#%%
import pandas as pd
import matplotlib.pyplot as plt
#import plotly.graph_objects as go

path="historico_temperaturas.xlsx"
ventas=pd.read_excel(path, nrows=100)

ventas= pd.read_excel(path, usecols=["año", "mes", "máxima", "mínima", "media"], nrows=1000000)
esto = ventas[ventas["año"]>= 2010]

plt.bar(esto["año"], esto["máxima"])
plt.xlabel("AÑOS")
plt.ylabel("TEMPERATURAS")
plt.title("TEMPERATUAS MÁXIMAS")
plt.xticks(rotation=50, ha="right")
plt.show()


# %%
esto = ventas[ventas["año"]>= 2010]


plt.bar(esto["año"], esto["mínima"])
plt.xlabel("AÑOS")
plt.ylabel("TEMPERATURAS")
plt.title("TEMPERATUAS MÍNIMAS")
plt.xticks(rotation=50, ha="right") 
plt.show()
# %%