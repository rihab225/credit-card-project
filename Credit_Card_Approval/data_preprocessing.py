import pandas as pd

application_df = pd.read_csv("application_record.csv")
credit_df = pd.read_csv("credit_record.csv")
print(credit_df.head())
print(credit_df["STATUS"].unique())
def to_binary(status):
    if status in ['0', 'X', 'C']:
        return 1      # Approved (good payment/no loan)
    else:
        return 0      # Not Approved
    credit_df["STATUS_BIN"] = credit_df["STATUS"].apply(to_binary)
    print(credit_df["STATUS_BIN"].value_counts())
    final_df = application_df.merge(
    credit_df,
    how="left",
    on="ID"
)
    print(final_df.shape)
    print(final_df.head())
    print(final_df.isnull().sum())
