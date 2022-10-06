
import pandas as pd
#import csv

# file = open('C365_AF.csv')
# type(file)
df = pd.read_csv(r'C:\Users\Gayathri.Sujatha\Downloads\C365_AF.csv')

# new_df = C365_AF.shape
# C365_AF.isnull()
# C365_AF.isnull().sum()
# cVar = C365_AF[ThreadId].isnull().sum()
# print (cVar)
df.info()
ct = df.ThreadId.isna().sum()
print(ct)
countRows = df.head()
print(countRows)

# cVar = df["ThreadId"].std.count("")