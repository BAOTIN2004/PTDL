import pandas as pd

# đọc dữ liệu từ file excel
data=pd.read_excel("E:\data\PTDL\ds_salaries.xlsx")

# kiểm tra xem dữ liệu có bao nhiêu hàng và cột
print('Tập dữ liệu có số hàng và cột lần lượt là',data.shape)

# thống kê lương trung bình theo từng năm bằng bằng USD
print('Lương trung bình của mỗi năm',data.groupby(['work_year'])['salary_in_usd'].mean())

# tính phân vị trong tập dữ liệu với thuộc tính lương (phân vị 25, 50, 75)
print('Phân vị 25 của tập dữ liệu có thuộc tính về lương',data['salary_in_usd'].quantile(0.25))
print('Trung vị của lương nhân viên theo USD',data['salary_in_usd'].quantile(0.5))
print('Phân vị 75 của tập dữ liệu có thuộc tính về lương',data['salary_in_usd'].quantile(0.75))

# tính phương sai 
import numpy as np
# trước tiên cần chuyển danh sách lương về mảng 
salary_arr=np.array(data['salary_in_usd'])
# phương sai của tổng thể
print('Phương sai của tổng thể về lương(USD)',np.var(salary_arr,ddof=0))
# phương sai của mẫu
print('Phương sai của mẫu về lương (USD)',np.var(salary_arr,ddof=1))

# độ lệch chuẩn: là căn  bậc 2 của phương sai

# thống kê max, min của lương 
print('Lương cao nhất:',data['salary_in_usd'].max(),'$')
print('Lương thấp nhất:',data['salary_in_usd'].min(),'$')

# độ chênh lệch của người có lương cao nhất với người thấp nhất
data['salary_in_usd'].max()-data['salary_in_usd'].min()

# thống kê số lượng người trong khoảng lương
bins=[40000,80000,120000,200000,280000,350000,450000]
labels=['40000-80000','80000-120000','120000-200000','200000-280000','280000-350000','350000-450000']
data['Khoang_Luong'] = pd.cut(data['salary_in_usd'], bins=bins, labels=labels, include_lowest=True)
luong_counts = data['Khoang_Luong'].value_counts()
print('Số lượng người trong mỗi khoảng lương\n',luong_counts)
