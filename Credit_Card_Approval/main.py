import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
app = pd.read_csv("application_record.csv")
corr = app.corr(numeric_only=True)
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(
    corr,
    annot=True
)
plt.title("Correlation Heatmap")
plt.show()
