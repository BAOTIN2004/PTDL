import pandas as pd
import numpy as np
import statistics
# Đọc dữ liệu từ file 
data=pd.read_excel('E:\\data\\PTDL\\ds_salaries.xlsx')

# Lấy cột dữ liệu cần tính phương sai
column_data = data['salary_in_usd']

# Chuyển đổi dữ liệu thành mảng numpy
array_data = np.array(column_data)

# Tính phương sai
column_data1=statistics.mean(column_data)
phuongsai1=np.var(array_data, ddof=1)
phuongsai = np.var(array_data,ddof=0)


# print("giá trị trung bình:",column_data1)
# print('phương sai mẫu:',phuongsai1)
# print("phương sai tổng thể :", phuongsai)

# print(data)
#lọc dữ liệu
# lọc ra các ngành nghề có mức lương lớn hơn 100000 usd
data_loc1 = data[data['salary_in_usd'] > 100000]
print('Lọc ra nhân viên có mức lương lớn hơn 100000(usd) \n',data_loc1)

# lọc ra các công ty size L và công ty đó đến từ US
data_loc2 =data[(data['company_size'] == 'L') & (data['company_location'] == 'US')]
print("Lọc ra nhân viên làm cho các công ty size L và từ US \n",data_loc2)