import pandas as pd


def check_nan(df):
    """
    Check if there is any nan for each column in dataframe,
    and return a dataframe summarizing the results.
    """
    n_rows = len(df)

    check_df = {"col": [], "dtype": [], "nan_prc": []}

    for col in df.columns:
        check_df["col"].append(col)
        check_df["dtype"].append(df[col].dtype)
        check_df["nan_prc"].append(df[col].isna().sum() / n_rows)

    check_df = pd.DataFrame(check_df)
    print("\n")
    print(f"dataframe n_rows {n_rows}")
    print(check_df)
    print("\n")
