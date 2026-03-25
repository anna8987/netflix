
import os
import pandas as pd

file_path = "ds/Netflix_Title_Cleaned.csv"

df = pd.read_csv(file_path)

print(f"Dataset caricato: {df.shape[0]:,} righe × {df.shape[1]} colonne")
