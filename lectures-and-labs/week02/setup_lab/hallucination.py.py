import pandas as pd


def load_spreadsheet(path: str) -> pd.DataFrame:
    """Load an Excel spreadsheet with pandas."""
    return pd.read_excel(path)


spreadsheet = load_spreadsheet("data.xlsx")
print(spreadsheet.head())