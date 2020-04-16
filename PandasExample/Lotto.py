import pandas as pd
df = pd.read_csv('.\\CSV\\Lotto.csv')
# print(df.head(3))
print(df)
print(df.columns)
# print(df['bonus'][0:5])
# print(df.describe())

# num = df.apply(pd.value_counts).fillna(0).astype(int)
# print(num)
# print(df.duplicated())
# print(df[df.duplicated()])
# print(df.info())
# bo = df['bonus'].value_counts(dropna = False)
# print(bo.sort_index()) #정렬
# print(bo) #정렬