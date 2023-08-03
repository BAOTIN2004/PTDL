import pandas as pd
data = pd.read_excel("E:\data\PTDL\ds_salaries.xlsx")
# a2=data[data['job_title']=='Data Scientist']['salary_in_usd']
a3=data[data['job_title']=='Data Analytics Manager']['salary_in_usd']
a4=data[data['job_title']=='Data Analytics Manager']['number of ex _level']

print("Hệ số tương quan giữa ngành 'Data Analytics Manager' với SSkinh nghiệm làm việc: ",a3.corr(a4))
print("Hệ số tương quan giữa ngành 'Data Analytics Manager' với kinh nghiệm làm việc: ",a3.corr(a4))

