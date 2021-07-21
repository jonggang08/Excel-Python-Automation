import pandas as pd
import numpy as np

excel_file = 'shift-data.xlsx'
df = pd.read_excel(excel_file)

split_values = df['Product'].unique()
#print(split_values)

for value in split_values:
    df1 = df[df['Product']== value]
    output_filename = "Product_" + str(value) + "_ProductList.xlsx"
    df1.to_excel(output_filename,index=False)