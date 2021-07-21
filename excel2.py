import numpy as np
import pandas as pd

excel_file = 'shift-data.xlsx'
df = pd.read_excel(excel_file)

# conditional
cheese = df['Name'].where(df['Product']=='Cheese')
#print(cheese.dropna())

data = df.loc[df['Product']=="Sausage"]


# mulitple excel files
excel_files= ['shift-data.xlsx','third-shift-data.xlsx']

for ind in excel_files:
    df = pd.read_excel(ind)
    cheese = df['Name'].where(df['Product']=='Cheese').dropna()
    print("File Name"+ ind)
    print(cheese)