import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = "Financial Sample.xlsx"
df = pd.read_excel(excel_file_path)
#print(df.head())

# Time Series
canada = df.loc[(df['Country']=="Canada") & (df['Segment']=="Government")]
canada = canada.sort_values(by=['Date'])
#canada.plot(x='Date', y = 'Profit')
#plt.show()

#Bar
df_products = df.groupby(['Product']).sum()
df_products['Units Sold'].plot.bar()
plt.show()

#Pie
df_products = df.groupby(['Product']).sum()
df_products['Units Sold'].plot.pie()
plt.show()