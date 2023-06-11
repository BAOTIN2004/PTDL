import pandas as pd


data = pd.read_excel("E:\data\PTDL\ds_salaries.xlsx")
# a2=data[data['job_title']=='Data Scientist']['salary_in_usd']
a3=data[data['job_title']=='Data Analytics Manager']['salary_in_usd']
a4=data[data['job_title']=='Data Analytics Manager']['number of ex _level']
print("Hệ số tương quan giữa ngành 'Data Analytics Manager' với kinh nghiệm làm việc: ",a3.corr(a4))




b=data['job_title'].value_counts()
employee_counts = data['job_title'].value_counts()

# Lọc những ngành có từ 30 đến 50 người làm
filtered_jobs = employee_counts[(employee_counts >=20) & (employee_counts <= 30)]

# In kết quả
# print(filtered_jobs)