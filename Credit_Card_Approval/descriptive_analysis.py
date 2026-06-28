import pandas as pd

app = pd.read_csv("application_record.csv")
print(app.head())
print(app.info())
print(app.describe())
