import pandas as pd 
from pathlib import Path 

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def oky_csv(filename:str)->str:
    """
    just read the csv file  and return simple summary.
    """
    file_path =DATA_DIR / filename

    df = pd.read_csv(file_path)
    return f"CSV file '{filename}' has {len(df)} rows and {len(df.columns)} columns."


def oky_parqet(filename: str)->str:
    """
    tozhe samoe kak s csv file
    """
    file_path = DATA_DIR/filename

    df = pd.read_parquet(file_path)
    return f"parquet file '{filename}' has {len(df)} rows and {len(df.columns)} columns."




