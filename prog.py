# #  import os
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import kagglehub

# # Download dataset
# DATASET_ID = "ds\Netflix_Title_Cleaned"
# FILE_NAME  = "Netflix_Title_Cleaned.csv"
# OUTPUT_DIR = os.path.join(os.getcwd(), "data", "netflix") 

# kagglehub.dataset_download(DATASET_ID, output_dir=OUTPUT_DIR)

# df = pd.read_csv(os.path.join(OUTPUT_DIR, FILE_NAME)) 

# print(f'Dataset caricato: {df.shape[0]:,} righe × {df.shape[1]} colonne') 

# import os
# import kagglehub
# import pandas as pd

# DATASET_ID = "ds/Netflix_Title_Cleaned" 
# FILE_NAME = "Netflix_Title_Cleaned.csv"
# OUTPUT_DIR = os.path.join(os.getcwd(), "data", "netflix")

# kagglehub.dataset_download(DATASET_ID, output_dir=OUTPUT_DIR)

# print("Cartella:", OUTPUT_DIR)
# print("File presenti:", os.listdir(OUTPUT_DIR))

# file_path = os.path.join(OUTPUT_DIR, FILE_NAME)

# if os.path.exists(file_path):
#     df = pd.read_csv(file_path)
#     print(df.head())
# else:
#     print("File NON trovato ❌")

import os
import pandas as pd

file_path = "/Users/annacavallari/progetto/netflix/ds/Netflix_Title_Cleaned.csv"

df = pd.read_csv(file_path)

print(f"Dataset caricato: {df.shape[0]:,} righe × {df.shape[1]} colonne")