import pandas as pd
import numpy as np
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
pd.read_excel("E:\\PTDL\\pandas\\sv_HUET.xlsx",skiprows=3,nrows=7)
# lấy phân vị 50%
df.describe(include=np.number).T[['50%']]
# giá trị xuất hiện nhiều nhất trong cột
df.describe(include=[object]).T['top']
# số lần xuất hiện của giá trị top
df.describe(include=[object]).T['freq']
# tính phân vị 25 >> sắp xếp tăng dần>> vị trí ceil(0.25*n)= vị trí nguyên nhỏ nhất lớn hơn 0.25*n
# tính phân vị của cột thu nhập với phân vị 25%
df['Thu nhập'].quantile(0.25)
# phân tổ
df['DTB C3']=pd.qcut(df['Điểm TB lớp 12'],q=3,labels=['<6.5','6.5-7.9','>=8.0'])
df['Loại']=pd.qcut(df['Điểm TB lớp 12'],q=3,labels=['TB','Khá','GIỎI'])
a=df.groupby(['DTB C3','Loại']).size().unstack(fill_value=0)

import matplotlib.pyplot as plt

def do_thi():
    df['Lớp'].value_counts().sort_index().plot(kind='bar')
    plt.title('Biểu đồ tổng thu nhập từng lớp')
    plt.xlabel('Thu nhập')
    plt.ylabel('Số lượng')
    plt.show()

    df['Thu nhập'].value_counts().sort_index().plot(kind='bar').pcolor 
    plt.title('Biểu đồ thu nhập')
    plt.xlabel('Thu nhập')
    plt.ylabel('Số lượng')
    plt.show()

