import pandas as pd
df = pd.read_csv (r'C:\UVA\Techbootcamp\download.csv') 

groupby_sum1 = df.groupby(['Country']).sum() 
print(groupby_sum1)