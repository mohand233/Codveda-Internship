from google.colab import files
import pandas as pd

uploaded = files.upload()
file_name = list(uploaded.keys())[0]  
df=pd.read_csv(file_name)
df=df.dropna()
df=df.drop_duplicates()
df["species"]=df["species"].astype(str).str.lower().str.strip()
print("duplicated_rows_is ",df.duplicated().sum())
print("Missing values:",df.isnull().sum())
df.to_csv("final_iris.csv", index=False)
files.download("final_iris.csv")
