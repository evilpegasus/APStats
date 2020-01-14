import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile



df = pd.read_excel('WA _District_SAT_2019.xlsx')

#display 500 rows and 500 columns
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#print
#print("Column headings:")
#print(df.columns)
print(df)