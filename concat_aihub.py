import pandas as pd
import glob

data_paths = glob.glob('./crawling_data/*')
df = pd.DataFrame()
for path in data_paths:
    df_temp = pd.read_csv(path, index_col=0, encoding='cp949')
    df = pd.concat([df, df_temp], ignore_index=True)
df.drop_duplicates(inplace=True)
# df.dropna(inplace=True)

print(df.head(30))
df.info()
# print(len(df.titles.value_counts()))
df.to_csv('./crawling_data/감정분류데이터셋.csv', index=False)