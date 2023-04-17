import pandas as pd, numpy as np,openpyxl
df = pd.read_excel("E:\\PTDL\\pandas\\sv_HUET.xlsx")

# đếm số lần xuất hiện của các giá trị trong cột thứ 6
df.iloc[0:,5].value_counts()
# tương tự ý trên
df["Giới tính"].value_counts()
# để tránh dữ liệu bị nhầm một số chổ có kiểu khác số thực ,kh thể thực hiện phép tính nên có thể ép kiểu như dưới đây
df['Thu nhập']=df["Thu nhập"].astype(float)
# tính tổng thu nhập toàn bộ 
df["Thu nhập"].sum()
# gom nhóm theo lớp, tính về thu nhập: tổng, trung bình,..
df.groupby(by='Lớp').agg({'Thu nhập': 'mean'})
# có thể sử dụng đơn giản như dưới đây
df.groupby(['Lớp'])['Thu nhập'].mean() # trung bình thu nhập theo lớp
# thông tin thu nhập max, min từng lớp
df.groupby(['Lớp'])['Thu nhập'].max()
g=df.groupby(['Lớp'])
def hien_theo_lop(g):
    for grade, item in g:
        print('Lớp:'+str(grade))
        print( str(item),'\n\n')
a=df.groupby(['Lớp'])['Thu nhập'].min()
print(a)