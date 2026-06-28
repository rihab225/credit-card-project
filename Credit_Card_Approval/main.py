import pandas as pd

app = pd.read_csv('application_record.csv')
credit = pd.read_csv('credit_record.csv')
print(app.head())

print(credit.head())
print(app.shape)
print(credit.shape)
print(app.info())
print(credit.info())
print(app.isnull().sum())
print(credit.isnull().sum())
