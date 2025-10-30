#!/usr/bin/env python3

from os import sep
import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep='\t')

    df.replace("New", np.nan, inplace=True)
    df.replace("Re", np.nan, inplace=True)
    df.any()

    df["LW"] = df["LW"].astype(float)
    df["Pos"] = df["Pos"].astype(float)

    print(df.dtypes)
    mask = df["LW"] < df["Pos"]
    #print(df.columns)
    return df[mask]

    pass

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
