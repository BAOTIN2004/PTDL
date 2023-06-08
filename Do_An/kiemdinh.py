import pandas as pd
# đọc dữ liệu
data=pd.read_excel('E:\\data\\PTDL\\ds_salaries.xlsx')

# Giả thuyết H0: lương trung bình của hai ngành là giống nhau
# Giả thuyết H1: Lương trung của hai ngành là khác nhau. 
import scipy.stats as stats
# Truy xuẩt dữ liệu cho từng ngành
salary_DA=data[data['job_title']=='Data Analyst']['salary_in_usd']
salary_DE=data[data['job_title']=='Data Engineer']['salary_in_usd']

# Kiểm định t
t_statistic, p_value = stats.ttest_ind(salary_DA,salary_DE)

# Kiểm tra kết quả
alpha = 0.05  # Mức ý nghĩa
if p_value < alpha:
    print("Có sự khác biệt ý nghĩa về mặt thống kê lương trung bình giữa nhóm 'Data Analyst' và nhóm 'Data Engineer'.")
else:
    print("Không có sự khác biệt ý nghĩa về mặt thống kê lương trung bình giữa nhóm 'Data Analyst' và nhóm 'Data Engineer'.")