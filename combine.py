import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt
import average_salary
import sat

#get and print sat and salary dataframes from sat.py and average_salary.py respectively
sat_df = sat.get()
salary_df = average_salary.get()
print(sat_df)
print(salary_df)

#combine sat and salary dataframes into a combined dataframe
#take only the sat and average salary columns
combined_df = pd.concat([sat_df, salary_df], axis=1, sort=True)[['Total Score Mean', 'Average Salary']]
print(combined_df)
print("Combined dataframe has " + str(combined_df.shape[0]) + " data points")

#copy combined dataframe to Excel
#combined_df.to_excel("combined.xlsx")

#plot data
ax = combined_df.plot.scatter(x='Average Salary', y='Total Score Mean')
ax.set_xlim(xmin = 0)
ax.set_ylim(bottom = 0)
plt.show()