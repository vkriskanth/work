"""
This module contains all the big data related modules

"""
import pandas as pd

def convert_parquet_to_csv(input_file,output_file):
    df=pd.read_parquet(input_file)
    df.to_csv(output_file)
    return 0
