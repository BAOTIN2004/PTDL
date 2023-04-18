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
df.groupby(['Lớp'])['Thu nhập'].min()
g=df.groupby(['Lớp'])

def hien_theo_lop(g):
    for grade, item in g:
        print('Lớp:'+str(grade))
        print( str(item),'\n\n')

# tùy chọn đọc từ hàng thứ đầu tiền đến hàng n
df.head(10)
# đọc từ hàng 2 đến hàng 9
df.loc[2:9]
# ngoài ra có thể đọc số hàng tùy chọn mà ko cần phải đọc toàn bộ file, skiprows : bo qua 2 dong dau bat dau doc tu dong 3 voi so luong 7 dong
df1=pd.read_excel("E:\\PTDL\\pandas\\sv_HUET.xlsx",skiprows=3,nrows=7)