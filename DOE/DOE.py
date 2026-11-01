import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

#Insert data table from Excel file
dfRaw = pd.read_excel(r'C:\Users\nloyp\Documents\GitHub\Dissertation\DOE\Table\DOE_Cell area_Dissertation.xlsx', sheet_name=0) #Raw dataframe

#Extract and structure First and Second replicate runs
df1 = dfRaw.iloc[1:9, 0:5].copy() #rep 1
df1.columns = ['Test', 'MouldTemp', 'GasContent', 'InjSpeed', 'CellArea']

df2 = dfRaw.iloc[12:20, 0:5].copy() #rep 2
df2.columns = ['Test', 'MouldTemp', 'GasContent', 'InjSpeed', 'CellArea']

#Combile replicate
df = pd.concat([df1, df2], ignore_index=True)
df['MouldTemp'] = df['MouldTemp'].astype(str) #independent variable
df['GasContent'] = df['GasContent'].astype(str) #independent variable
df['InjSpeed'] = df['InjSpeed'].astype(str) #independent variable
df['CellArea'] = df['CellArea'].astype(float) #Dependent variable

#3-Way ANOVA model
model = ols('CellArea ~ MouldTemp * GasContent * InjSpeed', data=df).fit() #ols = Ordinary Least Squares

#Create ANOVA table
anovaTable = sm.stats.anova_lm(model,typ=2) #Type II Sum of Squares
anovaTable['eta_sq'] = anovaTable['sum_sq'] / anovaTable['sum_sq'].sum()

print(anovaTable)