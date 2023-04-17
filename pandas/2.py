import numpy as np, pandas as pd 
#DataFrame là một cấu trúc dữ liệu có nhãn 2 chiều với các cột có nhiều kiểu 
# khác nhau. Dataframe giống như một bảng tính hoặc bảng trong SQL.
#Tạo DataFrame
columns1 = ['name', 'age', 'gender', 'job']
dt1 = pd.DataFrame([['Bao Tin',19,'M','engineer'],['alice', 19, "F", "student"],['john', 26, "M", "student"]],columns=columns1)
dt2 = pd.DataFrame(dict(name=['Bao TIn', 'julie',"peter"],age=[33, 44,19], gender=['M', 'F',"M"],job=[ 'scientist','student','engineer']))
height = pd.DataFrame(dict(height=[1.65, 1.8]))
# pd.concat la ham dung de noi cac doi tuong du lieu theo truc nhat dinh , axis =0 nối theo chiều  dọc, axis=1 nối theo chiều ngang  
# ket hợp cột
dt3= pd.concat([dt2 ,height], axis=1)
# kết hợp hàng 
dt4=pd.concat([dt1,dt2],axis=0)
# cung co the dung append de ket hop cac df theo hang
#(dt1.append(dt2))
#Sử dụng phép giao các khoá của 2 frame (kết nối trong 2 bảng - innner joint)
dt5 = pd.DataFrame(dict(name=['Bao Tin', 'john', 'eric', 'julie',"alice"], height=[165, 180, 175, 171,162]))
# chỉ các hàng có giá trị khớp trong 2 data frame mới có thêm 
dt6 = pd.merge(dt2, dt5)
# thêm cột height cho tat ca doi tuong trong dt2, chỉ định cot name làm cột chung , how= outer de cac hang kh khop trong 2 df van dc trong ket qua cuoi
dt7 = pd.merge(dt2, dt5,on="name", how='outer')

# bảng pivoting
# Bảng pivoting“Unpivots” sẽ tạo ra một dataframe từ định dạng rộng sang định dạng dài (xếp chồng lên nhau).
dt8= pd.melt(dt7, id_vars="name", var_name="biến", value_name="giá trị")
# chuyển từ địng dạng dài sang rộng
dt9=dt8.pivot(index='name',columns="biến",values="giá trị")
# dt.head(): lấy 5 hàng đầu tiên của df
# dt.tail(): lấy 5 hàng cuối cùng của df

# count: số lượng mục nhập (dòng) của cột trong DataFrame. Nếu có giá trị bị thiếu (missing value) thì giá trị count sẽ giảm đi tương ứng.
# unique: số lượng giá trị duy nhất trong cột. Chỉ tính cho các cột kiểu dữ liệu không phải là số.
# top: giá trị xuất hiện nhiều nhất trong cột. Chỉ tính cho các cột kiểu dữ liệu không phải là số.
# freq: số lượng lần xuất hiện của giá trị top. Chỉ tính cho các cột kiểu dữ liệu không phải là số.
# mean: giá trị trung bình của cột. Chỉ tính cho các cột kiểu dữ liệu là số.
# std: độ lệch chuẩn của cột. Chỉ tính cho các cột kiểu dữ liệu là số.
# min: giá trị nhỏ nhất trong cột. Chỉ tính cho các cột kiểu dữ liệu là số.
# 25%, 50%, 75%: phân vị 25%, 50% và 75% của các giá trị trong cột. Chỉ tính cho các cột kiểu dữ liệu là số.
# max: giá trị lớn nhất trong cột. Chỉ tính cho các cột kiểu dữ liệu là số.
a=dt1.describe(include="all")
# chỉ định danh sách thông sô muốn trả về ; về số : np.number, kh phải là số: object
# dt1.describe(include=[np.number]).T[['count']]
# dt1.describe(include=[object]).T[['freq']]

# dt1.shape : trích số hàng và số cột của 

# dt1.index
#dt1.columns : cac cot trong dt và kiểu

# dt1.dtypes : kiểm tra kiểu dữ liệu từng cột

# dt1['name'] : trích cột của df

# dt1.iloc[0,]: dung iloc de truy xuat hang
# dt1.iloc[[0,1]] : trich 2 hang dau tien cua df

#Sử dụng loc để lựa chọn dựa trên chỉ số nguyên lẫn một nhãn (label)
# (dt1.loc[[0,1],'name']) : tric cot name hang 1,2
# dt1.loc[1,'name']='vini' : gan lai gia tri cot name hang 1 bang ten khac

# 2.2.5 sap xep

 # Phương thức iterrows(): trả về các cặp,ko cho phép chỉnh sửa dữ liệu 
    #for index, row in dt2.iterrows(): print(row['name'],row['age'])
 
 # phương thức itertuples: trả về các bộ (tuple) của các giá trị; truy xuất các trường có chỉ số nguyên bắt đầu từ 0.
#for tup in dt2.itertuples(): print(tup[1],tup[2])
# thay doi du lieu hang loat 
    #for i in range(dt2.shape[0]): dt2.loc[i,'age']*=5 : nhân 5 cho trường age của dataframe 

# lựa chọn hàng theo phép lọc
   # phép lọc đơn giản trên các giá trị 
dt2[dt2.age<20]
dt2[dt2.job=='student']
dt1[dt1.job.isin(['student', 'teach'])]
dt2[dt2['job'].str.contains("student|engineer")]

# lọc với điều kiện kết hợp
# loc tuoi va lay thong tin cot name, age
dt2[dt2.age>19][['name','age']]
# loc tuoi va gioi tinh roi lay thonh tin name, gender, age
dt2[(dt2.age>19)&(dt2.gender=="M")][['name','gender','age']]

# sắp xếp 
dt10=dt2.copy()
# sap xep df theo tuoi, ascending : True :sx tang dan roi lay thong tin name, tuoi,..
dt10.sort_values(by='age',ascending=True)[['name','age']]
# cach khac
dt10.age.sort_values(ascending=False)
# sap xep uu tien theo thu tu list 
dt10.sort_values(by=['age','name'],ascending=True)
# sắp xếp job  dựa trên thứ tự từ điển, tham số : inplace: tùy lựa chọn lưu vào DataFrame gốc hay không.
print(dt10.sort_values(by=['job','age'],inplace=False))
