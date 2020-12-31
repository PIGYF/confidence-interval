import pandas as pd


df = pd.read_excel(r'C:\Users\sinotrans\Desktop\test.xlsx', engine='openpyxl')
df_group = df.groupby(["经营单位", "品名"]).count()
#print(df_group)

df_mean = df.groupby(["经营单位", "品名"]).mean()
df_std = df.groupby(["经营单位", "品名"]).std()
#df_group = df_group.size()
a = df_mean - 1.96*df_std/((df_group)**0.5)
b = df_mean + 1.96*df_std/((df_group)**0.5)
a.to_excel('下限.xlsx')
b.to_excel('上限.xlsx')
#print(a)
