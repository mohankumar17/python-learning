import pandas as pd

df = pd.DataFrame([(1, "Paul", 32), (2, "Tina", 36), (3, "John", 26)], columns=["ID", "NAME", "AGE"])
#print(df)

print(df["NAME"][2])
