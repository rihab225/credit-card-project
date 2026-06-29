import pandas as pd
from sklearn.preprocessing import LabelEncoder
app = pd.read_csv("application_record.csv")
app.drop_duplicates(inplace=True)
print(app.isnull().sum())
print(app.isnull().mean())
app.drop(columns=['OCCUPATION_TYPE'], inplace=True)
app['DAYS_BIRTH'] = app['DAYS_BIRTH'].abs()
app['DAYS_EMPLOYED'] = app['DAYS_EMPLOYED'].abs()
app['FAMILY_DEPENDENCY'] = app['CNT_FAM_MEMBERS'] - app['CNT_CHILDREN']
le = LabelEncoder()

app['CODE_GENDER'] = le.fit_transform(app['CODE_GENDER'])
app['FLAG_OWN_CAR'] = le.fit_transform(app['FLAG_OWN_CAR'])
app['FLAG_OWN_REALTY'] = le.fit_transform(app['FLAG_OWN_REALTY'])
app['NAME_INCOME_TYPE'] = le.fit_transform(app['NAME_INCOME_TYPE'])
app['NAME_EDUCATION_TYPE'] = le.fit_transform(app['NAME_EDUCATION_TYPE'])
app['NAME_FAMILY_STATUS'] = le.fit_transform(app['NAME_FAMILY_STATUS'])
app['NAME_HOUSING_TYPE'] = le.fit_transform(app['NAME_HOUSING_TYPE'])
print(app.head())
app.to_csv("application_cleaned.csv", index=False)
