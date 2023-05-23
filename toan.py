import pandas as pd
data=pd.read_excel("E:\data\PTDL\ds_salaries.xlsx")
import matplotlib.pyplot as plt
x=data['employment_type']
y=data['salary_in_usd']
plt.xlabel('Hình thức làm việc')
plt.ylabel('Lương')
plt.scatter(x,y,c='red',s=20)
plt.title('Biểu đồ phân tán hình thức làm việc với lương')
plt.show()

import seaborn as sns ,numpy as np
meanYearlySalary = np.array(data['salary_in_usd'].groupby(data['work_year']).mean())
plt.xlabel('Năm')
plt.ylabel('$')
plt.title("Trung bình lương các năm")
sns.lineplot(x=['2020', '2021', '2022', '2023'], y=meanYearlySalary)
plt.show()