import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

#display 500 rows and 500 columns
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)





#SAT data

sat_df = pd.read_excel('WA _District_SAT_2019.xlsx', usecols= [0, 10])
print(sat_df)
#print(sat_df.shape[0])