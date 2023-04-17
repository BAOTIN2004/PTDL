import pandas as pd
df = pd.read_excel('E:\\PTDL\\pandas\\Temperature.xlsx',sheet_name='Sheet1')
df.head(100)
#df1=pd.read_excel('E:\\PTDL\\pandas\\tuoi.xlsx',sheet_name='Sheet1')
df.iloc[0,0] # truy xuat vi tri cu the
df.loc[0:2] # truy xuat tu hang 0 den hang 

sort_point=df.sort_values(by='Nhiệt độ',ascending=True)
print(sort_point)
# cách này sẽ ghi đè nội dung trước : 
#data_add.to_excel('E:\\PTDL\\pandas\\tuoi.xlsx',sheet_name='Sheet1',index=False)
# import openpyxl 



