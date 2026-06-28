import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset
app = pd.read_csv("application_record.csv")
print("Number of people working status:")

print(app["OCCUPATION_TYPE"].value_counts())
plt.figure(figsize=(18,6))

sns.countplot(
    x="OCCUPATION_TYPE",
    data=app,
    palette="Set2"
)
plt.xticks(rotation=90)
plt.title("Occupation Type Distribution")
plt.show()
