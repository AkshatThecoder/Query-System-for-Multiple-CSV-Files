import pandas as pd
import os

def load_csv(file_path):
    """Loads CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path)

# def list_available_csv(data_folder="data/"): 
#     """Lists all available CSV files in the data folder."""
#     return [f for f in os.listdir(data_folder) if f.endswith(".csv")]


## updated 
def list_available_csv(data_folder="data/"):
    """Lists all available CSV files in the data folder. Creates the folder if it does not exist."""
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)  # ✅ Automatically create the missing folder
    return [f for f in os.listdir(data_folder) if f.endswith(".csv")]

def get_csv_summary(df):
    """Generates a summary of the CSV file."""
    return {
        "columns": df.columns.tolist(),
        "num_rows": len(df),
        "num_columns": len(df.columns),
        "preview": df.head(5).to_dict()
    }
